# Run this script as a scheduled task every hour. It will scan $ScanPath and generate a list of filenames.
# If any files have been in the directory for longer than $TimeThreshold, it will notify you.
# TODO: To reduce volume of emails, have it only send emails once/twice a day?

# Globals
$ScanPath = ".\test"
$OutputPath = ".\results.csv"
$Threshold = 24
$TimeThreshold = New-TimeSpan -Days 0 -Hours $Threshold -Minutes 0

# Email Credentials https://interworks.com/blog/trhymer/2013/07/08/powershell-how-encrypt-and-store-credentials-securely-use-automation-scripts/
$SendEmail = $true
$From = "notifications@example.com"
$To = "admins@example.com"
$Subject = "Stale Files in $ScanPath"
$Body = "This is an automated email to alert you that the following files have been in the '$ScanPath' folder longer than $TimeThreshold :"
$SMTPServer = "smtp.example.com"
$emailusername = "notifications"
$encrypted = Get-Content c:notifications_encrypted_password.txt | ConvertTo-SecureString
$credential = New-Object System.Management.Automation.PsCredential($emailusername, $encrypted)

function Send-Output {
    param([bool]$MailFlag, [string]$Output)
    # Optionally send an email or write to console depending on $MailFlag
    if ($MailFlag) {
    Send-MailMessage -From $From -To $To -Subject $Subject -Body $Output -SmtpServer $SMTPServer -UseSsl -Credential $credential
    } else {
    Write-Output $Output
    }
}

# Read current files and store at end of file
$CurrentTime = Get-Date -uformat "%Y-%m-%d %H%M"
$CurrentFiles = Get-ChildItem -Path $ScanPath -Name -Recurse
$NewLine =,$CurrentTime + $CurrentFiles -join ","
Add-Content -Path $OutputPath $NewLine

# Check if any of files are in previous entry
$Head = (Get-Content $OutputPath -Head 2 | Select-Object -skip 1).split(",") # Oldest Entry
$Tail = (Get-Content $OutputPath -Tail 1).split(",") # Newest Entry
$OldTime = [datetime]::ParseExact($Head[0],"yyyy-MM-dd HHmm", $null)
$OldFiles = $Head[1..$Head.Length]

$CutoffTime = [datetime]::ParseExact($Tail[0],"yyyy-MM-dd HHmm", $null) - $TimeThreshold
$TimeDiff = New-TimeSpan -Start $OldTime -End $CutoffTime
$match = $CurrentFiles | Where-Object { $_ -in $OldFiles } # Get any current files that are also in the oldest entry

if ($match.Length -gt 0 -and $TimeDiff -gt 0) {
    # There are files that have been in the folder longer than is allowed!
    $Body = $Body + $match
    Send-Output $SendEmail $Body
    $LastEmail = $CurrentTime
}
else {
    # No files have been in the folder beyond the threshold.
    # Send-Output $SendEmail "No stale files exist in $ScanPath"
}

# Delete oldest entries if there are too many.
while ((Get-Content $OutputPath | Measure-Object).count -gt $Threshold + 1)
{
    (Get-Content $OutputPath | Select-Object -Skip 2) | Set-Content $OutputPath
}
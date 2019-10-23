"""Create a file with the given size.

Disk usage is actually low even for large files since only a single byte is written.

"""


if __name__ == "__main__":
    units = {"B": 1, "KB": 1024, "MB": 1024 * 1024, "GB": 1024 * 1024 * 1024}

    raw = input("Enter the desired size of file (e.g. 10 MB):\t")

    size, unit = raw.split()
    size = int(size)
    filename = f"{size}_{unit.upper()}.bin"
    unit = units[unit.upper()]

    with open(filename, "wb") as f:
        f.seek(size * unit - 1)
        f.write(b"\0")
    print(f"Created file: {filename}")

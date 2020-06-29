import datetime
import PySimpleGUI as sg


def tick():
    """Return the current date and time as a string."""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


layout = [[sg.Text(tick(), key="Time")]]
window = sg.Window("", auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

while True:
    event, values = window.Read(timeout=2)
    if event is None or event == "Exit":  # Ends the script if the window is closed
        break
    window.FindElement("Time").Update(tick())  # Update the displayed text
window.Close()

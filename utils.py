"""Select file or directory by dialog box."""
import os
import tkinter as tk
from tkinter import filedialog  # This submodule must be explicitly imported.


def prompt_filename(
    initialdir=os.getcwd(),
    title="Please select a file",
    filetypes=(("All Files", ".*"),),
):
    """Prompt the user for the location of a file.

    Keyword Arguments:
        initialdir {string} -- Initial directory to start the file browser in.
            (default: os.getcwd())
        title {string} -- Window title.
            (default: Please select a file")
        filetypes {sequence of tuples} -- Allowed file types and extensions.
            (default: (("All Files", ".*"),))

    Returns:
        string -- Absolute path to selected file.

    """
    root = tk.Tk()
    root.withdraw()  # Hide main window

    # Prompt for the file path
    filename = filedialog.askopenfilename(
        parent=root, initialdir=initialdir, title=title, filetypes=filetypes,
    )

    root.destroy()  # Clean up Tk objects

    return filename


def prompt_directoryname(
    initialdir=os.getcwd(), title="Please select a directory",
):
    """Prompt the user for the location of a directory.

    Keyword Arguments:
        initialdir {string} -- Initial directory to start the file browser in.
            (default: {os.getcwd()})
        title {string} -- Window title
            (default: {"Please select a directory"})

    Returns:
        string -- Absolute path to selected directory.

    """
    root = tk.Tk()
    root.withdraw()  # Hide main window

    # Prompt for the file directory
    filename = filedialog.askdirectory(parent=root, initialdir=initialdir, title=title,)

    root.destroy()  # Clean up Tk objects

    return filename

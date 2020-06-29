"""Flatten a directory.

Any files within that directory will be moved to the base level.
All child directories are removed.
"""
import pathlib
from tkinter import filedialog


def move_files_to_base(current_dir: pathlib.Path, base_dir: pathlib.Path):
    """Move all files in subdirectories to the base directory.

    Args:
        current_dir (pathlib.Path): directory at the current recursive level
        base_dir (pathlib.Path): destination directory
    """
    for p in current_dir.iterdir():
        if p.is_file():
            p.rename(base_dir.joinpath(p.name))
        else:
            move_files_to_base(p, base_dir)


def remove_empty_dir(path):
    """Remove empty directory trees.

    Does not remove directories that contain any files.

    Args:
        path (pathlib.Path): Directory to remove
    """
    try:
        path.rmdir()
    except OSError:
        for p in path.rglob("*"):
            remove_empty_dir(p)
    # Try again after removing child directories
    try:
        path.rmdir()
    except OSError:
        pass


if __name__ == "__main__":
    DIR = pathlib.Path(filedialog.askdirectory())
    move_files_to_base(DIR, DIR)
    remove_empty_dir(DIR)

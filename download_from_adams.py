"""Application to download documents from ADAMS by a list of Accession numbers."""
import requests
from pathlib import Path
import tkinter as tk
from tkinter.filedialog import askdirectory


def select_dir():
    """Ask the user to select a directory."""
    filepath = askdirectory()
    if filepath:
        ent_dir.delete(0, tk.END)
        ent_dir.insert(tk.END, filepath)


def download_files():
    """Retrieve the provided documents from ADAMS."""
    docs = txt_docs.get("1.0", tk.END).splitlines()
    output_dir = Path(ent_dir.get())
    endpoint = "https://adamswebsearch2.nrc.gov/webSearch2/main.jsp"
    for doc in docs:
        if not doc:
            continue
        if "ML" not in doc:
            doc = "ML" + doc
        response = requests.get(endpoint, params={"AccessionNumber": doc.strip()})
        if not response.encoding:
            # ADAMS returns a status 200 even on error
            # so we cannot use that to detect failures
            # Correct responses will not include an encoding, so we use that.
            with output_dir.joinpath(doc + ".pdf").open("wb") as f:
                f.write(response.content)
        else:
            print(f"Error retrieving document {doc} from ADAMS!")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("ADAMS Downloader")
    window.resizable(False, False)

    # Frame 1 - Accession Entry
    fr_1 = tk.Frame(window, relief=tk.SUNKEN, bd=3, padx=5, pady=5)
    fr_1.grid(row=0, column=0, sticky="nsew")

    lbl_instr = tk.Label(
        fr_1, text="Please enter the accession numbers to download on separate lines.",
    )
    lbl_instr.grid(row=0, column=0, sticky="nsew")

    txt_docs = tk.Text(fr_1, bd=3, height=20, width=20)
    txt_docs.grid(row=1, column=0, sticky="nsew")

    # Frame 2 - Output Directory and Submit Button
    fr_2 = tk.Frame(window, relief=tk.SUNKEN, bd=3, padx=5, pady=5)
    fr_2.grid(row=1, column=0, sticky="nsew")

    ent_dir = tk.Entry(fr_2, width=30)
    ent_dir.grid(row=0, column=0, sticky="ew")

    btn_select_dir = tk.Button(
        fr_2, text="Select Output Directory..", command=select_dir
    )
    btn_select_dir.grid(row=0, column=1)

    btn_submit = tk.Button(fr_2, text="Submit", command=download_files)
    btn_submit.grid(row=0, column=2, sticky="e")

    window.mainloop()

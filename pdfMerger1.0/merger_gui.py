import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg
from pypdf import PdfWriter

pdf_list = []   # PDF File List
window = tk.Tk()     # Tkinter Window
window.title("PDF Merger")
tk.Label(window, text="PDF Merger", font=("arial", 20)).pack()
e1 = tk.Entry(window)   # File Name
l1 = tk.Label(window)   # Selected Files
l2 = tk.Label(window, text="filename Output")   # Entry Info
window.geometry("700x500")  # App Resolution
window.resizable(width=False, height=False)

l1.pack()   # Pack Label
l2.pack()   # Pack Label
e1.pack()   # Pack Label


def append_list_to_list():
    global pdf_list, l1

    filename = fd.askopenfilenames(
        title='Open a file',
        initialdir='/')     # select files
    for i in range(len(filename)):
        pdf_list.append(filename[i])    # append Files to pdf

    text = "selected Files:\n"  # get Info text
    for elm in filename:
        text += elm + "\n"  # set Info text
    l1.config(text=text)    # Output of the Info text


def merge_pdfs():
    x = e1.get()
    dictx = fd.askdirectory(title="Open Save Folder", initialdir='/')   # select directory
    merger = PdfWriter()    # implement the PdfWriter
    if dictx == () or dictx == []:
        msg.showerror("PDF Merger", "Merger failed")
        return
    for elm in pdf_list:
        merger.append(elm)  # add the items of pdf list to the merge list
    if e1.get() == "":
        merger.write(dictx + "/" + "result.pdf")    # merge the file without own File name
    else:
        if not e1.get().endswith(".pdf"):
            merger.write(dictx + "/" + e1.get() + ".pdf")   # correct the syntax of merge writer
            x = "/" + e1.get() + ".pdf"
        else:
            merger.write(dictx + "/" + e1.get())    # is no correction then is all perfect
            x = "/" + e1.get()
    merger.close()  # is the progress done then close the merger
    txt = ""
    for elm2 in pdf_list:
        txt += elm2 + "\n" + "\n"
    msg.showinfo("PDF Merger", f"Selected Files:\n{txt}\n are saved in {dictx}{x}")  # You get an information
    exit(0)     # exit for save files


tk.Button(window, text="Select Files", command=append_list_to_list).pack()  # function buttons
tk.Button(window, text="Start Merge ", command=merge_pdfs).pack()


window.mainloop()   # program loop

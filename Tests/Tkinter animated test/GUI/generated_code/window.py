import tkinter as tk


def btn_clicked():
    print("Button Clicked")


window = tk.Tk()

window.geometry("1000x806")
window.configure(bg = "#ff9494")
canvas = tk.Canvas(
    window,
    bg = "#ff9494",
    height = 806,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = tk.PhotoImage(file = f"img0.png")
b0 = tk.Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command=btn_clicked,
    relief = "flat")

b0.place(
    x = 384, y = 566,
    width = 231,
    height = 223)

Entry0_img = tk.PhotoImage(file = f"img_textBox0.png")
Entry0_bg = canvas.create_image(
    499.5, 439.5,
    image = Entry0_img)

Entry0 = tk.Entry(
    bd = 0,
    bg = "#FFD1D1",
    highlightthickness = 0)

Entry0.place(
    x = 274, y = 413,
    width = 451,
    height = 51)

img1 = tk.PhotoImage(file = f"img1.png")
b1 = tk.Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    state="normal",
    relief = "flat")

b1.place(
    x = 365, y = 307,
    width = 269,
    height = 65)

Entry1_img = tk.PhotoImage(file = f"img_textBox1.png")
Entry1_bg = canvas.create_image(
    511.5, 204.5,
    image = Entry1_img)

Entry1 = tk.Entry(
    bd = 0,
    bg = "#FFD1D1",
    highlightthickness = 0)

Entry1.place(
    x = 286, y = 178,
    width = 441,
    height = 41)

img2 = tk.PhotoImage(file = f"img2.png")
b2 = tk.Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    state="normal",
    relief = "flat")

b2.place(
    x = 365, y = 72,
    width = 269,
    height = 65)

window.resizable(False, False)
window.mainloop()

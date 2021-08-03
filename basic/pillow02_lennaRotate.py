from PIL import Image, ImageTk
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

img = Image.open("./img_lenna/lenna.png")
out = img.rotate(45)

#이미지를 tk형식으로 변환
tk_img = ImageTk.PhotoImage(out)

canvas.create_image(250, 250, image=tk_img)

window.mainloop()
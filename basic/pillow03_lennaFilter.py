from PIL import Image, ImageTk, ImageFilter
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

img = Image.open("files/img_lenna/lenna.png")
out = img.filter(ImageFilter.BLUR)

#이미지를 tk형식으로 변환
tk_img = ImageTk.PhotoImage(out)

canvas.create_image(250, 250, image=tk_img)

window.mainloop()
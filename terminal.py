import tkinter as tk
from tkinter import Button
import cv2
from PIL import Image, ImageTk
import predict_opt
import choose
class CountdownApp:
    def __init__(self, master):
        self.master = master
        self.scan_button = Button(root, text="Scan", command=self.onClick, height=5, width=10)
        self.scan_button.pack(padx=20, pady=20)
        self.label1 = tk.Label(self.master)  
        self.master.title("Terminal emulation")
    def onClick(self):
        self.scan_button.destroy()
        self.label1.pack()
        self.get_images()

    def get_images(self):
        result = predict_opt.trayclf()
        rgb_image= cv2.cvtColor(result[0], cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(image=Image.fromarray(rgb_image))
        self.label1.config(image=photo)
        self.label1.image = photo
        choose.chs(result[1])




if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()

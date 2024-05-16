import tkinter as tk
from tkinter import simpledialog
import cv2 as cv
import os
from PIL import Image, ImageTk
import camera

class App:

    def __init__(self, window=tk.Tk(), window_title="Camera Classifier"):
        self.window = window
        self.window.title(window_title)
        self.camera = camera.Camera()

        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()

        self.update_frame()

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_frame(self):
        ret, frame = self.camera.get_frame()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(10, self.update_frame)

    def on_closing(self):
        del self.camera
        self.window.destroy()

if __name__ == "__main__":
    app = App()
    app.window.mainloop()

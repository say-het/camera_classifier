import tkinter as tk
from tkinter import simpledialog
import cv2 as cv
import os
import PIL.Image, PIL.ImageTk
import camera

class App:

    def __init__(self,window=tk.Tk(),window_title="Camera Classifier"):
        self.window = window;
        self.window_title = window_title;
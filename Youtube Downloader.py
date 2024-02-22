import tkinter as tk
from tkinter import filedialog
from video_downloader import video_download as vd
import os
from PIL import ImageTk, Image

# globals
path = os.getcwd()
permanent_frame = None


def getPath():
    global path
    path = filedialog.askdirectory(initialdir='/', title='Select directory')


def downloadVideo_command(url):
    global path
    global permanent_frame
    vd(url, path)
    done_label = tk.Label(permanent_frame, text='Done!')
    done_label.grid(row=1, column=0, padx=10)


def main():
    # setting up root
    root = tk.Tk()
    root.geometry('1047x450')
    root.title('YouTube Downloader')

    # setting up the main frame which has deletable elements
    main_frame = tk.LabelFrame(root, text="Enter the url", padx=200, pady=100)
    main_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, ipadx=12)

    url_holder = tk.Entry(main_frame, width=100)
    url_holder.grid(row=0, column=0, columnspan=4)

    # setting up the permanent frame which does not delete elements
    permanent_frame = tk.Frame(main_frame, pady=50, padx=250)
    permanent_frame.grid(row=1, column=1)

    # declaring buttons
    download_button = tk.Button(permanent_frame, text='Download', command=lambda: downloadVideo_command(url_holder.get()
                                                                                                        ))
    path_button = tk.Button(permanent_frame, text='Pick directory to save', command=getPath)

    # printing buttons
    download_button.grid(row=1, column=0, ipadx=20)
    path_button.grid(row=0, column=0, ipadx=17)
    root.mainloop()


if __name__ == '__main__':
    main()

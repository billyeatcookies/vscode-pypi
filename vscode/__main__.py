import platform
import tkinter as tk

if platform.system() != 'Windows':
    print("System does not support webview")
    exit()

import clr
from tkwebview2.tkwebview2 import WebView2, have_runtime, install_runtime

from .utils import dark

clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Threading')

from System.Threading import ApartmentState, Thread, ThreadStart
from System.Windows.Forms import Control


def load_vscode():
    if not have_runtime():
        install_runtime()
    
    root = tk.Tk()
    dark(root)
    root.config(background="black")
    root.geometry('1200x600+5+5')
    root.update()
    root.update_idletasks()
    root.title('Visual Studio Code')

    view = WebView2(root, 500, 500, background="black")
    view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    view.load_url('https://vscode.dev')

    root.mainloop()

t = Thread(ThreadStart(load_vscode))
t.ApartmentState = ApartmentState.STA
t.Start()
t.Join()

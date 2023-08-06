import ctypes as ct

def dark(window):
    # https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    window.update()
    value = ct.c_int(2)
    ct.windll.dwmapi.DwmSetWindowAttribute(
        ct.windll.user32.GetParent(window.winfo_id()), 20, 
        ct.byref(value), ct.sizeof(value))

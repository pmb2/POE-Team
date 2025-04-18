# sync_esc_client.py (Run this on other PCs)
import socket
import ctypes
import time
import sys
from ctypes.wintypes import HWND, DWORD, WPARAM, LPARAM

# Auto-configure firewall
try:
    import os

    os.system('netsh advfirewall firewall add rule name="ESC Sync" dir=in action=allow protocol=UDP localport=51987')
except:
    pass

user32 = ctypes.WinDLL('user32')
EnumWindows = user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowTextLength = user32.GetWindowTextLengthW
GetWindowText = user32.GetWindowTextW

POE_TITLE = "Path of Exile"
HOST_IP = input("Enter host IP address: ")


def get_poe_hwnd():
    hwnds = []

    def foreach_window(hwnd, lParam):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        if POE_TITLE in buff.value:
            hwnds.append(hwnd)
        return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)
    return hwnds[0] if hwnds else None


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 0))
sock.sendto(b'REGISTER', (HOST_IP, 51987))

print("Connected to ESC Sync! Path of Exile will now sync ESC presses")
print("(This window can be minimized but must stay running)")

while True:
    sock.settimeout(0.1)
    try:
        data = sock.recv(1024)
        if data == b'ESC' and get_poe_hwnd():
            user32.keybd_event(0x1B, 0, 0, 0)  # Send ESC
            user32.keybd_event(0x1B, 0, 2, 0)
    except:
        pass
    time.sleep(0.01)

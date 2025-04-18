# sync_esc_host.py (Run this FIRST on the hosting PC)
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

POE_TITLE = "Path of Exile 2"


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
sock.bind(('0.0.0.0', 51987))
clients = set()

print("Hosting ESC Sync server! Share your public IP with friends")
print("(This window can be minimized but must stay running)")

while True:
    data, addr = sock.recvfrom(1024)
    if data == b'REGISTER':
        clients.add(addr)
        print(f"New client: {addr[0]}")
    elif data == b'ESC':
        if get_poe_hwnd():
            user32.keybd_event(0x1B, 0, 0, 0)  # Send ESC
            user32.keybd_event(0x1B, 0, 2, 0)
        for client in clients:
            if client != addr:
                sock.sendto(b'ESC', client)
    time.sleep(0.01)

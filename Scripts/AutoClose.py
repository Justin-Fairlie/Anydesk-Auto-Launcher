import time
import subprocess
import win32gui
import win32con
import win32api
import win32process
import win32gui_struct
import pywintypes

def get_window_rect(hwnd):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowVisible(hwnd):
        rect = win32gui.GetWindowRect(hwnd)
        # Return a tuple of (left, top, width, height)
        return rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1]
    else:
        return None

def get_window_title(hwnd):
    return win32gui.GetWindowText(hwnd)

def get_window_pid(hwnd):
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    return pid

def get_all_windows():
    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            windows.append(hwnd)
        return True

    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows

def main():
    while True:
        # Get all visible windows
        windows = get_all_windows()

        # Filter AnyDesk windows
        anydesk_windows = [hwnd for hwnd in windows if "AnyDesk" in get_window_title(hwnd)]

        # Get monitor information
        monitors = win32api.EnumDisplayMonitors(None, None)

        # Move the first AnyDesk window to the first monitor and maximize it
        rect1 = get_window_rect(anydesk_windows[0])
        if rect1:
            monitor_info = win32api.GetMonitorInfo(monitors[0][0])
            monitor_area = monitor_info['Monitor']
            win32gui.SetWindowPos(anydesk_windows[0], win32con.HWND_TOPMOST, monitor_area[0], monitor_area[1], rect1[2], rect1[3], 0)
            win32gui.ShowWindow(anydesk_windows[0], win32con.SW_MAXIMIZE)

        print("AnyDesk windows moved and maximized successfully.")

        # Wait for 2 minutes
        time.sleep()

        # Prepare the CMD command you want to execute
        cmd_command = "taskkill/im anydesk.exe"

        # Use subprocess to run the command
        process = subprocess.Popen(cmd_command, shell=True)
        process.communicate()


if __name__ == "__main__":
    main()



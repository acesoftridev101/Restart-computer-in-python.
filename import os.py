import os
import platform

def restart_computer():
    """Restarts the computer immediately."""
    os_name = platform.system()

    if os_name == "Windows":
        # Command for Windows: /r for restart, /t 0 for 0 second delay, /f to force running apps to close
        os.system("shutdown /r /f /t 0")
    elif os_name == "Darwin":
        # Command for macOS: -r for restart, "now" for immediate execution; usually requires sudo privileges
        os.system("sudo shutdown -r now")
    elif os_name == "Linux":
        # Command for Linux: reboot command; usually requires sudo privileges
        os.system("sudo reboot")
    else:
        print(f"Unsupported operating system: {os_name}")

if __name__ == "__main__":
    confirm = input("Are you sure you want to restart your computer? (yes/no): ")
    if confirm.lower() == 'yes':
        print("Restarting the computer...")
        restart_computer()
    else:
        print("Restart cancelled.")

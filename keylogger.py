import psutil
import argparse
from colorama import init, Fore
from datetime import datetime

# Initialize colorama for colored terminal output
init(autoreset=True)

# List of common suspicious keywords
keylogger_signatures = [
    "keylogger", "klg", "logger", "spy", "hook", "capture", "record", "keyboard"
]

def detect_keyloggers():
    suspicious_processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            pname = proc.info['name'].lower()
            cmdline = ' '.join(proc.info['cmdline']).lower() if proc.info['cmdline'] else ""

            # Check in process name or command line
            for keyword in keylogger_signatures:
                if keyword in pname or keyword in cmdline:
                    suspicious_processes.append((proc.info['pid'], proc.info['name'], cmdline))
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return suspicious_processes

def save_to_log(detected):
    with open("keylogger_log.txt", "a") as f:
        f.write(f"\n\n[SCAN: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
        if detected:
            for pid, name, cmd in detected:
                f.write(f"PID: {pid} | Name: {name} | Cmdline: {cmd}\n")
        else:
            f.write("No suspicious keylogger processes detected.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Keylogger Detector")
    parser.add_argument("--log", action="store_true", help="Save output to keylogger_log.txt")
    args = parser.parse_args()

    print(Fore.CYAN + "🔍 Scanning for suspicious keylogger processes...\n")

    detected = detect_keyloggers()

    if detected:
        print(Fore.RED + "⚠️ Potential keylogger processes found:\n")

        # Print table header
        print(Fore.YELLOW + f"{'PID':<10}{'Process Name':<30}{'Command Line'}")
        print(Fore.YELLOW + "-" * 80)

        # Print each detected process in formatted rows
        for pid, name, cmd in detected:
            print(Fore.LIGHTYELLOW_EX + f"{pid:<10}{name:<30}{cmd}")
    else:
        print(Fore.GREEN + "✅ No suspicious keylogger processes detected.")

    if args.log:
        save_to_log(detected)
        print(Fore.BLUE + "\n📁 Results saved to keylogger_log.txt")

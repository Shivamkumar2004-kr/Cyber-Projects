import socket

# List of common ports you can expand later
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL"
}

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)  # fast scan
        sock.connect((ip, port))
        return True
    except:
        return False
    finally:
        sock.close()

def main():
    target = input("🔍 Enter IP address or domain to scan: ")

    print(f"\nScanning {target}...\n")
    for port, service in common_ports.items():
        if scan_port(target, port):
            print(f"✅ Port {port} ({service}) is OPEN")
        else:
            print(f"❌ Port {port} ({service}) is CLOSED")

if __name__ == "__main__":
    main()

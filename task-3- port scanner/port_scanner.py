import socket
import time


def scan_ports(target, start_port, end_port):
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\nError: Could not find that host/domain.")
        return

    print("\n====================================")
    print("        PORT SCANNER REPORT")
    print("====================================")
    print("Target Host :", target)
    print("Target IP   :", target_ip)
    print("Port Range  :", start_port, "to", end_port)
    print("Scanning... Please wait.\n")

    start_time = time.time()
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target_ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Unknown"
            print(f"[OPEN] Port {port} ({service})")
            open_ports.append(port)

        sock.close()

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    print("\n====================================")
    print("Scan Completed in", time_taken, "seconds")
    print("Total Open Ports Found:", len(open_ports))
    print("====================================")


def main():
    print("====================================")
    print("       PYTHON PORT SCANNER")
    print("====================================")
    print("Tip: For safe testing, use 127.0.0.1 or scanme.nmap.org\n")

    target = input("Enter target IP or domain: ")
    start_port = int(input("Enter start port (example: 20): "))
    end_port = int(input("Enter end port (example: 100): "))

    scan_ports(target, start_port, end_port)


if __name__ == "__main__":
    main()
import socket
import yaml
import nmap

def run_scan():
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    ip_range = config["network_scan"]["ip_range"]
    ports = config["network_scan"]["ports"]

    print(f"[*] Escaneando la red: {ip_range}")

    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments="-p " + ",".join(map(str, ports)) + " --open")

    for host in nm.all_hosts():
        print(f"\nHost detectado: {host} ({nm[host].hostname()})")
        for proto in nm[host].all_protocols():
            print(f"  Protocolo: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                print(f"    - Puerto {port}: {nm[host][proto][port]['state']} ({nm[host][proto][port]['name']})")

if __name__ == "__main__":
    run_scan()

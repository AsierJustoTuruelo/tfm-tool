import argparse
from modules import network_scan, host_scan, crypto_evaluation, report_generation

def main():
    parser = argparse.ArgumentParser(description="Crypto Inventory Scanner")
    parser.add_argument("--network", help="Escaneo de red", action="store_true")
    parser.add_argument("--host", help="Escaneo de host local", action="store_true")
    args = parser.parse_args()

    if args.network:
        network_scan.run_scan()
    elif args.host:
        host_scan.run_scan()
    else:
        print("Usage: python main.py --network | --host")

if __name__ == "__main__":
    main()

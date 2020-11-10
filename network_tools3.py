import argparse
import modules.data
import modules.resolve
import modules.curl
from modules import *
import sys


def banner():
    print("    ____        __  __                   _   __     __                      __      ______            __")
    print("   / __ \__  __/ /_/ /_  ____  ____     / | / /__  / /__      ______  _____/ /__   /_  __/___  ____  / /____")
    print("  / /_/ / / / / __/ __ \/ __ \/ __ \   /  |/ / _ \/ __/ | /| / / __ \/ ___/ //_/    / / / __ \/ __ \/ / ___/")
    print(" / ____/ /_/ / /_/ / / / /_/ / / / /  / /|  /  __/ /_ | |/ |/ / /_/ / /  / ,<      / / / /_/ / /_/ / (__  ) ")
    print("/_/    \__, /\__/_/ /_/\____/_/ /_/  /_/ |_/\___/\__/ |__/|__/\____/_/  /_/|_|    /_/  \____/\____/_/____/")
    print("      /____/")
    print("")
    print("by: sneakerhax")
    print("")


def main():
    banner()
    parser = argparse.ArgumentParser(description='Python Network Tools')
    parser.add_argument('--ucurl', action='store_true', help='Curl a provided URL with urllib must use http://')
    parser.add_argument('--mx', action='store_true', help='Lookup MX record')
    parser.add_argument('--dnsresolve', action='store_true', help='resolve hostname')
    parser.add_argument('--dnsreverse', action='store_true', help='reverse lookup')
    parser.add_argument('--targets', required=True, help='file to open')
    args = parser.parse_args()

    if args.ucurl:
        host_list = data.make_list_file(args.targets)
        curl.urllib_curl(host_list)
    if args.mx:
        host_list = data.make_list_file(args.targets)
        resolve.mx_lookup(host_list)
    if args.dnsresolve:
        host_list = data.make_list_file(args.targets)
        resolve.resolve_hostname(host_list)
    if args.dnsreverse:
        ip_list = data.make_list_file(args.targets)
        resolve.reverse_lookup(ip_list)


if __name__ == "__main__":
    main()

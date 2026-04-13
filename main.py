import requests
import socket
import phonenumbers
from phonenumbers import geocoder, carrier
import dns.resolver
from colorama import Fore, Style, init
import os
import shutil

# ===== CLEAR SCREEN =====
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ===== CENTER TEXT =====
def center(text):
    columns = shutil.get_terminal_size().columns
    return "\n".join(line.center(columns) for line in text.split("\n"))

init(autoreset=True)

# ===== UI =====
def banner():
    print(Fore.WHITE + Style.BRIGHT + center("""
███████╗███████╗██████╗  ██████╗ ████████╗██████╗  █████╗  ██████╗███████╗
╚══███╔╝██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
  ███╔╝ █████╗  ██████╔╝██║   ██║   ██║   ██████╔╝███████║██║     █████╗  
 ███╔╝  ██╔══╝  ██╔══██╗██║   ██║   ██║   ██╔══██╗██╔══██║██║     ██╔══╝  
███████╗███████╗██║  ██║╚██████╔╝   ██║   ██║  ██║██║  ██║╚██████╗███████╗
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝
"""))

def menu():
    print(Fore.LIGHTBLACK_EX + center("""
[1] Email OSINT
[2] Phone Number Info
[3] Sherlock Username Search
[4] Holehe Email Check
[5] Port Scanner
[6] IP Info Lookup
[7] DNS Lookup
[8] Username Generator
[9] Metadata Extractor
[10] Password Leak Check
[0] Exit
"""))

# ===== TOOLS =====

# [1] Email OSINT
def email_osint():
    email = input(center("Email: "))
    print(center(f"https://www.google.com/search?q=\"{email}\""))
    print(center(f"https://www.google.com/search?q=site:linkedin.com \"{email}\""))
    print(center(f"https://www.google.com/search?q=site:facebook.com \"{email}\""))

# [2] Phone Info
def phone_lookup():
    number = input(center("Phone (+123...): "))
    parsed = phonenumbers.parse(number)

    print(center("Location: " + geocoder.description_for_number(parsed, "en")))
    print(center("Carrier: " + carrier.name_for_number(parsed, "en")))

# [3] Sherlock
def sherlock_search():
    username = input(center("Username: "))
    os.system(f"sherlock {username}")

# [4] Holehe
def holehe_check():
    email = input(center("Email: "))
    os.system(f"holehe {email}")

# [5] Port Scanner
def port_scan():
    target = input(center("IP/Host: "))
    print(center("Scanning..."))

    for port in range(20, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(center(f"Open port: {port}"))
        sock.close()

# [6] IP Info
def ip_lookup():
    ip = input(center("IP: "))
    res = requests.get(f"http://ip-api.com/json/{ip}").json()

    for k, v in res.items():
        print(center(f"{k}: {v}"))

# [7] DNS Lookup
def dns_lookup():
    domain = input(center("Domain: "))
    result = dns.resolver.resolve(domain, 'A')

    for ip in result:
        print(center(f"IP: {ip}"))

# [8] Username Generator
def username_gen():
    name = input(center("Name: "))
    print(center(name + "123"))
    print(center(name + "_official"))
    print(center("real_" + name))
    print(center(name + "_x"))

# [9] Metadata Extractor
def metadata():
    file = input(center("File path: "))
    try:
        from PIL import Image
        img = Image.open(file)
        print(center(str(img.info)))
    except:
        print(center("Error reading metadata."))

# [10] Leak Check
def leak_check():
    email = input(center("Email: "))
    print(center("Check: https://haveibeenpwned.com/"))
    print(center(f"Search: {email}"))

# ===== MAIN =====
def main():
    while True:
        clear()
        banner()
        menu()

        choice = input(center("Select: "))

        if choice == "1":
            email_osint()
        elif choice == "2":
            phone_lookup()
        elif choice == "3":
            sherlock_search()
        elif choice == "4":
            holehe_check()
        elif choice == "5":
            port_scan()
        elif choice == "6":
            ip_lookup()
        elif choice == "7":
            dns_lookup()
        elif choice == "8":
            username_gen()
        elif choice == "9":
            metadata()
        elif choice == "10":
            leak_check()
        elif choice == "0":
            break
        else:
            print(center("Invalid"))

        input(center("\nPress Enter..."))

if __name__ == "__main__":
    main()

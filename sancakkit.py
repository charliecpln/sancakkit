#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Coded by      @charliecpln
# Discord:      @charliecpln
# Telegram:     @charliecpln
# Github:       @charliecpln

#KÜTÜPHANELER
import os
from sys import exit
import time

def sil():
    try:
        name = os.name
        if name == "nt":
            os.system("cls")

        elif name == "posix":
            os.system("clear")
            
        else:
            print("[!] Unsupported operating system!")
            input("Press enter to continue...")
    
    except Exception as e:
        print(f"[X] Error: {e}")
        input("Press enter to continue...")
sil()

def check_libraries():
    try:
        sil()
        import requests
        import whois
        import dns.resolver
        import instaloader
        from colorama import Fore, Back, Style, init
        from bs4 import BeautifulSoup

    except ImportError:
        oto_indirilsin_mi = input(f"[!] Missing libraries found, download automatically(y/n): ").lower().strip()
        if oto_indirilsin_mi == "y":
            installation()
            globals().update(
                {lib: __import__(lib) for lib in ["requests", "whois", "dns.resolver", "instaloader"]}
            )
            from colorama import Fore, Back, Style, init
            from bs4 import BeautifulSoup

        elif oto_indirilsin_mi == "n":
            print("[!] Libraries are required for the program to function!")
            input("Press enter to continue...")

        else:
            print("[X] Libraries not installed. Exiting...")
            input("Press enter to continue...")
            exit(1)

def installation():
    try:
        os.system("pip install requests python-whois dnspython instaloader colorama beautifulsoup4")
        print("[+] Successfully downloaded")
        sil()

    except Exception as e:
        print(f"[X] Error: {e}")
        input("Press enter to continue...")
        exit(1)

check_libraries()

# KÜTÜPHANELER 2
import requests
import whois as whois_module
import dns.resolver
import instaloader
from colorama import Fore, Back, Style, init
from bs4 import BeautifulSoup

# COLORAMA AUTORESETİ
init(autoreset=True)

# BANNER
def banner():
    banner = Fore.LIGHTRED_EX + Style.BRIGHT + """
███████╗ █████╗ ███╗   ██╗ ██████╗ █████╗ ██╗  ██╗    ██╗  ██╗██╗████████╗
██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗██║ ██╔╝    ██║ ██╔╝██║╚══██╔══╝
███████╗███████║██╔██╗ ██║██║     ███████║█████╔╝     █████╔╝ ██║   ██║   
╚════██║██╔══██║██║╚██╗██║██║     ██╔══██║██╔═██╗     ██╔═██╗ ██║   ██║   
███████║██║  ██║██║ ╚████║╚██████╗██║  ██║██║  ██╗    ██║  ██╗██║   ██║   
╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝   ╚═╝   
                                                       @charliecpln - v1.0
"""
    print(banner)

# FONKSİYONLAR
def ip_info():
    try:
        sil()
        banner()
        ip = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "[?] Enter the IP address: ")
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            ip_info_data = {
                "IP": data.get("query"),
                "Country": data.get("country"),
                "Region Name": data.get("regionName"),
                "City": data.get("city"),
                "ISP": data.get("isp"),
                "Org": data.get("org"),
                "Zip": data.get("zip"),
                "Time Zone": data.get("timezone"),
                "As": data.get("as")
            }
            for key, value in ip_info_data.items():
                print(f"{key}: {value}")

            kayit_edilsin_mi = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "\n[?] Do you want to save to file (y/n): ").lower().strip()
            if kayit_edilsin_mi == "y":
                try:
                    with open("ipinfo.txt", "a", encoding="utf-8") as dosya:
                        for key, value in ip_info_data.items():
                            dosya.write(f"{key}: {value}\n")
                        dosya.write("\n")
                    return main_menu()

                except Exception as e:
                    print(Fore.RED + f"[X] Error while saving file: {e}")
                    input("Press enter to continue...")
                    return main_menu()
            else:
                return main_menu()
        
        else:
            print(Fore.RED + "[X] Error: Unknown error")
            input("Press enter to continue...")
            return main_menu()
        
    except KeyboardInterrupt:
        return main_menu()

def whois_query():
    sil()
    banner()
    domain = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "[?] Please enter a domain: ").lower().strip()

    try:
        domain_info = whois_module.whois(domain)
        whois_data = {
            "Domain name": domain_info.get('domain_name', 'N/A'),
            "Registrar": domain_info.get('registrar', 'N/A'),
            "Creation date": format_date(domain_info.get('creation_date')),
            "Expiration date": format_date(domain_info.get('expiration_date')),
            "Updated date": format_date(domain_info.get('updated_date')),
            "Status": format_list(domain_info.get('status')),
            "Name servers": format_list(domain_info.get('name_servers')),
            "Registrant name": domain_info.get('registrant_name', 'N/A'),
            "Registrant organization": domain_info.get('registrant_organization', 'N/A'),
            "Registrant email": domain_info.get('registrant_email', 'N/A'),
            "Registrant phone": domain_info.get('registrant_phone', 'N/A'),
            "Registrant address": domain_info.get('registrant_address', 'N/A'),
            "Admin name": domain_info.get('admin_name', 'N/A'),
            "Admin email": domain_info.get('admin_email', 'N/A'),
            "Admin phone": domain_info.get('admin_phone', 'N/A'),
            "Tech name": domain_info.get('tech_name', 'N/A'),
            "Tech email": domain_info.get('tech_email', 'N/A'),
            "Tech phone": domain_info.get('tech_phone', 'N/A'),
            "Country": domain_info.get('country', 'N/A'),
            "City": domain_info.get('city', 'N/A'),
            "Postal code": domain_info.get('postal_code', 'N/A'),
            "IP address": domain_info.get('ip', 'N/A'),
        }

        print("\n[+] WHOIS Information for domain:", domain)
        for key, value in whois_data.items():
            print(f"{key}: {value}")

        save_choice = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "[?] Do you want to save this WHOIS information to a file (y/n): ").lower().strip()

        if save_choice == 'y':
            with open(f"{domain}_whois_data.txt", "w") as file:
                for key, value in whois_data.items():
                    file.write(f"{key}: {value}\n")
            print(f"[+] WHOIS information saved to {domain}_whois_data.txt")
            input("Press enter to continue...")

        else:
            return main_menu()

        return main_menu()

    except Exception as e:
        print(f"[X] Error occurred: {str(e)}")
        input("Press enter to continue...")
        return main_menu()
    
    except KeyboardInterrupt:
        return main_menu()
    
def format_date(date_info):
    if isinstance(date_info, list):
        date_info = date_info[0]
    return date_info if date_info else 'N/A'

def format_list(value):
    if isinstance(value, list):
        return ', '.join(value)
    return value if value else 'N/A'

def username_search():
    sil()
    banner()
    try:
        username = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "[?] Please enter a username: ")

        platforms = {
            "Instagram": f"https://www.instagram.com/{username}/",
            "Twitter": f"https://x.com/{username}",
            "GitHub": f"https://github.com/{username}",
            "TikTok": f"https://www.tiktok.com/@{username}",
            "Youtube": f"https://www.youtube.com/@{username}",
            "Telegram": f"https://t.me/{username}",
            "Facebook": f"https://www.facebook.com/{username}",
            "Reddit": f"https://www.reddit.com/user/{username}",
            "LinkedIn": f"https://www.linkedin.com/in/{username}",
            "Pinterest": f"https://www.pinterest.com/{username}",
            "Snapchat": f"https://www.snapchat.com/add/{username}",
            "Twitch": f"https://www.twitch.tv/{username}",
            "Kick": f"https://kick.com/{username}",
            "Spotify": f"https://open.spotify.com/user/{username}",
            "Vimeo": f"https://vimeo.com/{username}",
            "Patreon": f"https://www.patreon.com/{username}",
            "Onlyfans": f"https://onlyfans.com/{username}"
        }

        for platform, url in platforms.items():
            try:
                response = requests.get(url)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')

                    if platform == "Instagram":
                        if "not found" in soup.title.string.lower() or "sorry, this page isn't available" in soup.get_text().lower():
                            print(Fore.LIGHTRED_EX + Style.DIM + f"[-] Instagram: {url}")
                        else:
                            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"[+] Instagram: {url}")

                    elif platform == "Twitter":
                        if "page does not exist" in soup.get_text().lower():
                            print(Fore.LIGHTRED_EX + Style.DIM + f"[-] Twitter: {url}")
                        else:
                            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"[+] Twitter: {url}")

                    elif platform == "GitHub":
                        if "page not found" in soup.get_text().lower():
                            print(Fore.LIGHTRED_EX + Style.DIM + f"[-] GitHub: {url}")
                        else:
                            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"[+] GitHub: {url}")
                    
                    elif platform == "TikTok":
                        if "page not found" in soup.get_text().lower():
                            print(Fore.LIGHTRED_EX + Style.DIM + f"[-] TikTok: {url}")
                        else:
                            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"[+] TikTok: {url}")
                    
                    elif platform == "Youtube":
                        if "404" in soup.get_text() or "this page isn’t available" in soup.get_text().lower():
                            print(Fore.LIGHTRED_EX + Style.DIM + f"[-] Youtube: {url}")
                        else:
                            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"[+] Youtube: {url}")

                else:
                    print(Fore.LIGHTRED_EX + Style.DIM + f"[-] {platform}: {url}")

            except requests.RequestException as e:
                print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f"[!] {platform}: {url}")

        input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "\nPress Enter to continue...")
        return main_menu()

    except KeyboardInterrupt:
        print("\nProgramdan çıkılıyor...")
    
def instagram_osint():
    sil()
    banner()
    L = instaloader.Instaloader()
    username = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "[?] Please enter a username: ").lower().strip()
    
    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print(f"Profile Info for {username}:")
        print(f"Full Name: {profile.full_name}")
        print(f"Bio: {profile.biography}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Posts: {profile.mediacount}")
        print(f"Is Private: {profile.is_private}")
        print(f"Is Verified: {profile.is_verified}")

        kayit_edilsin_mi = input(Style.BRIGHT + Fore.LIGHTCYAN_EX + "[?] Do you want save to file (y/n): ").lower().strip()
        if kayit_edilsin_mi == "y":
            with open(f"{username}_data.txt", "w") as file:
                file.write(f"Profile Info for {username}:\n")
                file.write(f"Full Name: {profile.full_name}\n")
                file.write(f"Bio: {profile.biography}\n")
                file.write(f"Followers: {profile.followers}\n")
                file.write(f"Following: {profile.followees}\n")
                file.write(f"Posts: {profile.mediacount}\n")
                file.write(f"Is Private: {profile.is_private}\n")
                file.write(f"Is Verified: {profile.is_verified}\n")
                print(f"[+] Data saved to '{username}_data.txt'")

        else:
            return main_menu()

        input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "\nPress Enter to continue...")
        return main_menu()

    except instaloader.exceptions.InstaloaderException as e:
        print(f"[X] Error {str(e)}")
        input("\nPress Enter to continue...")
        return main_menu()
    
    except KeyboardInterrupt:
        return main_menu()

def about_the_program():
    sil()
    banner()
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + """
This program is called "Sancak KIT"

This program was written by @charliecpln using python3, covers basic OSINT features and is distributed as open source.

This program was written on behalf of Sancak Offensive Club.

If you find any errors or want to make a suggestion, you can contact us through our accounts in the main menu.

          Version: v1.0
""")
    
    input("\nPress Enter to continue...")
    return main_menu()

def contact():
    sil()
    banner()
    print("Telegram: https://t.me/charliecpln                  -               @charliecpln")
    print("GitHub: https://github.com/charliecpln              -               @charliecpln")
    print("TurkHackTeam: https://www.turkhackteam.org/uye/charliex2.1016339/ - @charliex2")
    
    input("\nPress Enter to continue...")
    return main_menu()

def qquit():
    sil()
    exit(1)

# ANA MENÜ
def main_menu():
    try:
        sil()
        banner()
        menu = Fore.LIGHTGREEN_EX + Style.BRIGHT + """
        [1] - Ip Query
        [2] - Whois Query
        [3] - Username Search
        [4] - Instagram Osint

        [A] - About the program
        [C] - Contact
        [Q] - Exit
        
        """
        print(menu)
        secenek = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "[?] Please select an option: ").lower().strip()

        if secenek == "1" or secenek == "i":
            ip_info()

        elif secenek == "2" or secenek == "w":
            whois_query()

        elif secenek == "3" or secenek == "u":
            username_search()

        elif secenek == "4" or secenek == "ig":
            instagram_osint()

        elif secenek == "a" or secenek == "about":
            about_the_program()

        elif secenek == "c" or secenek == "contact" or secenek == "ct":
            contact()

        elif secenek == "q" or secenek == "x" or secenek == "e" or secenek == "quit" or secenek == "exit":
            qquit()

        else:
            return main_menu()
        
    except KeyboardInterrupt:
        return main_menu()

sil()
main_menu()

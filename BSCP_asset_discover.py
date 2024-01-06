#!/usr/bin/python3

"""
Script aimed to ease the detection of possible vulnerabilities during BSCP exam

Made with <3 by SolracS
"""

import requests
import argparse
from termcolor import colored

def check_robots(base_url):
    url = base_url + 'robots.txt'
    r = requests.get(url)
    if r.status_code == 200:
        print(colored('\n[*] Robots.txt detected', 'yellow'))
        lines = r.text.split('\n')
        for line in lines[0:-1]:
            print(colored('\t[+] '+line))
    else:
        print(colored('\n[*] Robots.txt NOT detected', 'yellow'))

def check_login(base_url):
    url = base_url + 'login'
    r = requests.get(url)
    if r.status_code == 200:
        print(colored('\n[*] Login detected detected', 'yellow'))
        print(colored('\t[+] Trying to IDOR my-account...', 'yellow'))
        idor_url = base_url + 'my-account?id='
        r_idor = requests.get(idor_url+'wiener')
        if r.status_code == 200 or r.content != requests.get(idor_url+'carlos'):
            print(colored('\t\t[x] Posible IDOR at id parameter', 'red'))
        else:
            print(colored('\t\t[x] IDOR NOT detected at id parameter', 'red'))

    else:
        print(colored('\n[*] Login detected NOT detected', 'yellow'))

def check_default_admin_panel(base_url):
    url = base_url + 'admin'
    r = requests.get(url)
    if r.status_code != 400:
        print(colored('\n[*] Default admin panel at /admin detected detected', 'red'))
    else:
        print(colored('\n[*] Default admin panel at /admin detected NOT detected', 'green'))

def check_DOM_xss(base_url):
    # Add list of DOM XSS vulnerable js functions and check if any is present
    pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", type=str, required=True, help="Target's url")

    args = parser.parse_args()

    check_robots(args.target)
    check_login(args.target)
    check_default_admin_panel(args.target)


if __name__ == '__main__':
    main()

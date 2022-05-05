# -*- coding: UTF-8 -*-

import requests
import lxml
from bs4 import BeautifulSoup
import os
import msvcrt


WEBSITE_1 = "https://ipaddress.com/website/github.global.ssl.fastly.net#ipinfo"
WEBSITE_2 = "http://github.com.ipaddress.com/#ipinfo"
HOSTS_FILE_PATH = "C:\\Windows\\System32\\drivers\\etc\\hosts"


#topic body > div.resp.main > main > section:nth-child(4) > table > tbody >
def get_ip1():
    r = requests.get(WEBSITE_1, verify=False)
    soup = BeautifulSoup(r.text,'html.parser')
    return soup.select('tr:nth-child(3) > td > ul > li')[0].text


# topic body > div.resp.main > main > section:nth-child(6) > table > tbody 
def get_ip2():
    r = requests.get(WEBSITE_2, verify=False)
    soup = BeautifulSoup(r.text,'html.parser')
    return soup.select('tr:nth-child(7) > td > ul > li')[0].text


def edit_hosts(ip1, ip2):
    file = open(HOSTS_FILE_PATH, 'r')
    contents = file.readlines()
    new_contents = contents[:-2]
    file.close()
    file = open(HOSTS_FILE_PATH, "w")
    new_contents.append(ip1+" github.global.ssl.fastly.net\n")
    new_contents.append(ip2+" github.com")
    file.writelines(new_contents)
    file.close()

if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()
    ip1 = get_ip1()
    print("ip1("+WEBSITE_1+"):"+str(ip1))
    ip2 = get_ip2()
    print("ip2("+WEBSITE_2+"):"+str(ip2))
    edit_hosts(ip1, ip2)
    print("Hosts file updated!")
    os.system("ipconfig /flushdns")
    print("done")
    print("按任意键返回...")
    msvcrt.getwche()
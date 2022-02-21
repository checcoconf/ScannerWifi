import pyfiglet
import scapy.all as scapy
import re

titolo = pyfiglet.figlet_format("Scanner WiFi")
print(titolo)

ipRegex = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
ipAddRange = input ("Inserisci un indirizzo ip valido: ")

if ipRegex.search(ipaddRange):
    print(f"L'indirzzo ip: {ipAddRange} è valido!")

risultato = scapy.arping(ipAddRange)
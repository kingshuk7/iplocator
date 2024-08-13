#!/usr/bin/env python3
import requests
import socket
import ipaddress
from prettytable import PrettyTable

# Function to validate the IP address
def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Get IP address input from the user
ip = input("Enter the IP address: ")

# Check if the IP address is valid
if not is_valid_ip(ip):
    print("\nInvalid IP address. Please enter a valid IPv4 or IPv6 address.")
else:
    # Get full geolocation data
    geo_response = requests.get(f'https://ipinfo.io/{ip}/json')
    geo_data = geo_response.json()

    # Create a table for the geolocation data
    table = PrettyTable()
    table.field_names = ["Field", "Value"]

    # Set alignment to left for all columns
    table.align["Field"] = "l"
    table.align["Value"] = "l"

    # Add rows to the table
    table.add_row(["IP", geo_data.get('ip', 'N/A')])
    table.add_row(["Hostname", geo_data.get('hostname', 'N/A')])
    table.add_row(["City", geo_data.get('city', 'N/A')])
    table.add_row(["Region", geo_data.get('region', 'N/A')])
    table.add_row(["Country", geo_data.get('country', 'N/A')])
    table.add_row(["Location (Lat, Long)", geo_data.get('loc', 'N/A')])
    table.add_row(["ASN & Organization", geo_data.get('org', 'N/A')])
    table.add_row(["Postal Code", geo_data.get('postal', 'N/A')])
    table.add_row(["Timezone", geo_data.get('timezone', 'N/A')])

    # Print the table
    print("\nGeolocation Data:")
    print(table)

    # PTR (Reverse DNS Lookup) using socket
    try:
        ptr_data = socket.gethostbyaddr(ip)
        print("\nPTR Data (Host name):", ptr_data[0])
    except socket.herror:
        print("\nPTR Data: Could not find PTR record for this IP.")

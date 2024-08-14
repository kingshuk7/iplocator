# iplocator
IP locator is a Python script to get IP geolocation data.

## Usage
Install `requests`, `sockets`, `ipaddress` and `prettytable` Python module using below-mentioned command if they are not installed already.
```bash
pip3 install -r requirements.txt 
```
Run the script
```bash
cd ~/
git clone https://github.com/kingshuk7/iplocator.git
cd iplocator
python3 iplocator.py
```
The script will ask the user to enter an IP address and give you the results in below-mentioned format. If an invalid IP address is entered, the script will ask the user to input a valid IP.
```
Enter the IP address: 8.8.8.8

Geolocation Data:
+----------------------+---------------------+
| Field                | Value               |
+----------------------+---------------------+
| IP                   | 8.8.8.8             |
| Hostname             | dns.google          |
| City                 | Mountain View       |
| Region               | California          |
| Country              | US                  |
| Location (Lat, Long) | 37.4056,-122.0775   |
| ASN & Organization   | AS15169 Google LLC  |
| Postal Code          | 94043               |
| Timezone             | America/Los_Angeles |
+----------------------+---------------------+

PTR Data (Host name): dns.google
```


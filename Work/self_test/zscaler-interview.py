# Given a list of tls endpoints hostname:port combination in a file, write a script to verify and report the following

#1) valid certificate 
#2) expiry

#If the endpoint is a valid tls endpoint print the following if the certificate expires in the next 10 days
#1) certifcate CN
#2) expiry date
#3) serial number

# if the endpoint is not a valid endpoint print the following
# hostname:port 

# input 
# google.com:443
# yahoo.com:443
# random.none:8443

import ssl
import socket
import OpenSSL
from datetime import datetime

answer(filename):
    # Read the list of endpoints from a file
    with open(filename) as f:
        endpoints = [line.strip() for line in f]

    # Verify the certificate and report if it's valid or if it will expire in the next 10 days
    for endpoint in endpoints:
        hostname, port = endpoint.split(":")
        try:
            context = ssl.create_default_context()
            with socket.create_connection((hostname, int(port))) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert()
                    expires_on = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                    days_left = (expires_on - datetime.datetime.now()).days
                    if days_left <= 10:
                        print(f"Certificate CN: {cert['subject'][0][0][1]}")
                        print(f"Expiry date: {expires_on}")
                        print(f"Serial number: {cert['serialNumber']}")
        except (ssl.SSLError, socket.gaierror):
            print(f"{hostname}:{port} is not a valid endpoint")

def endponintcheck(urls):
        for i in urls:
            i = i.split(':')
            url = i[0]
            port = i[1]
            addr = url, port
            cert = ssl.get_server_certificate(addr)
            #return cert
            #print(url,port)
            x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
            bytes=x509.get_notAfter()
            print(bytes)
            timestamp = bytes.decode('utf-8')
            end_date = datetime.now() #+ datetime.timedelta(days=10)
            formated = datetime.strptime(timestamp, '%Y%m%d%H%M%S%z')
            
            if formated >= end_date:
            print(formated,end_date)
urls = [
    'google.com:443',
    'yahoo.com:443',
    'random.none:8443'
    ]
            
endponintcheck(urls)      
import ssl
import socket
import datetime



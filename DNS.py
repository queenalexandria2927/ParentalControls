import socket
import sys
import subprocess
import pkg_resources
from dnslib import DNSRecord, QTYPE, RR
from dnslib.dns import DNSHeader, DNSQuestion, DNSAnswer
import socketserver

# Function to check if a package is installed and install it if not
def check_and_install_packages(packages):
    for package in packages:
        try:
            pkg_resources.get_distribution(package)
            print(f"Package '{package}' is already installed.")
        except pkg_resources.DistributionNotFound:
            print(f"Package '{package}' not found. Installing it now...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = [
    "dnslib",   # This is the main package for DNS handling
    # You can add any other required packages here as needed
    # "requests", "flask", etc.
]

# Check and install all required packages
check_and_install_packages(required_packages)

# Define a basic DNS handler class
class DNSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Receive data from the client (DNS query)
        data = self.request[0]
        socket = self.request[1]

        # Parse the DNS query
        dns_query = DNSRecord.parse(data)

        # Display the received query (for debugging)
        print(f"Received query for domain: {dns_query.q.qname}")

        # Check for the domain being queried and return a predefined IP
        response = self.generate_dns_response(dns_query)

        # Send back the response
        socket.sendto(response.pack(), self.client_address)

    def generate_dns_response(self, dns_query):
        # DNS Header
        dns_header = DNSHeader(id=dns_query.header.id, qr=1, aa=1, ra=1)

        # DNS Question (we only respond to the first question in the query)
        question = dns_query.q

        # Predefined domains and their corresponding IP addresses
        domain_to_ip = {
            "example.com.": "93.184.216.34",
            "test.com.": "192.0.2.1"
        }

        # Default response if domain not found
        ip_address = "0.0.0.0"
        
        # Check if the queried domain exists in our dictionary
        if str(question.qname) in domain_to_ip:
            ip_address = domain_to_ip[str(question.qname)]

        # DNS Answer section (return the IP address)
        answer = RR(
            question.qname, QTYPE.A, rdata=socket.inet_aton(ip_address), ttl=60
        )

        # Build the full response
        dns_response = dns_header / question / answer

        return dns_response

# Set up the DNS server to listen on port 53
def run_dns_server():
    print("Starting DNS server on port 53...")
    server = socketserver.UDPServer(('0.0.0.0', 53), DNSHandler)
    server.serve_forever()

if __name__ == "__main__":
    try:
        run_dns_server()
    except Exception as e:
        print(f"Error occurred while starting DNS server: {e}")
        sys.exit(1)

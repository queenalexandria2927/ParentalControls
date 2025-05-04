# server_main.py

import subprocess
import time
import sys
import platform
import os

# Check if the user is on macOS
def check_os():
    if platform.system() == "Darwin":
        print("Warning: It is not recommended to run this on a Mac. Proceed at your own risk.")
        override = input("Do you want to override this warning and continue? (yes/no): ").strip().lower()
        if override != "yes":
            print("Exiting the program.")
            sys.exit(0)

# Check if it's the first time running the software
def check_first_run():
    if not os.path.exists("first_run.txt"):
        return True
    return False

# Mark the first run as completed
def mark_first_run():
    with open("first_run.txt", "w") as file:
        file.write("This file marks the first run of PhoenixRoseMedia Parental Controls.")

# Function to display error message
def display_error_message():
    print("\nUh-oh, seems like we ran into a problem. For support, visit https://help.phoenixrosemedia.org")

# Function to check if a file exists
def check_file_exists(filename):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        display_error_message()
        sys.exit(1)

# Run services and handle errors
def run_services():
    try:
        # Check if the necessary files exist
        check_file_exists("DNS.py")
        check_file_exists("web_server.py")

        # Start DNS Manager and Core Services in the background
        print("Starting DNS Manager and Core Services...")
        time.sleep(5)
        subprocess.Popen(["python3", "DNS.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("DNS core services started.")

        # Start web server in the background
        print("Starting web server...")
        time.sleep(5)
        subprocess.Popen(["python3", "web_server.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Web server started.")
        
        # Success message after services are loaded
        print("\n--------------------------------------------")
        print("Success! All services loaded successfully.")
        print("--------------------------------------------")
    
    except Exception as e:
        print("Error: ", e)
        display_error_message()
        sys.exit(1)  # Exit if there's an error starting the services

if __name__ == "__main__":
    try:
        check_os()  # Check the OS and handle for macOS

        # Display copyright information for PhoenixRoseMedia
        print("\n--------------------------------------------")
        print("Copyright © 2025 PhoenixRoseMedia. All Rights Reserved.")
        print("Made with love in York County, PA.")
        print("Made by Alexandria Myers.")
        print("This software is provided as-is, with no warranty.")
        print("--------------------------------------------\n")

        # Check for first-time run
        if check_first_run():
            print("\n--------------------------------------------")
            print("Welcome to PhoenixRoseMedia Parental Controls.")
            print("This is a network-wide Parental Controls program.")
            print("Please make sure you go into your router and computers and set your DNS Server to:")
            print("Find your computer's IP address, and set your DNS to that IP.")
            print("Then, go to the following address in your web browser:")
            print("http://<Your Computer's IP>:80")
            print("Username: admin")
            print("Password: Admin")
            print("--------------------------------------------\n")
            mark_first_run()  # Mark the first run as complete

        # Run DNS Manager and Web Server services
        run_services()

        # Keep console open but allow the user to close the window
        print("\nIf you want to close this window, feel free to do so. The services will continue running in the background.")
        input("Press Enter to exit... (This will only close the console window.)")

    except Exception as e:
        print("Critical error: ", e)
        display_error_message()
        sys.exit(1)

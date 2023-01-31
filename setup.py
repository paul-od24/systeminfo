import os
import platform
import psutil
import time

def cpu_strength_score():
    # Start the timer
    start = time.time()

    # Perform a simple numerical task
    for i in range(1000000):
        x = i * i

    # Stop the timer
    end = time.time()

    # Calculate and return the CPU strength score
    return (end - start)

def main():
    # Get the name of the machine
    hostname = platform.node()

    # Get the operating system name and version
    os_name = platform.system()
    os_version = platform.release()

    # Get the number of CPU's and amount of memory
    num_cpus = psutil.cpu_count()
    memory = psutil.virtual_memory().total / (1024.0 ** 3)

    # Get the IP address of the machine
    ip_address = psutil.net_if_addrs()['Wi-Fi'][0].address

    # Get the CPU strength score
    cpu_score = cpu_strength_score()

    # Print the information
    print("Hostname:", hostname)
    print("Operating System:", os_name, os_version)
    print("Number of CPU's:", num_cpus)
    print("Amount of Memory (GB):", memory)
    print("IP Address:", ip_address)
    print("CPU Strength Score:", cpu_score)

if __name__ == '__main__':
    main()
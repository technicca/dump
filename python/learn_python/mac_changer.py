import os
import subprocess
import random

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        # Error occurred, print error message
        print(stderr.decode())
        return None
    return stdout.decode()

def get_interfaces():
    raw_output = run_command(['ip', '-o', 'link', 'show'])
    if raw_output is None:
        return []  # Return empty list if error occurred
    interfaces = [line.split()[1].replace(':', '') for line in raw_output.splitlines()]
    return interfaces

def generate_random_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def change_mac(interface):
    new_mac = generate_random_mac()
    print(f"Changing MAC address of {interface} to {new_mac}")
    run_command(['ip', 'link', 'set', interface, 'down'])
    run_command(['ip', 'link', 'set', interface, 'address', new_mac])
    run_command(['ip', 'link', 'set', interface, 'up'])

def main():
    interfaces = get_interfaces()
    print(f"Found interfaces: {', '.join(interfaces)}")
    for interface in interfaces:
        if interface != 'lo':
            change_mac(interface)

if __name__ == "__main__":
    main()

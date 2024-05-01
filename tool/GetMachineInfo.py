#############################################################################
#   Author: Nguyen Quoc Truong                                              #
#   Developer: T&T Stdudio                                                  #
#   Description: Get mac address and host name of host device.              #
#   Usage: Included and used in GenLicenseKey.py                            #
#############################################################################

import platform
import subprocess
import psutil
import uuid
import re

def get_mac_address():
    interfaces = psutil.net_if_addrs()
    for interface, addrs in interfaces.items():
        # Skip loopback and virtual interfaces
        if interface.startswith('lo') or interface.startswith('virtual'):
            continue

        # Return the MAC address of the first non-empty MAC address
        for addr in addrs:
            if addr.family == psutil.AF_LINK and addr.address:
                return addr.address.upper().replace('-', ':')
    return None

def get_host_name():
    system = platform.system()
    
    if system == "Windows":
        return platform.node()
    elif system == "Linux":
        try:
            # Read the serial number from the /proc/cpuinfo file on Linux
            with open("/proc/cpuinfo", "r") as f:
                for line in f:
                    if "Serial" in line:
                        return line.split(":")[1].strip()
        except FileNotFoundError:
            pass

    # For other platforms or if serial number cannot be obtained, return None
    return None

def get_bios_serial_number():
    try:
        result = subprocess.run(["wmic", "bios", "get", "serialnumber"], capture_output=True, text=True)
        serial_number = result.stdout.strip()
        return serial_number
    except Exception as e:
        print(f"Error retrieving BIOS serial number: {e}")
        return None

def get_machine_product_id():    
    if platform.system() == "Windows":
        try:
            import winreg

            key_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
            value_name = "ProductId"

            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
                product_id, _ = winreg.QueryValueEx(key, value_name)

            return product_id
        except Exception as e:
            return f"Error: {e}"

    return "Not a Windows system"

if __name__ == "__main__":
    pass
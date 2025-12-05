#!/usr/bin/env python3
"""
Firmware Check Script
Collects system firmware/BIOS information and outputs to file
"""

import subprocess
import platform
import datetime
import os

def get_firmware_info():
    """Gather firmware information based on OS"""
    results = []
    results.append(f"Firmware Check Report")
    results.append(f"Generated: {datetime.datetime.now()}")
    results.append(f"Hostname: {platform.node()}")
    results.append(f"OS: {platform.system()} {platform.release()}")
    results.append("=" * 50)
    
    system = platform.system()
    
    if system == "Windows":
        # BIOS info via WMIC
        commands = {
            "BIOS Info": "wmic bios get manufacturer,name,version,smbiosbiosversion,releasedate /format:list",
            "Baseboard": "wmic baseboard get manufacturer,product,version /format:list",
            "System": "wmic computersystem get manufacturer,model,systemtype /format:list"
        }
        
        for label, cmd in commands.items():
            results.append(f"\n{label}:")
            results.append("-" * 30)
            try:
                output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                # Filter empty lines
                lines = [line.strip() for line in output.stdout.splitlines() if line.strip()]
                results.extend(lines)
            except Exception as e:
                results.append(f"Error: {e}")
    
    elif system == "Linux":
        # DMI decode requires root for full info
        commands = {
            "BIOS Info": "sudo dmidecode -t bios 2>/dev/null || cat /sys/class/dmi/id/bios_*",
            "System Info": "sudo dmidecode -t system 2>/dev/null || cat /sys/class/dmi/id/product_*",
            "Board Info": "sudo dmidecode -t baseboard 2>/dev/null || cat /sys/class/dmi/id/board_*"
        }
        
        for label, cmd in commands.items():
            results.append(f"\n{label}:")
            results.append("-" * 30)
            try:
                output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                results.append(output.stdout.strip() if output.stdout else "No data (may need root)")
            except Exception as e:
                results.append(f"Error: {e}")
        
        # Also try reading sysfs directly (doesn't need root)
        results.append("\nSysfs DMI Data:")
        results.append("-" * 30)
        dmi_path = "/sys/class/dmi/id"
        if os.path.exists(dmi_path):
            for item in ["bios_vendor", "bios_version", "bios_date", "board_vendor", "board_name"]:
                filepath = os.path.join(dmi_path, item)
                try:
                    with open(filepath, 'r') as f:
                        results.append(f"{item}: {f.read().strip()}")
                except:
                    pass
    
    elif system == "Darwin":  # macOS
        results.append("\nSystem Firmware:")
        results.append("-" * 30)
        try:
            output = subprocess.run(
                ["system_profiler", "SPHardwareDataType"],
                capture_output=True, text=True
            )
            results.append(output.stdout.strip())
        except Exception as e:
            results.append(f"Error: {e}")
    
    return "\n".join(results)


def main():
    output_file = "firmware_report.txt"
    
    print("Running firmware check...")
    report = get_firmware_info()
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write(report)
    
    print(f"\nReport saved to: {output_file}")
    print("\n" + "=" * 50)
    print(report)


if __name__ == "__main__":
    main()

import platform
import psutil
import socket

def get_system_info():
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor()
    }
    return system_info

def get_cpu_info():
    cpu_info = {
        "Physical Cores": psutil.cpu_count(logical=False),
        "Total Cores": psutil.cpu_count(logical=True),
        "Max Frequency": f"{psutil.cpu_freq().max:.2f} MHz",
        "Current Frequency": f"{psutil.cpu_freq().current:.2f} MHz",
        "CPU Usage": f"{psutil.cpu_percent(interval=1)}%"
    }
    return cpu_info

def get_memory_info():
    memory = psutil.virtual_memory()
    memory_info = {
        "Total Memory": f"{memory.total / (1024 ** 3):.2f} GB",
        "Available Memory": f"{memory.available / (1024 ** 3):.2f} GB",
        "Used Memory": f"{memory.used / (1024 ** 3):.2f} GB",
        "Memory Usage": f"{memory.percent}%"
    }
    return memory_info

def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_info = {}
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info[partition.device] = {
            "Mount Point": partition.mountpoint,
            "Total Size": f"{usage.total / (1024 ** 3):.2f} GB",
            "Used": f"{usage.used / (1024 ** 3):.2f} GB",
            "Free": f"{usage.free / (1024 ** 3):.2f} GB",
            "Usage": f"{usage.percent}%"
        }
    return disk_info

def get_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    network_info = {
        "Hostname": hostname,
        "IP Address": ip_address
    }
    return network_info

if __name__ == "__main__":
    print("System Information:", get_system_info())
    print("CPU Information:", get_cpu_info())
    print("Memory Information:", get_memory_info())
    print("Disk Information:", get_disk_info())
    print("Network Information:", get_network_info())
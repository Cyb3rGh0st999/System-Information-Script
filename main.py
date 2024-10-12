import platform
import os

# get_system_info function
def get_system_info():
    # Get basic system information
    print("Operating System:", platform.system())
    print("OS Version:", platform.version())
    print("Architecture:", platform.machine())
    print("Processor:", platform.processor())

    # Get CPU cores (logical cores using os)
    try:
        cpu_cores = os.cpu_count()
        print("CPU Cores:", cpu_cores if cpu_cores is not None else "Unavailable")
    except Exception as e:
        print("CPU Cores: Unable to retrieve information due to error:", str(e))

    # Get Total RAM using os.sysconf
    try:
        total_ram = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024**3)  # in GB
        print(f"Total RAM: {round(total_ram, 2)} GB")
    except Exception as e:
        print("Total RAM: Unable to retrieve information due to error:", str(e))

    # Get disk usage using os.statvfs
    try:
        statvfs = os.statvfs('/')
        total_disk_space = statvfs.f_frsize * statvfs.f_blocks / (1024**3)  # in GB
        available_disk_space = statvfs.f_frsize * statvfs.f_bfree / (1024**3)  # in GB
        print(f"Total Disk Space: {round(total_disk_space, 2)} GB")
        print(f"Available Disk Space: {round(available_disk_space, 2)} GB")
    except Exception as e:
        print("Disk Space: Unable to retrieve information due to error:", str(e))

if __name__ == "__main__":
    get_system_info()



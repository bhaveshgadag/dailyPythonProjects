# (1) The program should make use of the psutil library to store various computer metrics in a CSV file.
# (2) When the script is executed for the first time it creates a CSV file, adds a header (i.e., timestamp,
#     cpu_usage, memory_total_mb, memory_used_mb, disk_total_gb, disk_used_gb), measures the metrics, 
#     and adds those metrics as a row of data in the CSV.
# (3) When the script is executed for the second time, it adds a new row with data in the existing CSV file.
# (4) Any time the script is executed, a new row with data is stored.
# (5) Optionally, upload the script to a service such as PythonAnywhere.com to schedule it for execution 
#     at a certain time every day.

import psutil

# CPU Usage
print("CPU Usage")
print(psutil.cpu_percent(interval=1))

# RAM total & used
print("RAM")
mem = psutil.virtual_memory()
print(mem[0]/(1024 * 1024))
print(mem[3]/(1024 * 1024))

# disk usage
print("Disk")
disk = psutil.disk_usage('/')
print(disk[0]/(1024 * 1024 * 1024))
print(disk[1]/(1024 * 1024 * 1024))
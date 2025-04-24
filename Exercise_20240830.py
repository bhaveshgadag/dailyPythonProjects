# (1) The program should make use of the psutil library to store various computer metrics in a CSV file.
# (2) When the script is executed for the first time it creates a CSV file, adds a header (i.e., timestamp,
#     cpu_usage, memory_total_mb, memory_used_mb, disk_total_gb, disk_used_gb), measures the metrics, 
#     and adds those metrics as a row of data in the CSV.
# (3) When the script is executed for the second time, it adds a new row with data in the existing CSV file.
# (4) Any time the script is executed, a new row with data is stored.
# (5) Optionally, upload the script to a service such as PythonAnywhere.com to schedule it for execution 
#     at a certain time every day.

import psutil, time

system_metrics = []
# CPU Usage
system_metrics.append(psutil.cpu_percent(interval=1))

# RAM total & used
mem = psutil.virtual_memory()
system_metrics.append(mem[0]/(1024 * 1024))
system_metrics.append(mem[3]/(1024 * 1024))

# disk usage
disk = psutil.disk_usage('/')
system_metrics.append(disk[0]/(1024 * 1024 * 1024))
system_metrics.append(disk[1]/(1024 * 1024 * 1024))

with open('System_Metrics.csv', 'a+') as csvfile:

    header = 'timestamp,cpu_usage,memory_total_mb,memory_used_mb,disk_total_gb,disk_used_gb'
    # Check if header is present
    csvfile.seek(0)
    if header != csvfile.readline().strip():
        csvfile.seek(0)
        csvfile.write(f"{header}\n")
    
    # Change stream position to end of file
    csvfile.seek(0, 2)
    line = time.strftime("%Y-%m-%d %H:%M:%S")
    for metric in system_metrics:
        line = f"{line},{metric}"

    csvfile.write(f"{line}\n")
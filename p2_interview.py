import psutil
import logging

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
LOG_FILE = "/var/log/system_health.log"

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.info(f"CPU usage is above threshold: {cpu_usage}%")
        print(f"CPU usage is above threshold: {cpu_usage}%")

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.info(f"Memory usage is above threshold: {memory_usage}%")
        print(f"Memory usage is above threshold: {memory_usage}%")

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.info(f"Disk usage is above threshold: {disk_usage}%")
        print(f"Disk usage is above threshold: {disk_usage}%")

def check_running_processes():
    process_count = len(psutil.pids())
    logging.info(f"Number of running processes: {process_count}")
    print(f"Number of running processes: {process_count}")

def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
    logging.info("System health check completed.")
    print("System health check completed.")

if __name__ == "__main__":
    main()

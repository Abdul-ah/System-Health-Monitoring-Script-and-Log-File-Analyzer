import re
from collections import Counter

LOG_FILE = "/var/log/nginx/access.log"
REPORT_FILE = "/var/log/nginx/log_report.txt"

def read_log_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def analyze_log(log_lines):
    pattern_404 = re.compile(r' 404 ')
    pattern_request = re.compile(r'\"(?:GET|POST) (.*?) HTTP/1.[01]\"')
    pattern_ip = re.compile(r'(\d+\.\d+\.\d+\.\d+)')

    num_404 = 0
    request_paths = []
    ip_addresses = []

    for line in log_lines:
        if pattern_404.search(line):
            num_404 += 1
        request_match = pattern_request.search(line)
        if request_match:
            request_paths.append(request_match.group(1))
        ip_match = pattern_ip.search(line)
        if ip_match:
            ip_addresses.append(ip_match.group(1))

    most_requested = Counter(request_paths).most_common(10)
    most_requests_by_ip = Counter(ip_addresses).most_common(10)

    return num_404, most_requested, most_requests_by_ip

def generate_report(num_404, most_requested, most_requests_by_ip, report_file):
    with open(report_file, 'w') as file:
        file.write("Log Analysis Report\n")
        file.write("===================\n\n")
        file.write(f"Number of 404 errors: {num_404}\n\n")
        file.write("Most Requested Pages:\n")
        for path, count in most_requested:
            file.write(f"{path}: {count} requests\n")
        file.write("\nIP Addresses with the Most Requests:\n")
        for ip, count in most_requests_by_ip:
            file.write(f"{ip}: {count} requests\n")

def main():
    log_lines = read_log_file(LOG_FILE)
    num_404, most_requested, most_requests_by_ip = analyze_log(log_lines)
    generate_report(num_404, most_requested, most_requests_by_ip, REPORT_FILE)
    print(f"Log analysis report generated at {REPORT_FILE}")

if __name__ == "__main__":
    main()

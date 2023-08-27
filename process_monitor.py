import argparse
import csv
import sys
import time

import psutil


def monitor_process(process_name, duration, interval):
    process = None
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if process_name.lower() in proc.info['name'].lower():
            process = psutil.Process(proc.info['pid'])
            break

    if not process:
        print(f"No process with name '{process_name}' found.")
        return

    metrics = []
    end_time = time.time() + duration
    while time.time() < end_time:
        cpu_percent = process.cpu_percent(interval=interval)
        memory_info = process.memory_info()
        num_handles = len(process.open_files())

        metrics.append([cpu_percent, memory_info.rss, num_handles])

    return metrics


def create_csv_report(metrics):
    avg_cpu = sum([entry[0] for entry in metrics]) / len(metrics)
    avg_memory = sum([entry[1] for entry in metrics]) / len(metrics)
    avg_handles = sum([entry[2] for entry in metrics]) / len(metrics)

    with open('process_metrics.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(
            ['Average CPU (%)', 'Average Memory (bytes)', 'Average Handles'])
        csvwriter.writerow([avg_cpu, avg_memory, avg_handles])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process Resources Monitoring App')
    parser.add_argument('--process_name', type=str, help='Name of the process to monitor')
    parser.add_argument('--duration', type=int, help='Duration of monitoring in seconds')
    parser.add_argument('--interval', type=int, default=5, help='Sampling interval in seconds')
    args = parser.parse_args()

    if args.duration is None or args.duration <= 0:
        print("Duration must be provided as a positive integer.")
        sys.exit(1)

    if not args.process_name:
        print("Process name must be provided.")
        sys.exit(1)

    monitored_metrics = monitor_process(
        process_name=args.process_name,
        duration=args.duration,
        interval=args.interval
    )

    if monitored_metrics:
        create_csv_report(monitored_metrics)
        print("Monitoring complete. CSV report generated.")

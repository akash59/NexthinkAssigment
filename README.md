
# Process Resources Monitoring App

This is a Python script that monitors the resource usage (CPU, memory, and file handles) of a specified process over a specified duration. It utilizes the `psutil` library to gather information about the target process.

## Prerequisites

Before running the script, ensure you have Python 3.x installed on your system. You can install the required dependencies using the following command:

```bash
pip install psutil
```

## Usage

To run the script, use the following command:

```bash
python monitor_process.py --process_name <p_name> --duration <duration> [--interval <interval>]
```

## Script Overview

The script comprises two main functions: `monitor_process` and `create_csv_report`.

### `monitor_process(process_name, duration, interval)`

This function monitors the specified process. It locates the target process using the `psutil` library and collects CPU usage, memory info, and open file handle count at specified intervals.

**Parameters:**
- `process_name` (str): Name of the process to monitor.
- `duration` (int): Monitoring duration in seconds.
- `interval` (int): Sampling interval in seconds.

**Returns:**
- `metrics` (list): List of lists with metrics (CPU %, memory usage, open handles).

### `create_csv_report(metrics)`

This function generates a CSV report from collected metrics.

**Parameters:**
- `metrics` (list): List of lists containing collected metrics.

**Returns:**
- None

## Example Usage

To monitor a process named "my_process" for 120 seconds with a 10-second interval, use the following command:

```bash
python monitor_process.py --process_name my_process --duration 120 --interval 10
```

## Notes

- Ensure that you have the necessary permissions to monitor the specified process.
- The CSV report will be generated in the same directory as the script with the name `process_metrics.csv`.










# Process Resources Monitoring App

This is a Python script that monitors the resource usage (CPU, memory, and file handles) of a specified process over a specified duration. It utilizes the `psutil` library to gather information about the target process.

## Prerequisites

Before running the script, ensure you have Python 3.x installed on your system. You can install the required dependencies using the following command:

```bash
pip install psutil
```

## Usage

To run the script, use the following command:

```bash
python monitor_process.py --process_name <p_name> --duration <duration> [--interval <interval>]
```

## Script Overview

The script comprises two main functions: `monitor_process` and `create_csv_report`.

### `monitor_process(process_name, duration, interval)`

This function monitors the specified process. It locates the target process using the `psutil` library and collects CPU usage, memory info, and open file handle count at specified intervals.

**Parameters:**
- `process_name` (str): Name of the process to monitor.
- `duration` (int): Monitoring duration in seconds.
- `interval` (int): Sampling interval in seconds.

**Returns:**
- `metrics` (list): List of lists with metrics (CPU %, memory usage, open handles).

### `create_csv_report(metrics)`

This function generates a CSV report from collected metrics.

**Parameters:**
- `metrics` (list): List of lists containing collected metrics.

**Returns:**
- None

## Example Usage

To monitor a process named "my_process" for 120 seconds with a 10-second interval, use the following command:

```bash
python monitor_process.py --process_name my_process --duration 120 --interval 10
```

## Notes

- Ensure that you have the necessary permissions to monitor the specified process.
- The CSV report will be generated in the same directory as the script with the name `process_metrics.csv`.

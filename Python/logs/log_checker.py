# log_checker.py

def read_log(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


def count_log_levels(lines):
    levels = {'INFO': 0, 'WARNING': 0, 'ERROR': 0, 'DEBUG': 0, 'CRITICAL': 0}
    for line in lines:
        for level in levels:
            if level in line:
                levels[level] += 1
    return levels


def filter_logs(lines, level):
    return [line for line in lines if level in line]


def display_summary(file_path):
    print(f"Reading log from: {file_path}")
    lines = read_log(file_path)
    print(f"Total lines: {len(lines)}")
    level_counts = count_log_levels(lines)
    for level, count in level_counts.items():
        print(f"{level}: {count}")


def display_filtered(file_path, level):
    lines = read_log(file_path)
    filtered = filter_logs(lines, level)
    print(f"\n--- {level} Logs ---")
    for line in filtered:
        print(line.strip())


# Only runs if this file is executed directly
if __name__ == "__main__":
    log_file = "app.log"  # Change this to your log file path
    display_summary(log_file)
    display_filtered(log_file, "ERROR")  # Change "ERROR" to filter by other levels

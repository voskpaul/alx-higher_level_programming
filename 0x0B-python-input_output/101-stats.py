#!/usr/bin/python3
import sys

# Initialize variables to store the metrics
total_size = 0
status_code_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

try:
    line_count = 0
    for line in sys.stdin:
        # Split the input line into parts
        parts = line.split()
        if len(parts) >= 9:
            # Extract the status code and file size
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update the total file size
            total_size += file_size

            # Update the status code counts
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print("File size: {}".format(total_size))
                for code in sorted(status_code_counts.keys()):
                    count = status_code_counts[code]
                    if count > 0:
                        print("{}: {}".format(code, count))
except KeyboardInterrupt:
    pass

finally:
    # Print the final statistics
    print("File size: {}".format(total_size))
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        if count > 0:
            print("{}: {}".format(code, count))


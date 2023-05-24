import os
import sys
import re
import csv
import time

def convert_files_to_csv(folder_path, regex_pattern, csv_filename):

    # Variables to track total size of files and time spent
    total_size = 0
    total_rows = 0
    start_time = time.time()

    # Create a CSV file and open it in write mode
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row
        csv_writer.writerow(['Timestamp', 'Process', 'OrganizationId', 'Thread', 'Category','UserId', 'Level', 'ReqId', 'ActivityId', 'Details'])
        
        # Iterate through all files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Check if the path is a file
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                total_size += file_size
            
                with open(file_path, 'r', encoding="utf-8") as file:
                    try:
                        content = file.read()
                    except:
                        print("Error reading" + file_path)

                    # Find all matches in the file
                    matches = regex_pattern.findall(content)

                    # Write match groups to the CSV file
                    for match in matches:
                        csv_writer.writerow(list(match))
                        total_rows += 1
                        
    end_time = time.time()
    total_time = end_time - start_time

    print(f"Conversion completed. Results saved to {csv_filename}.")
    print(f"Total files processed: {len(os.listdir(folder_path))}")
    print(f"Total size of files processed: {total_size} bytes")
    print(f"Found {total_rows} rows.")
    print(f"Time spent: {total_time:.2f} seconds")

if __name__ == '__main__':
    # Check if the folder path is provided as an argument
    if len(sys.argv) < 2:
        print("Please provide the folder path as an argument.")
        sys.exit(1)

    # Folder path containing the files to be converted
    folder_path = sys.argv[1]

# Regex pattern to extract desired data with groups
regex_pattern = re.compile(r'^\[(.*)\] Process:(.*?)\s\|Organization:(.*?)\s\|Thread:\s*(\d*) \|Category: ([a-zA-Z\.]*?) \|User: (.*?) \|Level: (.*?) \|ReqId: (.*?) \|ActivityId: (.*?) \| (.*)$', re.M)

# CSV filename to save the results
csv_filename = 'output.csv'

# Call the function to convert files to CSV
convert_files_to_csv(folder_path, regex_pattern, csv_filename)

import os
import re
import csv

def convert_files_to_csv(folder_path, regex_pattern, csv_filename):
    # Get the number of match groups in the regex pattern
    num_groups = regex_pattern.groups

    # Create a CSV file and open it in write mode
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row
        csv_writer.writerow(['Timestamp', 'Process', 'OrganizationId', 'Thread', 'Category','UserId', "Level', ReqId', 'ActivityId', 'Details'])
        
        # Iterate through all files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Check if the path is a file
            if os.path.isfile(file_path):
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

    print(f"Conversion completed. Results saved to {csv_filename}.")


# Folder path containing the files to be converted
folder_path = 'C:/TEMP/tracelogs_NR2_2023_05_23'

# Regex pattern to extract desired data with groups
regex_pattern = re.compile(r'^\[(.*)\] Process:(.*?)\s\|Organization:(.*?)\s\|Thread:\s*(\d*) \|Category: ([a-zA-Z\.]*?) \|User: (.*?) \|Level: (.*?) \|ReqId: (.*?) \|ActivityId: (.*?) \| (.*)$', re.M)

# CSV filename to save the results
csv_filename = 'output.csv'

# Call the function to convert files to CSV
convert_files_to_csv(folder_path, regex_pattern, csv_filename)

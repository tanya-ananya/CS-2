import os
import csv

class FileProcessor:
    
    @staticmethod
    def merge(file1_path, file2_path, result_path):
        try:
            with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(result_path, 'w') as result:
                result.write(file1.read())
                result.write("\n")
                result.write(file2.read())
        except Exception as e:
            print(f"An error occurred while merging files: {e}")

    @staticmethod
    def copy(file1_path, num_copies):
        try:
            with open(file1_path, 'r') as file:
                content = file.read()
                for i in range(1, num_copies + 1):
                    copy_path = f"{os.path.splitext(file1_path)[0]}_copy{i}{os.path.splitext(file1_path)[1]}"
                    with open(copy_path, 'w') as copy_file:
                        copy_file.write(content)
        except Exception as e:
            print(f"An error occurred while copying the file: {e}")

    @staticmethod
    def convert_to_csv(text_file_path, csv_file_path):
        try:
            with open(text_file_path, 'r') as text_file, open(csv_file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                for line in text_file:
                    writer.writerow([line.strip()])
        except Exception as e:
            print(f"An error occurred while converting to CSV: {e}")

    @staticmethod
    def file_statistics(file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                num_lines = len(lines)
                num_words = sum(len(line.split()) for line in lines)
                print(f"Number of lines: {num_lines}")
                print(f"Number of words: {num_words}")
        except Exception as e:
            print(f"An error occurred while getting file statistics: {e}")

FileProcessor.merge("text1.txt", "text2.txt", "result.txt")

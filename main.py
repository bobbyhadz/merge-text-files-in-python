# How to merge text files in Python

file_paths = ['file-1.txt', 'file-2.txt']

with open('output-file.txt', 'w', encoding='utf-8') as output_file:
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            for line in input_file:
                output_file.write(line)
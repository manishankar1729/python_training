import os

def is_text_file(file_path):
    return file_path.endswith('.txt')

def append_file_content(file_path, output_file):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            output_file.write(content + '\n')
            print(f"Appended: {file_path}")
    except Exception as e:
        print(f"Failed to read {file_path}: {e}")

def process_directory(input_dir, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if is_text_file(file_path):
                    append_file_content(file_path, output_file)

if __name__ == "__main__":
    input_directory = "C:\\Users\\satyamanishankar\\handson\\DAY1"
    output_file = "output.txt"
    process_directory(input_directory, output_file)
    print(f" text file contents have been written to {output_file}")

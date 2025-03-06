import os

def find_largest_file(directory):
    max_size = 0
    largest_file = None

    
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path)
            
            
            if file_size > max_size:
                max_size = file_size
                largest_file = file_path
    return largest_file, max_size


directory = "C:/Users/satyamanishankar/handson/pkg" 
file, size = find_largest_file(directory)
if file!=None:
    print(f"Largest file: {file} with size: {size} bytes")
else:
    print("No files found.")

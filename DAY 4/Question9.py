import os

def split_file(file_name,num_parts):
    if not os.path.isfile(file_name):
        print(f"{file_name} not found")
        return 
    file_size=os.path.getsize(file_name)
    part_size=file_size//num_parts
    remainder=file_size%num_parts
    
    with open(file_name,'rb') as file:
        for i in range(num_parts):
           part_filename = f"{file_name}_part{i+1}"
           with open(part_filename, 'wb') as part_file:
               current_part_size = part_size + (1 if i < remainder else 0)
               part_file.write(file.read(current_part_size))
               print(f"Created {part_filename} with size {current_part_size} bytes.") 
                
split_file('merged_output.txt', 3)
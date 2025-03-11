import os

file_list=["h1.txt","h2.txt","h3.txt"]  #trying giving the txt files in your dir
output="merged_output.txt"


with open(output,'w') as outfile:
    for file_name in file_list:
        
        try:
            with open(file_name,'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n')
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Skipping...")
        except Exception as e:
            print(f"An error occurred while processing '{file_name}': {e}")
print(f"All files have been concatenated into '{output}'.")
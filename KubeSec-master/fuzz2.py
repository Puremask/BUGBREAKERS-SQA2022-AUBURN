#Fuzzing Python Methods
import random
import os
import string
from scanner import getYAMLFiles

def fuzz_getYAMLFiles():
    # Generates a random path directory
    path_to_dir = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    os.makedirs(path_to_dir)
    print('='*100)
    print(f" Check forensics.log file: Fuzz YAMLFiles test is now completed.")
    print('='*100)

    # Generates random YAML files with random names in the temp directory
    random_files = random.randint(1, 10)
    for i in range(random_files):
        files_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        with open(os.path.join(path_to_dir, f"{files_name}.yaml"), 'w') as f:
            f.write('this is a fuzz test: yaml')
        with open(os.path.join(path_to_dir, f"{files_name}.yml"), 'w') as f:
            f.write('this is a fuzz test: yml')
        result = getYAMLFiles(path_to_dir)
        assert(os.path.join(path_to_dir, f"{files_name}.yaml"))       
	
if __name__=='__main__':
   fuzz_getYAMLFiles()
			 

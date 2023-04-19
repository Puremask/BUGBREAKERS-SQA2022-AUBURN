#Fuzzing Python Methods
import random
import os
import string
import constants
from scanner import getYAMLFiles
from scanner import checkIfValidKeyValue
from constants import VALID_KEY_STRING

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

def fuzz_checkIfValidKeyValue():
    # Generates random string.
    single_config_val = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
    result = checkIfValidKeyValue(single_config_val)

    # Checks boolean method.
    assert isinstance(result, bool)
    assert result == False

    # Generates random string to check with VALID_KEY_STRING
    flag2Ret = random.choice(constants.VALID_KEY_STRING)
    single_config_val = ''.join(random.choices(string.ascii_letters + string.digits, k=15)) + (f':      ')+ (flag2Ret)
    result = checkIfValidKeyValue(single_config_val)
    assert isinstance(result, bool)
    assert result == True
    print('='*100)
    print(f"Key value is valid: Fuzz ValidKeyValue test is now completed.")
    print(single_config_val)
    print('='*100)

if __name__=='__main__':
   #fuzz_getYAMLFiles()
   #fuzz_checkIfValidKeyValue()
			 

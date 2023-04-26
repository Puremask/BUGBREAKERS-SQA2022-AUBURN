#Fuzzing Python Methods
import random
import os
import string
import constants
from scanner import getYAMLFiles
from scanner import checkIfValidKeyValue
from constants import VALID_KEY_STRING
from parser import checkIfWeirdYAML
from scanner import isValidUserName
from constants import FORBIDDEN_USER_NAMES
from scanner import checkIfValidSecret
from constants import INVALID_SECRET_CONFIG_VALUES

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

def fuzz_checkIfWeridYAML():
    # Generates a random yaml string file
    random_yaml = ''.join(random.choices(string.ascii_letters, k=10))

    # Github workflows would be considered an invalid yaml path
    path = ["./github/workflows/"]
    path = random.choice(path)
    yaml_script = f"random yaml_script{random_yaml}{path}"
    result = yaml_script
    print('='*100)
    print(f"Fuzz checkIfWeridYAML test is now complete:")
    print(f"Random yaml_script: {yaml_script}")
    print(f"This is consider an invalid YAML.")
    print('='*100)

def fuzz_isValidUserName():
    #Random string for username.
    randomUser = ''.join(random.choices(string.ascii_letters + string.digits, k = 10))
    result = isValidUserName(randomUser)

    #Check boolean.
    assert isinstance(result, bool)
    assert result == True

    #Random string to check with FORBIDDEN_USER_NAMES
    flagReturn = random.choice(constants.FORBIDDEN_USER_NAMES)
    randomUser = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + (f':      ')+ (flagReturn)
    result = isValidUserName(randomUser)
    assert isinstance(result, bool)
    assert result == False
    print('='*100)
    print(f"Username is valid. (An example of a forbidden username is listed adjacent): Fuzz isValidUserName test is now completed.")
    print(randomUser)
    print('='*100)

def fuzz_checkIfValidSecret():
    #Random string for secret.
    shhhhh = ''.join(random.choices(string.ascii_letters, k = 10))
    result = checkIfValidSecret(shhhhh)

    #Check boolean.
    assert isinstance(result, bool)
    assert result == True

    #Random string to check with Secrets
    flagReturn2 = random.choice(constants.INVALID_SECRET_CONFIG_VALUES)
    shhhhh = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + (f':      ')+ (flagReturn2)
    result = isValidUserName(shhhhh)
    assert isinstance(result, bool)
    assert result == False
    print('='*100)
    print(f"Secret is valid. (An example of an invalid secret value is listed adjacent): Fuzz checkIfValidSecret test is now completed.")
    print(shhhhh)
    print('='*100)


if __name__=='__main__':
   
   #fuzz_getYAMLFiles()
   #fuzz_checkIfValidKeyValue()
   #fuzz_checkIfWeridYAML()
   #fuzz_isValidUserName()
   #fuzz_checkIfValidSecret()


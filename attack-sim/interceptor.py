import os
import shutil
import random
import string
import time

def create_fake_file(original_file_path, fake_file_path):
    with open(original_file_path, 'r') as original_file:
        with open(fake_file_path, 'w') as fake_file:
            for line in original_file:
                mutated_line = mutate_line(line)
                fake_file.write(mutated_line)

def mutate_line(line):
    fields = line.strip().split()
    mutated_fields = []

    for field in fields:
        if field.isdigit():
            mutated_value = str(4 * int(field))
            mutated_fields.append(mutated_value)
        else:
            mutated_fields.append(field)

    return ' '.join(mutated_fields) + '\n'

def find_symbolic_link(original_file_path):
    for root, dirs, files in os.walk('/'):
        for name in files:
            if os.path.islink(os.path.join(root, name)):
                link_path = os.path.join(root, name)
                if os.path.realpath(link_path) == original_file_path:
                    return link_path

    return None

def revert(original_file_path, original_link_path, hidden_directory):
    fake_file_path = os.path.join(hidden_directory, "fake.txt")

    if os.path.exists(original_link_path):
        os.remove(original_link_path)
        os.symlink(original_file_path, original_link_path)
        print(f"Restored original link: {original_link_path}")

    if os.path.exists(fake_file_path):
        os.remove(fake_file_path)
        print(f"Deleted fake data file: {fake_file_path}")

    if os.path.exists(hidden_directory):
        shutil.rmtree(hidden_directory)
        print(f"Deleted hidden directory: {hidden_directory}")


def replace_symbolic_link(original_file_path, fake_file_path):
    link_path = find_symbolic_link(original_file_path)

    if link_path:
        os.remove(link_path)
        os.symlink(fake_file_path, link_path)
        print(f"Replaced symbolic link: {link_path}")
    else:
        print("Symbolic link not found")

def generate_hidden_directory():
    while True:
        directory_name = ''.join(random.choices(string.ascii_lowercase, k=8))
        hidden_directory_path = os.path.join('/home/student', directory_name)
        if not os.path.exists(hidden_directory_path):
            os.mkdir(hidden_directory_path)
            return hidden_directory_path

if __name__ == "__main__":
    original_file_path = "/home/student/data.txt"
    original_link_path = find_symbolic_link(original_file_path)
    hidden_directory = generate_hidden_directory()
    fake_file_path = os.path.join(hidden_directory, "fake.txt")
    replace_symbolic_link(original_file_path, fake_file_path)
    print(f"Replaced symbolic link '{original_file_path}' with fake symbolic link '{fake_file_path}'")
    print("Generating fake data...")
    try:
        while True:
            if os.path.exists(original_file_path):
    	        print(f"{create_fake_file(original_file_path, fake_file_path)}")
                #replace_symbolic_link(original_file_path, fake_file_path)
            time.sleep(1)
    except KeyboardInterrupt:
        revert(original_file_path, original_link_path, hidden_directory)


import random
import string
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--length", "--filelength", help="the character length of each output file", type=int, default=2700)
parser.add_argument("-c", "--count", "--filecount", help="the number of files to generate", type=int, default=3)
parser.add_argument("--clean", help="cleans the output folder before generating files", action="store_true")
parser.add_argument("-f", "--outputfolder", help="designates the output folder for the generated files", default="./generated-files")
args = parser.parse_args()

## vars
file_length = args.length
file_count = args.count
folder_path = args.outputfolder


## create the output folder if it doesn't exist, and clean if desired.
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Created directory: {folder_path}")
else:
    if args.clean:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path) # Removes a file or a symlink
            except OSError as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        print(f"Directory already exists: {folder_path}")




# define the characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

for i in range(file_count):

    # this has to store the entire string in memory. for small string counts this is probably fine,
    # but it's probably going to cause problems if the character count is too large.
    # perhaps refactor this to continually append to the file in a loop instead of generating the whole string at once?
    random_string = ''.join(random.choice(characters) for i in range(file_length))
    
    # define filename for this file.
    file_name = os.path.join(folder_path, "random_characters_{}.txt".format(i))

    # Write the random string to a file
    with open(file_name, 'w') as f:
        f.write(random_string)

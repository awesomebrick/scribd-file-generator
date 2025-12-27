import random
import string

filelength = 2800

#for five different files
for i in range(5):

    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random string of length 100
    random_string = ''.join(random.choice(characters) for i in range(filelength))

    # Write the random string to a file
    with open("random_characters_{}.txt".format(i), 'w') as f:
        f.write(random_string)

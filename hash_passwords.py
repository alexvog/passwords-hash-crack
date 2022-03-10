from nacl import pwhash
import os.path

# Check if the credentials file exists
file_exists = os.path.exists('credentials.txt')

# If the file doesn't exist, create a new one
if file_exists == 0:
    file = open('credentials.txt', 'w')
    file.close()

# Open file for read
file = open('credentials.txt', 'r+')

# Check file size
file_size = os.path.getsize("credentials.txt")

# If the file size is null, it doesn't have users, set user count = 0
# If the file size is not null, check the number of users (user count)
if file_size == 0:
    user_count = 0
else:
    line = ""
    with file as f:
        for line in f:
            pass

        # Get last line string
        last_line = line

        # Convert last_line string to list and get the username
        username = last_line.split(":")[0]

        # Get user count number
        num = ""
        for c in username:
            if c.isdigit():
                num = num + c

    user_count = int(num) + 1

file.close()

# Open file for appending
file = open("credentials.txt", "a+")

# Input for creating a new user
input_ = input("Do you want to create a new user? Y/N ").lower()

# Check for input validity, if input is 'y', create a new user, if it is 'n', exit the loop
while input_ != 'n':
    if input_ == 'y':
        # Username with userxxx format
        username = "user" + str(user_count).zfill(3)

        print("Assigned username: " + username)
        password = input("Enter password: ")

        password = bytes(password, 'utf-8')
        hashed = pwhash.str(password)

        file.write(username + ":" + hashed.decode("utf-8") + "\n")

        print("Congratulations! You have succesfully created a new account!\n")

        user_count += 1
    else:
        print('Wrong input. Please enter Y or N')

    input_ = input("Do you want to create a new user? Y/N ").lower()

file.close()

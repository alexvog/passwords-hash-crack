from nacl import pwhash
import os.path

# Check if credentials file exists
credentials_exists = os.path.exists('credentials.txt')

if credentials_exists == 0:
    print("You must create some users first")
else:
    # Check file size
    file_size = os.path.getsize("credentials.txt")

    # If file size is null, it doesn't have users
    if file_size == 0:
        print("You must create some users first")
    else:
        # Check if most common passwords file exists
        pw_file_exists = os.path.exists('20_wordlist.txt')

        if pw_file_exists == 0:
            print("You must insert the most common passwords file with name \"20_wordlist.txt\"")
        else:
            # Open credentials file
            credentialsFile = open('credentials.txt', 'r')

            # Open the file where the hacked usernames and passwords are stored
            hackedFile = open('hacked_users.txt', 'w')

            # Search credentials file
            for credential in credentialsFile:
                # Get username and hashed password from credentials file
                username = credential.split(":")[0]
                hashedPassword = credential.split(":")[1]

                # Open most common passwords file
                wordlist = open("20_wordlist.txt", 'r')

                for password in wordlist:
                    bytes_pass = bytes(password.strip(), 'utf-8')
                    bytes_hashed_password = bytes(hashedPassword.strip(), 'utf-8')

                    try:
                        # Verify hashed password
                        pwhash.verify(bytes_hashed_password, bytes_pass)

                        # If user's password is hacked print the user credentials, and also store them to a file
                        print(username + " password is: " + password)
                        hackedFile.write(username + " : " + password)
                        break
                    except:
                        pass

                wordlist.close()
            hackedFile.close()

# passwords-hash-crack
A python project that we can create a file with hashed passwords and we can crack those passwords with a worldlist file

The project is divided into 2 programs: hash_passwords.py and crack_hash.py.

The libraries needed to run the programs are in the requirements.txt file.


## hash_passwords.py:

hash_passwords.py is a program that creates users with usernames in ascending order in userxxx format. The first user will have username user000, the second user001, and so on. All the checks are made so that if there are no users in the file, the numbering starts from 000, or if there are already some users in the file, the numbering continues by the last user numbering.

In the program we have the option to create many users. The question "Do you want to create a new user?" Y / N ", where we enter "y" if we want to create a new user or "n" if don't. If we select "y", then we can enter a password for the new user to be created.

The entered password is a hashed via the pwhash.str function of the nacl library.

The program creates a text file called "credentials.txt", where usernames and hashed passwords are stored in the following format:

**<p align="center">username: hashed_password</p>**



## crack_hash.py:

crack_hash.py is a program that accepts the text file "credentials.txt" created by the hash_passwords.py program and a text file "20_wordlist.txt", which contains 20 user passwords (usually the most common). The reason why 20_wordlist.txt contains only 20 passwords is due to the time it takes for hashed passwords to be broken. The more passwords the file contains, the more time the search takes.

The function that is used to perform the attack is pwhash.verify of the nacl library.

If the "credentials.txt" includes hashed passwords that are contained in the "20_wordlist" file, the users will be printed on the screen and stored in the "hacked_users.txt" file, along with their passwords.

# https://en.wikipedia.org/wiki/S/KEY
# First time user logs in, they enter a number.
# Hash the number and continue iteratively hashing the result 100 times, generating a hash chain.
# Perform 1 additional calculation and store the result on the server.
# Return the list of the other 100 to the user.
# Each time the user logs in, calculate f(n) where f() is the hash function and n is the attempted password
# If f(n) matches the value stored on the server, login is successful
# Now, store this user input so it cannot be used again
import hashlib


def encrypt(k):
    # Calculates the md5 hash of k, then the hash of that hash... (etc) x100 and returns an array of the values
    chain = []
    byte_string = k.encode('utf-8')
    print("Note: Once your keychain is empty, you will need to enter a new password.")
    # enter a new password if this is the last logon
    num = int(input("How many passwords would you like in your keychain?: "))
    for i in range(0, num):
        hash_string = hashlib.md5(byte_string).hexdigest()
        chain.append(hash_string)
        byte_string = hash_string.encode('utf-8')
    return chain


def newUser():
    name = input("Enter a username: ")
    with open("SKEY.txt", "r") as file:
        data = file.read()
        if name in data:
            raise ValueError('User already exists')
    # TODO: make the error checking above more graceful
    password_chain = encrypt(input("Enter a password: "))
    with open("keyChain.txt", "w") as keyChain:
        for p in reversed(password_chain):
            keyChain.write(p + '\n')
    # Calculate the 101st hash, which is the one that gets stored
    pass_to_store = password_chain[-1].encode('utf-8')
    hash_to_store = hashlib.md5(pass_to_store).hexdigest()
    with open("SKEY.txt", "a") as file:
        user_string = name + ':' + hash_to_store + '\n'
        file.write(user_string)


def tryPassword(u, p):
    # TODO: loop; give them 5 tries or something
    pwd = None
    with open("SKEY.txt", "r") as file:
        user_data = file.readlines()
    for entry in user_data:
        if u in entry:
            user_length = len(u) + 1
            pwd = entry[user_length:].strip()   # create a string with just the password
    p_bytes = p.encode('utf-8')
    p_hash = hashlib.md5(p_bytes).hexdigest()
    if pwd == p_hash:
        # print('Logon success.')
        # Update the user's entry with the new password
        for i, line in enumerate(user_data):
            if u in line:
                print(line)
                new_line = u + ':' + p + '\n'
                user_data[i] = new_line
                with open("SKEY.txt", "w") as file:
                    file.writelines(user_data)
                return True
    else:
        return False


def login():
    name = input("Enter a username: ")
    password = input("Enter your password: ")
    if tryPassword(name, password):
        print("Login success. Your keychain has been updated.")
        # TODO: update the keychain - probably above, in tryPassword() - also display number of keys left
    else:
        print("Login fail")
        # TODO: loop here

#newUser()
# tryPassword('hayden', '')
login()

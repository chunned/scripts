alphabet = "abcdefghijklmnopqrstuvwxyz"


def shift(r):
    front = alphabet[r:]
    back = alphabet[:r]
    shif = front + back
    return shif


def encrypt(m, r):
    shifted = shift(r)
    enc = ""
    for char in m:
        if char == ' ':
            enc += char
        else:
            i = alphabet.find(char)
            enc += shifted[i]
    print(enc)
    return enc


def getRot():
    try:
        rot = int(input("Choose the number to rotate by: "))
        if not -26 < rot < 26:
            raise ValueError("Please enter a number between -26 and 26")
    except ValueError:
        print("Please enter a number between -26 and 26")
        rot = getRot()
    return rot


if __name__ == '__main__':
    print("Basic rotational cipher. Lower-case alphabetic characters only.")
    msg = input("Enter a message to encrypt: ").lower()
    rota = getRot()
    encrypt(msg, rota)

# https://www.codewars.com/kata/62bdd252d8ba0e0057da326c/train/python
alphabet = " abcdefghijklmnopqrstuvwxyz"
def encrypt(word, n):
    print('ENCRYPTING')
    numWord = []
    for char in word:
        i = alphabet.find(char)
        print(f'{char} = {i}')
        numWord.append(i)
    print(f'RAW: {numWord}')
    for z in range(0, n):
        for i, num in enumerate(numWord):
            numWord[i] = ((num * 3) - 5)
    print(f'ENC: {numWord}')
    return numWord

def decrypt(word, n):
    print('DECRYPTING')
    print(f'RAW: {word}')
    while n > 0:
        for i, num in enumerate(word):
            x = (num + 5) // 3
            word[i] = x
        n -= 1
    strWord = ""
    for num in word:
        strWord += alphabet[num]
    print(f'DEC: {strWord}')
    return strWord


w = "abc"
x = encrypt(w, 2)

decrypt(x, 2)

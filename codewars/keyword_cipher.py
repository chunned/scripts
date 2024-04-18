# inspired by https://www.codewars.com/kata/57241cafef90082e270012d8/train/python
def keyword_cipher(msg, keyword):
    keyword = keyword.lower()
    msg = msg.lower()
    print(f'KEY: {keyword}')
    print(f'MSG: {msg}')
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    key = ""
    for i in keyword:
        if i not in key:
            key += i
    for i in alphabet:
        if i not in key:
            key += i
    print('CIPHER ALPHABET:')
    print(f'{alphabet}\n{key}')
    enc = ""
    for char in msg:
        j = alphabet.find(char)
        if j != -1:
            print(f'{char} -> {key[j]}')
            enc += key[j]
    return enc

if __name__ == '__main__':
    m = "Welcome home"
    k = "secret"
    c = keyword_cipher(m, k)
    print(c)

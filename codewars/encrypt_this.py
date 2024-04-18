# https://www.codewars.com/kata/5848565e273af816fb000449/train/python
def encrypt_this(m):
    if not m:
        return ''
    l = m.split(' ')
    outList = []
    for word in l:
        out = ''
        out += str(ord(word[0]))    # m[0] - first char of msg, ord = ascii value, convert to str and concat
        if len(word) > 1:
            out += word[-1]
        if len(word) > 2:
            for i in range(2, len(word) - 1):
                out += word[i]
            end = word[1]
            out += end
        outList.append(out)
    enc = ' '.join(outList)
    return enc


msg = "A wise old owl lived in an oak"
print(encrypt_this(msg))

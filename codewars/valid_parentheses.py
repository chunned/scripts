# https://www.codewars.com/kata/6411b91a5e71b915d237332d/train/python
def valid_parentheses(string):
    stack = []
    for paren in string:
        if paren == "(":
            stack.append("(")
        elif paren == ")":
            if stack:
                stack.pop()
            else:
                return False
    return False if stack else True

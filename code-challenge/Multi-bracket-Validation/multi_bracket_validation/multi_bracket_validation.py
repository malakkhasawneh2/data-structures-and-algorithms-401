def validate_brackets(string):
    open_brac = ''
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '{' or string[i] == '[':
            open_brac += string[i]
        if string[i] == ')':
            if open_brac[len(open_brac)-1] == '(':
                open_brac = open_brac[:(len(open_brac)-1)]
            else:
                return False
        if string[i] == '}':
            if open_brac[len(open_brac)-1] == '{':
                open_brac = open_brac[:(len(open_brac)-1)]
            else:
                return False
        if string[i] == ']':
            if open_brac[len(open_brac)-1] == '[':
                open_brac = open_brac[:(len(open_brac)-1)]
            else:
                return False

    if open_brac == '':
        return True
    else:
        return False  

if __name__ == "__main__":
    print(validate_brackets("{}()[]"))             
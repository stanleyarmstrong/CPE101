def str_rot_13(statement):
    newlist = []
    for i in statement:
        if (ord('a') <= ord(i) <= ord('z')) or (ord('A') <= ord(i) <= ord('Z')):
            if ord('a') <= ord(i) <= ord('z'):
                if ord(i) < ord('n'):
                    char_val = ord(i) + 13
                    newlist.append(chr(char_val))
                else:
                    char_val = ord(i) - 13
                    newlist.append(chr(char_val))
            else:
                if ord(i) < ord('N'):
                    char_val = ord(i) + 13
                    newlist.append(chr(char_val))
                else:
                    char_val = ord(i) - 13
                    newlist.append(chr(char_val))
    newstr = ''.join(newlist)
    return newstr


def str_translate_101(statement, constant, replace):
    clist = []
    for i in statement:
        if ord(i) == ord(constant):
            clist.append(replace)
        else:
            clist.append(i)
    cstr = ''.join(clist)
    return cstr



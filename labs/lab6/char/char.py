def is_lower_101(char):
    if ord('a') <= ord(char) <= ord('z'):
        return True
    else:
        return False


def char_rot_13(char):
    if (ord('a') <= ord(char) <= ord('z')) or (ord('A') <= ord(char) <= ord('Z')):
        if ord('a') <= ord(char) <= ord('z'):
            if ord(char) < ord('n'):
                char_val = ord(char) + 13
                return chr(char_val)
            else:
                char_val = ord(char) - 13
                return chr(char_val)
        else:
            if ord(char) < ord('N'):
                char_val = ord(char) + 13
                return chr(char_val)
            else:
                char_val = ord(char) - 13
                return chr(char_val)

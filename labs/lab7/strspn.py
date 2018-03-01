def my_strspn(str1, str2):
    count = 0
    if (type(str1) is not str) or (type(str2) is not str):
        return 0
    for i in str1:
        if i not in str2:
            break
        count += 1
    return count


def main():
    str1 = input('Enter string1: ')
    str2 = input('Enter String2: ')
    result_num = my_strspn(str1, str2)
    result_str = 'Result: ' + str(result_num)
    print(result_str)


if __name__ == '__main__':
    main()




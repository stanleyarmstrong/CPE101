def open_fun(file):
    in_file = open(file, 'r')
    line_num = 0
    for line in in_file:
        line = line.strip()
        print('Line', line_num, '('+str(len(line))+" chars): " + line)
        line_num += 1
    in_file.close()


def main():
    open_fun('in.txt')


if __name__ == '__main__':
    main()

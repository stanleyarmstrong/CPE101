def reverse_str(my_str):
    my_list = list(my_str)
    new_list = []
    for i in range(len(my_list)):
         new_list.append(my_list[len(my_list)- 1 - i])
    new_str = ''.join(new_list)
    return new_str

hello = reverse_str('hello')
print('Hello')
print(hello)
print(reverse_str('hi'))
print('SLO Hacks was cool')
print(reverse_str('SLO Hacks was cool'))

num_rows = int(input("Number of rows      : "))
num_col = int(input("Number of Columns    : "))
print(num_rows, "*", num_col, "multiplication table")

print()
print("  * |", end="")
for col in range(1, num_col +1):
    print('%5d' % col, end="")

print()

print('-----' , end="")

for col in range(1 , num_col + 1):
    print('-----', end='')


print()

for row in range(1, num_rows + 1):
    print("   "+str(row)+"|" ,end="")
    for col in range(1, num_col+1):
        print('%5d' % (row * col), end="")
    print()


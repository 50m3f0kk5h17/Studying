height = int(input('\nPlease enter the height of figure:\t'))
print()
width = (height * 2) - 1

print(' "A"')
for i in range(height):
    for k in range(width):
        if k == height - 1 - i or k == height - 1 + i or i == height - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()
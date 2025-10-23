RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
BLACK = '\u001b[30m'
GREEN = '\033[92m'

h, w = 15,40


def draw_cross(height=11, width=30):
    print(RED + ' ' * width + END)
    for i in range(height):
        if 4 <= i <= 6:
            print(RED + ' ' * 3 + WHITE + ' ' * 24 + RED + ' ' * 3 + END)
        else:
            print(RED + ' ' * 11 + WHITE + ' ' * 8 + RED + ' ' * 11 + END)
    print(RED + ' ' * 30 + END)

print('Task 1 : Swiss Flag')
draw_cross()


R =8
r =6
print('Task 2 : Pattern')
for y in range(h):
    for x in range(w):
        d1 = ((x - 10)**2 + (y - 7)**2)**0.5 # Euclidean distance
        d2 = ((x - 25)**2 + (y - 7)**2)**0.5 # Euclidean distance
        if (r <= d1 < R) or (r <= d2 < R):
            print(f"{BLACK}  {END}", end="")
        else:
            print(f"{WHITE}  {END}", end="")
    print()



print('Task 3 : Graphics')
for y in range(h, -1, -1):
        for x in range(w + 1):
            if x // 3== y:
                print(f"{BLACK} {END}", end="")
            else:
                print(f"{WHITE} {END}", end="")
        print()


print('Task 4 : Percentage')
f = open('sequence (1).txt')
numbers = [float(n.strip()) for n in f]
f.close()
digits = sum(-3 <= x <= 3 for x in numbers)
notdigits= sum(x < -3 or x > 3 for x in numbers)
percentage = (digits * 100) / (digits+ notdigits)
needed = int(percentage / 10)
least = 10 - needed
print(f'{percentage:.2f}% [{RED}{"+" * needed}{END} {GREEN}{"+" * least}{END}]')
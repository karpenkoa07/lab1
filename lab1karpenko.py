RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
BLACK = '\u001b[30m'
GREEN = '\033[92m'
h, w = 15,40
def draw_cross():
    print(RED + ' ' * 30 + END)
    for i in range(11):
        if 4 <= i <= 6:
            print(RED + ' ' * 3 + WHITE + ' ' * 24 + RED + ' ' * 3 + END)
        else:
            print(RED + ' ' * 11 + WHITE + ' ' * 8 + RED + ' ' * 11 + END)
    print(RED + ' ' * 30 + END)

print('Task 1 : Swiss Flag')
draw_cross()

def draw_pattern(cols, rows):
    tile = "OO"
    gap  = " "
    line = (gap + tile) * cols
    for _ in range(rows):
        print(line)
        print()
    print()

print('Task 2 : Pattern')
draw_pattern(8, 5)

print('Task 3 : Graphics')
for y in range(h, -1, -1):
        for x in range(w + 1):
            if x// 3== y:
                print(f"{BLACK} {END}", end="")
            else:
                print(f"{WHITE} {END}", end="")
        print()


print('Task 4 : Percentage')
f = open('sequence (1).txt', 'r')
numbers = [float(n.strip()) for n in f]
f.close()
chisla= sum(-3 <= x <= 3 for x in numbers)
net  = sum(x < -3 or x > 3 for x in numbers)
percentage = (chisla * 100) / (chisla + net)
percentage2 = (net * 100) / (chisla + net)
podh = int(percentage / 10)
ostalnye = 10 - podh
print(f'{percentage:.2f}% [{RED}{"+" * podh}{END} {GREEN}{"+" * ostalnye}{END}]{percentage2:.2f}%')







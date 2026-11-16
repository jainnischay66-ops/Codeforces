Black = {"q":9,"r":5,"b":3,"n":3,"p":1}
White = {"Q":9,"R":5,"B":3,"N":3,"P":1,}
black = 0
white = 0
for i in range(8):
    s = input().strip()
    for j in s:
        if j in Black:
            black += Black[j]
        elif j in White:
            white += White[j]
if white==black:
    print("Draw")
elif white>black:
    print("White")
else:
    print("Black")
players = int(input("Enter players: "))
played = input("Play: ").split()

t = 0
b = 0
f = 0

for i in range(players - 1):
    t += 1
    if played[f] == '1':
        if played[f+1] == '2':
            print(played[f])
            played.pop(f+1)
        elif played[f+1] == '3':
            print(played[f+1])
            played.pop(f)
    elif played[f] == '2':      
        if played[f+1] == '1':
            print(played[f+1])
            played.pop(f)
        elif played[f+1] == '3':
            print(played[f])
            played.pop(f+1)
    elif played[f] == '3':
        if played[f+1] == '1':
            print(played[f])
            played.pop(f+1)
        elif played[f+1] == '2':
            print(played[f+1])
            played.pop(f)
    f += 1
    if t == players / 2:
        f = 0
        continue
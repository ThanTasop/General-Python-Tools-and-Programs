
def states(l):
    print("+---+---+---+")
    print("| "+l[0]+" | "+l[1]+" | "+l[2]+" |")
    print("+---+---+---+")
    print("| "+l[3]+" | "+l[4]+" | "+l[5]+" |")
    print("+---+---+---+")
    print("| "+l[6]+" | "+l[7]+" | "+l[8]+" |")
    print("+---+---+---+")
def paikse():
    print(f"Player {player} plays")
    a=int(input("dwse prwth suntetagmenh: "))
    b=int(input("dwse deuterh suntetagmenh: "))
    while (a,b) in moves or a<1 or a>3 or b<1 or b>3:
        a=int(input("dwse prwth suntetagmenh, ALLO: "))
        b=int(input("dwse deuterh suntetagmenh, ALLO: "))
    moves.add((a,b))
    moves_X.add((a,b))
    state[3*(a-1)+b-1]=player
    states(state)

def pc_play():
    print(f"Player {player} plays")
    differences = []
    pc_wins = []
    for nikh in nikes:
        if moves.issuperset(nikh) == False:
            differences.append(nikh.difference(moves_X))
        if len(nikh.intersection(moves_O)) == 2 and moves.issuperset(nikh) == False:
            pc_wins = list(nikh.difference(moves_O))
    if len(pc_wins) >= 1:
        lis = pc_wins
    elif (2,2) not in moves:
        lis = [(2,2)]
    elif len(corners.difference(moves)) >= 3:
        corn = list(corners.difference(moves))
        lenghts = []
        for cn in corn:
            lenghts.append(0)
            for mov in moves_X:
                lenghts[len(lenghts)-1] += abs(cn[0]-mov[0])+abs(cn[1]-mov[1])
        m = min(lenghts)
        pos = lenghts.index(m)
        lis = [corn[pos]]
    elif moves_X == {(1,3),(3,1)} or moves_X == {(1,1),(3,3)}:
        se = positions.difference(corners)
        pcpl = list(se.difference(moves))
        lis = [pcpl[0]]

    else:
        lenghts = [len(diff) for diff in differences]
        m=min(lenghts)
        pos=lenghts.index(m)
        lis=list(differences[pos])
        for i in lis:
            if i not in moves_O:
                lis[0]=i
                break
    moves.add(lis[0])
    moves_O.add(lis[0])
    state[3*(lis[0][0]-1)+lis[0][1]-1]=player
    states(state)
def elegxos_nikhs(x):
    global a
    for nikh in nikes:
        if x.issuperset(nikh):
            a = 1
            print(f"Player {player} wins!")
            break


positions = {(i,j) for i in range(1,4) for j in range (1,4)}
state = [" " for i in range(9)]
moves = set()
moves_X = set()
moves_O = set()

nikes=[{(i,j) for j in range(1,4)} for i in range(1,4)]
b = [{(i,j) for i in range (1,4)} for j in range(1,4)]
nikes.extend(b)
nikes.extend([{(1,1),(2,2),(3,3)},{(1,3),(2,2),(3,1)}])
corners = {(1,1),(1,3),(3,1),(3,3)}

a = 0
player = "O"
for i in range(9):
    if player == "X":
        player = "O"
        pc_play()
        elegxos_nikhs(moves_O)
        if a == 1:
            break
    else:
        player = "X"
        paikse()
        elegxos_nikhs(moves_X)
        if a == 1:
            break

    if moves == positions:
        print("Draw!")
        break

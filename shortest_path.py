def jump(s,t,mvs=0):
    if s[0]==t[0]:
        moves = t[1]-s[1]
        abs_moves = abs(moves)
        if moves>0:
            for i in range(abs_moves):
                print("U")
        else:
            for i in range(abs_moves):
                print("D")
        mvs += abs_moves

    elif s[1]==t[1]:
        moves = ord(t[0]) - ord(s[0])
        abs_moves = abs(moves)
        if moves>0:
            for i in range(abs_moves):
                print("R")
        else:
            for i in range(abs_moves):
                print("L")
        mvs += abs_moves

    else:
        if t[0]>s[0]:
            if t[1]>s[1]:
                print("RU")
                jump([chr(ord((s[0])+1)),s[1]+1],t,mvs+1)
            else:
                print("RD")
                jump([chr((ord(s[0])+1)),s[1]-1],t,mvs+1)

        else:
            if t[1]>s[1]:
                print("LU")
                jump([chr((ord(s[0])-1)),s[1]+1],t,mvs+1)
            else:
                print("LD")
                jump([chr((ord(s[0])-1)),s[1]-1],t,mvs+1)

# inputs
s = input()
t = input()

# inputs in list format
s = [s[0],int(s[1])]
t = [t[0],int(t[1])]

jump(s,t)

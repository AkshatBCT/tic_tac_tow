move=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

st='''

{}|{}|{}
-----
{}|{}|{}
-----
{}|{}|{}

'''.format(*move)
print(st)

turn='o'

while 1:

    player_in=int(input(f'{turn} turn Enter location 0-8: '))
    if (move[player_in]!=' '):
       print('Location already in use, try again')
    else:
     move[player_in]=turn
     st='''

    {}|{}|{}
    -----
    {}|{}|{}
    -----
    {}|{}|{}

    '''.format(*move)
    print(st)
    if (move[0]==move[1]==move[2]!=' '):
       print('move[0] won')
       break
    if (move[3]==move[4]==move[5]!=' '):
       print('move[3] won')
       break
    if (move[6]==move[7]==move[8]!=' '):
       print('move[6] won')
       break
    if (move[0]==move[3]==move[6]!=' '):
       print('move[0] won')
       break
    if (move[1]==move[4]==move[7]!=' '):
       print('move[1] won')
       break
    if (move[2]==move[5]==move[8]!=' '):
       print('move[2] won')
       break
    if (move[0]==move[4]==move[8]!=' '):
       print('move[0] won')
       break
    if (move[2]==move[4]==move[6]!=' '):
       print('move[2] won')
       break
    if ' ' not in move:
       print('Match tie')
       break
    turn='x' if turn=='o' else 'o'
indices: list = [ [(i,j) for i in range(1,10)] for j in range(1,10) ]
init_puzzle: list = [ ['x' for _ in range(1,10)] for _ in range(1,10)]
x: str = 'x'

init_puzzle = [ [ x,x,x, x,1,x, x,x,4 ],
                [ 3,8,x, x,9,4, 2,5,x ],
                [ 4,x,x, 8,7,2, 6,1,3 ],
                [ 9,3,x, x,8,x, 7,4,5 ],
                [ 5,x,7, x,x,9, x,x,x ],
                [ x,x,x, x,x,x, 1,x,x ],
                [ 6,7,3, x,x,x, x,x,9 ],
                [ x,x,5, 9,x,6, 3,7,x ],
                [ 2,x,x, x,4,7, x,6,x ]]


#print(len(init_puzzle))
#print( [len(init_puzzle[i]) for i in range(9)] )

#for i in range(9): print(init_puzzle[i])

def find_candidates( puzzle: list, index: tuple) -> list :
    (i,j) = index

    return 0

def entire_row( puzzle: list, index: tuple) -> list:
    (i,j) = int(index[0]), int(index[1])
    return puzzle[i]

def entire_column(puzzle: list, index: tuple) -> list:
    (i,j) = int(index[0]) , int(index[1])
    col = [ puzzle[i][j] for i in range(9) ]
    return col

def entire_box(puzzle: list, index: tuple) -> list:
    i,j = int(index[0]), int(index[1])
    rows = list(range(3*(i//3),3*(i//3)+3))
    cols = list(range(3*(j//3),3*(j//3)+3))
    print(rows)
    print(cols)
    print((i,j))
    box = [ puzzle[x][y] for x in rows for y in cols ]
    return box

print(entire_box(init_puzzle,(0,8)))
#num=5
#print( [ i for i in range( 3*(num//3)+1,3*(num//3)+4) ] )
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
    i,j = int(index[0]) , int(index[1])
    candidate_list=[]
    if puzzle[i][j] == 'x':
        for candidate in range(1,10):
            if candidate not in entire_row(puzzle=puzzle , index=(i,j)):
                if candidate not in entire_column(puzzle=puzzle , index=(i,j)):
                    if candidate not in entire_box(puzzle=puzzle, index=(i,j)):
                        candidate_list.append(candidate)
    else:
        candidate_list.append(puzzle[i][j])
    return candidate_list

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
    #print(rows)
    #print(cols)
    #print((i,j))
    box = [ puzzle[x][y] for x in rows for y in cols ]
    return box

#print( find_candidates(puzzle=init_puzzle,index=(0,8)) )
all_candidates = [ [ find_candidates(puzzle=init_puzzle,index=(i,j)) for j in range(9) ] for i in range(9)  ]

#for i in range(9): print(all_candidates[i])

def update_puzzle(puzzle: list, candidate: list) -> list:
    #i,j = int(index[0]), int(index[1])
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 'x':
                if len(candidate[i][j]) == 1:
                    puzzle[i][j] = candidate[i][j][0]
    return puzzle

def print_puzzle(puzzle: list):
    #print("-"*29)
    for i in range(9):
        print("|",end='')
        for j in range(9):
            if puzzle[i][j] == 'x':
                print("   ",end='|')
            else:
                print(f' {puzzle[i][j]} ',end='|')
        print("\n",end='')
        #print("-"*29)

if __name__ == '__main__':
    puzzle = init_puzzle
    interations = 0
    while True:
        print(f'Iteration no {interations}')
        print('Current puzzle')
        interations += 1
        print_puzzle(puzzle)
        candidates = [ [ find_candidates(puzzle=puzzle,index=(i,j)) for j in range(9) ] for i in range(9) ]
        puzzle = update_puzzle(puzzle=puzzle,candidate=candidates)
        if all([ len(candidates[i][j]) == 1 for i in range(9) for j in range(9)]):
            break
    #for i in range(9): print(puzzle[i])
    print('Final puzzle')
    print_puzzle(puzzle)
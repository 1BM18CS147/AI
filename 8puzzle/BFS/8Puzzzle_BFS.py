def bfs_8Puzzle(src, target):
   queue = []
   queue.append(src)
    
   exp = []
    
   while len(queue) > 0:
        source = queue.pop(0)
        exp.append(source)
        
        print(source)
        
        if source==target:
            print("success")
            return
        
        poss_moves_to_do = []
        poss_moves_to_do = possible_moves(source,exp)
        
        for move in poss_moves_to_do:
            
            if move not in exp and move not in queue:
                queue.append(move)

def possible_moves(state, visited_states):
    b = state.index(-1)

    d = []

    if b not in [0, 1, 2]:
        d.append('u')
    if b not in [6, 7, 8]:
        d.append('d')
    if b not in [0, 3, 6]:
        d.append('l')
    if b not in [2, 5, 8]:
        d.append('r')

    pos_moves_it_can = []

    for i in d:
        pos_moves_it_can.append(gen(state, i, b))

    return [move_it_can for move_it_can in pos_moves_it_can if move_it_can not in visited_states]


def gen(state, m, b):
    temp = state.copy()

    if m == 'd':
        temp[b + 3], temp[b] = temp[b], temp[b + 3]

    if m == 'u':
        temp[b - 3], temp[b] = temp[b], temp[b - 3]

    if m == 'l':
        temp[b - 1], temp[b] = temp[b], temp[b - 1]

    if m == 'r':
        temp[b + 1], temp[b] = temp[b], temp[b + 1]

    return temp


print("Welcome to 8 puzzle solver!")

src=list(map(int,input("Enter source as an array").split(" ")))
target=list(map(int,input("Enter destination as an array").split(" ")))
print("Solving the puzzle using BFS")
bfs_8Puzzle(src, target)
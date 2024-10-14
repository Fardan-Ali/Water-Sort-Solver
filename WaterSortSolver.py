import copy

#dictionary for data entry
colours = {
    "re": [1, 1], "re2": [1, 2], "re3": [1, 3],
    "or": [2, 1], "or2": [2, 2], "or3": [2, 3],
    "br": [3, 1], "br2": [3, 2], "br3": [3, 3],
    "ye": [4, 1], "ye2": [4, 2], "ye3": [4, 3],
    "pu": [5, 1], "pu2": [5, 2], "pu3": [5, 3],
    "pi": [6, 1], "pi2": [6, 2], "pi3": [6, 3],
    "db": [7, 1], "db2": [7, 2], "db3": [7, 3],
    "lb": [8, 1], "lb2": [8, 2], "lb3": [8, 3],
    "dg": [9, 1], "dg2": [9, 2], "dg3": [9, 3],
    "lg": [10, 1], "lg2": [10, 2], "lg3": [10, 3],
    "te": [11, 1], "te2": [11, 2], "te3": [11, 3],
    "gr": [12, 1], "gr2": [12, 2], "gr3": [12, 3],
    "em": [-1, -1], "empty": [-1, -1]
}


# function which takes the current state and desired move, and returns the resulting state
def next_state_function(move, current_state):
    new_state = copy.deepcopy(current_state) #creates a copy of the current state to manipulate

    # ONLY CHANGE VALUES USING POP AND APPEND FUNCTIONS TO PREVENT CHANGING OTHER VALUES OF THE SAME AMOUNT

    # if target tube is empty, simply add the last value of source tube into target tube
    if not new_state[move[1]]:
        new_state[move[1]].append(new_state[move[0]].pop())

    # if liquid won't be overflowing, add the volume of top liquid in source tube to top liquid in target tube
    elif new_state[move[0]][-1][1] + sum(v for [_, v] in new_state[move[1]] ) <=4:
        new_value = [new_state[move[1]][-1][0], (new_state[move[1]][-1][1] + new_state[move[0]][-1][1])]
        new_state[move[1]].pop()
        new_state[move[1]].append(new_value)
        new_state[move[0]].pop()

    # if liquid will be overflowing, add and remove liquid equal to the available left space in target tube
    else:
        amount_to_pour = 4 - sum(v for [_, v] in new_state[move[1]])
        new_target_value = [new_state[move[1]][-1][0], new_state[move[1]][-1][1] + amount_to_pour]
        new_source_value = [new_state[move[0]][-1][0], new_state[move[0]][-1][1] - amount_to_pour]
        new_state[move[1]].pop()
        new_state[move[0]].pop()
        new_state[move[1]].append(new_target_value)
        new_state[move[0]].append(new_source_value)
    return new_state


# function which takes the current state, and returns true if the game is solved
def is_solved(current_state):
    # checks if the volume of the top liquid in non-empty tubes is 4 (therefore each tube contains only one liquid colour)
    for i in current_state:
        if i and i[-1][1] != 4:
            return False
    return True


# function which takes the current state, and returns a list of all possible moves
def valid_moves_function(current_state):

    valid_move_list = []
    source_tube_id = -1 # tracks the index of the source tube

    for source_tube in current_state:
        source_tube_id += 1
        target_tube_id = -1 # tracks the index of the target tube
        for target_tube in current_state:
            target_tube_id += 1
            # check if the tubes are different and source is not empty
            if source_tube and source_tube_id!=target_tube_id:
                # if the target is empty, ensure the source is not a single colour (redundant move)
                # if the target is not empty, ensure it is not full and the top fluid is the same colour
                if (not target_tube and source_tube[-1][1] != sum(v for _, v in source_tube)) or (target_tube and source_tube[-1][0]==target_tube[-1][0] and sum(v for _, v in target_tube) <= 3):
                        # add a tuple with the source and target to the valid moves list
                        valid_move_list.append((source_tube_id, target_tube_id))
    return valid_move_list


# function which takes the current state, and orders possible moves from worst to best
def best_moves(current_state):
    best_moves_list = [] # list to store moves from worst to best
    possible_moves = valid_moves_function(current_state) # receives list of possible moves

    #ADD THE WORST MOVES FIRST AND THE BETTER MOVES LATER SO THAT THE BEST MOVES ARE AT THE END OF THE LIST

    # Worst move is when all the liquid will not fit in the tube
    for move in possible_moves:
        if current_state[move[0]][-1][1] + sum(v for _, v in current_state[move[1]]) > 4:
            best_moves_list.append(move)
    possible_moves = [item for item in possible_moves if item not in best_moves_list]

    # Next worst move is pouring into an empty tube
    for move in possible_moves:
        if not current_state[move[1]]:
            best_moves_list.append(move)
    possible_moves = [item for item in possible_moves if item not in best_moves_list]

    # Next worst move is when pouring does not result in completing a colour
    for move in possible_moves:
        if current_state[move[0]][-1][1] + current_state[move[1]][-1][1] < 4:
            best_moves_list.append(move)
    possible_moves = [item for item in possible_moves if item not in best_moves_list]

    # Remaining possibilities are those which lead to a completed colour
    if possible_moves:
        for move in possible_moves:
            best_moves_list.append(move)
    return best_moves_list


#function to enter data and check for typos
def input_typo_checker():

    empty_vial = False
    output = []
    tube_fluid = 0
    colour_input = input(f"What's in tube {tubes + 1}? ")
    words = colour_input.split(' ')
    for ch in words:
        output += [colours.get(ch, [0, 0])]
        tube_fluid += output[-1][1]
    empty_vial = [-1, -1] in output
    while [0, 0] in output != False:
        colour_input = input("Incorrect spelling. Please enter again: ")
        tube_fluid = 0
        output = []
        words = colour_input.split(' ')
        for ch in words:
            output += [colours.get(ch, [0, 0])]
            tube_fluid += output[-1][1]
        empty_vial = [-1, -1] in output

    if empty_vial:
        game_state.append([])
    else:
        game_state.append(output)


#function to check if entered data is a possible starting position
def input_logic_check():
    colour_counter = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0]]

    # adds the volume of each fluid in each tube to the colour counter
    for each_tube in game_state:
        if each_tube:
            for each_fluid in each_tube:
                colour_counter[int(each_fluid[0]) - 1][1] += each_fluid[1]

        # Merges adjacent liquids of the same colour in a tube
        counter = 0
        while counter < (len(each_tube)-1):
            if each_tube[counter][0] == each_tube[counter + 1][0]:  # Check if first numbers are the same
                each_tube[counter] = [each_tube[counter][0], each_tube[counter][1] + each_tube[counter + 1][1]]
                each_tube.pop(counter+1)
            else:
                counter += 1

    # checks if there are 4 of each colour
    for each_colour in colour_counter:
        if each_colour[1] != 0 and each_colour[1] != 4:
            print("This combination of colours is impossible. There must be 4 of each colour.")
            return False
    return True

print("")
print("This program is a GBFS Solver for a Water Sort Puzzle. ")

#Inputting and verifying the starting tubes state
while True:
    game_state = []
    total_tubes = input("Enter the number of starting tubes: ")
    try:
        tube_number = int(total_tubes)
    except ValueError:
        total_tubes = input("That's not a number. How many tubes are there?: ")
        continue

    print("""Please enter each colour (from bottom to top) using the following format:
        pink = pi
        red = re
        orange = or
        yellow = ye
        light green = lg
        dark green = dg
        teal = te
        light blue = lb
        dark blue = db
        purple = pu
        brown = br
        gray = gr
        empty = em
        """)

    for tubes in range(tube_number):
        input_typo_checker()
    if input_logic_check():
        break

print ("\nInput verified. Calculating Solution... \n")

visited_states = [] # tracks the list of states visited
completed_moves = [] # tracks moves from start to current state
moves_stack = best_moves(game_state) # stores the ordered sequence of moves to try
states_stack = [game_state] # stores the ordered sequence of states to try
move_counter = [len(moves_stack)] # used to match moves to corresponding state


# Greedy Best-First Search
while moves_stack:
# USE CODE BELOW FOR DEBUGGING OR TRACKING INPUTS

    # print(f"The latest state is: {states_stack[-1]} ")
    # print (f"The move counter is {move_counter}")
    # print(f"The best moves left are:")
    # for i in range(move_counter[-1]):
    #     print(f"""      tube {moves_stack [-i-1][0]+1} to tube {moves_stack [-i-1][1]+1}""")
    # print (f"The failed states are: {len(visited_states)}")
    # print ("----------------------------------------------------------------------------------------------------------------------------")

    # if there are no more moves possible in the current state, revert to the previous state, and add this state to visited states
    if move_counter[-1] == 0:
        completed_moves.pop()
        moves_stack.pop()
        move_counter.pop()
        visited_states.append(states_stack.pop())

    # if the current state has moves to complete, execute the best move
    else:

        is_cycling = False # flag for continuing the loop if state is visited
        move_counter[-1] -= 1

        next_state = next_state_function(moves_stack[-1], states_stack[-1]) # the next state is calculated from the best move from the current state

        # checks if this state has been visited, rejects the move if true, otherwise adds it to visited states.
        for i in visited_states:
            if i == next_state:
                is_cycling = True
                break
        if is_cycling:
            moves_stack.pop()
            continue

        visited_states.append(next_state)

        # if the next state has possible moves: complete the move, and add it's possible moves to the move stack and counter.
        if valid_moves_function(next_state):
            states_stack.append(next_state)

            next_best_moves = best_moves(next_state)
            completed_moves.append(moves_stack[-1])
            move_counter.append(len(next_best_moves))
            for i in next_best_moves:
                moves_stack.append(i)

        # if the next state has no moves but is solved, add it to state stack, complete the move, and terminate the loop.
        elif is_solved(next_state):
            states_stack.append(next_state)
            completed_moves.append(moves_stack[-1])
            break

        # if the next state has no moves, and is not solved, reject the move.
        else:
            moves_stack.pop()

# once all moves have been tried, print the solution or state there is no solution.
if is_solved(states_stack[-1]):
    print(f"Moves tried: {len(visited_states)}")
    print("Solution found:")
    for i in completed_moves:
        print(f"Pour from tube {i[0]+1} to tube {i[1]+1}")
else:
    print(f"Moves tried: {len(visited_states)}")
    print('There is no Solution')

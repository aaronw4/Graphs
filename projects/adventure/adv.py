from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "C:/Users/aaron/Git/Graphs/projects/adventure/maps/test_line.txt"
# map_file = "C:/Users/aaron/Git/Graphs/projects/adventure/maps/test_cross.txt"
# map_file = "C:/Users/aaron/Git/Graphs/projects/adventure/maps/test_loop.txt"
# map_file = "C:/Users/aaron/Git/Graphs/projects/adventure/maps/test_loop_fork.txt"
map_file = "C:/Users/aaron/Git/Graphs/projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
def reverse_direction(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'


def queue_fxn(current_room, branch):
    current_exits = current_room.get_exits()
    current_branch = branch

    for an_exit in current_exits:
        stack_fxn(current_room, an_exit)

    for i in range(0, len(current_branch)):
        last_direction = current_branch.pop()
        return_direction = reverse_direction(last_direction)
        current_room.get_room_in_direction(return_direction)
        traversal_path.append(return_direction)
        

def stack_fxn(current_room, current_direction):
    new_stack = Stack()
    branch_path = []
    room = current_room.get_room_in_direction(current_direction)

    if room in visited:
        pass
    else:
        traversal_path.append(current_direction)
        branch_path.append(current_direction)
        new_stack.push(room)
        start = current_room
        dead_end = False
    
    while new_stack.size() > 0:
        room = new_stack.pop()
        new_exits = room.get_exits()
        visited.add(room)

        if len(new_exits) > 2:
            queue_fxn(room, branch_path)
        elif len(new_exits) == 1:
            new_direction = new_exits[0]
            new_next_room = room.get_room_in_direction(new_direction)
            if new_next_room not in visited:
                traversal_path.append(new_direction)
                main_queue.enqueue(new_next_room)
            else:
                dead_end = True
                for i in range(0, len(branch_path)):
                    last_direction = branch_path.pop()
                    return_direction = reverse_direction(last_direction)
                    room.get_room_in_direction(return_direction)
                    traversal_path.append(return_direction)
        else:
            if room.get_room_in_direction(new_exits[0]) in visited and room.get_room_in_direction(new_exits[1]) in visited:
                for i in range(0, len(branch_path)):
                    last_direction = branch_path.pop()
                    return_direction = reverse_direction(last_direction)
                    current_room.get_room_in_direction(return_direction)
                    traversal_path.append(return_direction)
            else:
                for new_possible_exit in new_exits:
                    new_next_room = room.get_room_in_direction(new_possible_exit)
                    if new_next_room not in visited:
                        traversal_path.append(new_possible_exit)
                        branch_path.append(new_possible_exit)
                        new_stack.push(new_next_room)
                    elif new_next_room == start and dead_end is False and len(branch_path) > 2:
                        traversal_path.append(new_possible_exit)
                    else:
                        pass
                    

starting_room = world.starting_room

traversal_path = []
visited = set()
main_queue = Queue()
main_queue.enqueue(starting_room)

while main_queue.size() > 0:
    room = main_queue.dequeue()

    if type(room) == tuple:
        location = room[0]
        movement = room[1]
        stack_fxn(location, movement)
    else:
        exits = room.get_exits()
        visited.add(room)

        if len(exits) > 2:
            for an_exit in exits:
                main_queue.enqueue((room, an_exit))
        elif len(exits) == 1:
            direction = exits[0]
            next_room = room.get_room_in_direction(direction)
            if next_room not in visited:
                traversal_path.append(direction)
                main_queue.enqueue(next_room)
            else:
                pass
        else:
            for possible_exit in exits:
                next_room = room.get_room_in_direction(possible_exit)
                if next_room not in visited:
                    traversal_path.append(possible_exit)
                    main_queue.enqueue(next_room)
                else:
                    pass






# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
    print(traversal_path)



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

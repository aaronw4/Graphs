from util import Stack, Queue
import copy

def get_parents(ancestors, node):
    parents = []
    for index in range(len(ancestors)):
        if ancestors[index][1] == node:
            parents.append(ancestors[index][0])

    if len(parents) == 0:
        return -1
    else:
        return parents


def earliest_ancestor(ancestors, starting_node):
    line = Stack()
    line.push([starting_node])
    paths = []
    
    while line.size() > 0:
        parent_path = line.pop()
        current_node = parent_path[-1]
        parents = get_parents(ancestors, current_node)

        if parents == -1:
            paths.append(parent_path)
        else:
            for parent in parents:
                one_path = copy.deepcopy(parent_path)
                one_path.append(parent)
                line.push(one_path)

    if len(paths) == 1 and len(paths[0]) == 1:
        return -1
    else:
        for x in range(len(paths)):
            longest = paths[0]
            if len(paths[x]) > len(longest):
                longest = paths[x]
            elif len(paths[x]) == len(longest):
                if longest[-1] > paths[x][-1]:
                    longest = paths[x]

        return longest[-1]

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import copy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}


    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO

    def bft(self, starting_vertex):
        line = Queue()
        line.enqueue(starting_vertex)
        visited = []
        
        while line.size() > 0:
            current_node = line.dequeue()
            if current_node not in visited:
                visited.append(current_node)
                neighbors = self.vertices[current_node]
                for neighbor in neighbors:
                    line.enqueue(neighbor)
        
        for x in range(len(visited)):
            print(visited[x])


    def dft(self, starting_vertex):
        line = Stack()
        line.push(starting_vertex)
        visited = []

        while line.size() > 0:
            current_node = line.pop()
            if current_node not in visited:
                visited.append(current_node)
                neighbors = self.vertices[current_node]
                for neighbor in neighbors:
                    line.push(neighbor)

        for x in range(len(visited)):
            print(visited[x])


    def dft_recursive(self, starting_vertex):
        visited = []

        def helper(vertex):
            if vertex not in visited:
                visited.append(vertex)
                neighbors = self.vertices[vertex]
                for neighbor in neighbors:
                    helper(neighbor)
            else:
                pass
        
        helper(starting_vertex)
        for x in range(len(visited)):
            print(visited[x])
       

    def bfs(self, starting_vertex, destination_vertex):
        line = Queue()
        line.enqueue([starting_vertex])
        visited = []

        while line.size() > 0:
            current_path = line.dequeue()
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path
            if current_node not in visited:
                visited.append(current_node)
                neighbors = self.vertices[current_node]
                for neighbor in neighbors:
                    one_path = copy.deepcopy(current_path)                 
                    one_path.append(neighbor)
                    line.enqueue(one_path)


    def dfs(self, starting_vertex, destination_vertex):
        line = Stack()
        line.push([starting_vertex])
        visited = []

        while line.size() > 0:
            current_path = line.pop()
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path
            if current_node not in visited:
                visited.append(current_node)
                neighbors = self.vertices[current_node]
                for neighbor in neighbors:
                    one_path = copy.deepcopy(current_path)
                    one_path.append(neighbor)
                    line.push(one_path)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        visited = []
        path = [starting_vertex]
        paths = []

        def helper(path):
            vertex = path[-1]

            if vertex == destination_vertex:
                paths.append(path)
            if vertex not in visited:
                visited.append(vertex)
                neighbors = self.vertices[vertex]
                for neighbor in neighbors:
                    new_path = copy.deepcopy(path)
                    new_path.append(neighbor)
                    helper(new_path)
            else:
                pass
        
        helper(path)

        for x in range(0, len(paths)):
            shortest = paths[0]
            if len(paths[x]) < len(shortest):
                shortest = paths[x]

        return shortest
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

import random, copy
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        
        # Add users
        for i in range(num_users):
            self.add_user(i)

        # Create friendships
        all_combinations = []

        for i in range(1, num_users + 1):
            for j in range(i + 1, num_users + 1):
                all_combinations.append((i, j))

        random.shuffle(all_combinations)

        for i in range(10):
            self.add_friendship(all_combinations[i][0], all_combinations[i][1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        line = Queue()
        line.enqueue([user_id])
        completed = []
        visited = {}  # Note that this is a dictionary, not a set

        while line.size() > 0:
            user_path = line.dequeue()
            user = user_path[-1]

            if user in completed:
                pass
            else:
                completed.append(user)
                friends = self.friendships[user]
            
                for i in range(len(friends)):
                    friend = friends.pop()
                    if friend in completed:
                        pass
                    else:
                        new_path = copy.deepcopy(user_path)
                        new_path.append(friend)
                        visited[friend] = new_path
                        line.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

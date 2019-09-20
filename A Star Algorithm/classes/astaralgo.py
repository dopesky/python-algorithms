import networkx as nx


class AStarTraverser:
    def __init__(self):
        # heuristics dictionary is always from point x to Imara Daima.
        self.heuristics = {
            'karen': 21.22,
            'gitaru': 25,
            'loresho': 16,
            'lavington': 12,
            'parklands': 10,
            'kilimani': 11,
            'langata': 15,
            'CBD': 8,
            'donholm': 4,
            'hill view': 12,
            'kasarani': 11,
            'kahawa': 16,
            'imara daima': 0,
            'j1': 19,
            'j2': 14.5,
            'j3': 10,
            'j4': 17,
            'j5': 12,
            'j6': 22,
            'j7': 24,
            'j8': 17,
            'j9': 14,
            'j10': 9,
            'j11': 11.7,
            'j12': 9,
            'j13': 4
        }
        self.visited = []
        self.closed = []
        self.endSearch = False

    @staticmethod
    def get_min_key(dictionary: dict):
        min_key = None
        min_num = None
        for key in dictionary.keys():
            if min_num is None:
                min_num = dictionary[key]
                min_key = key
            elif float(dictionary[key]) < float(min_num):
                min_num = dictionary[key]
                min_key = key
        return min_key

    def a_star(self, graph: nx.Graph, start_node, goal_node):
        queue = [start_node]
        cost_so_far = {
            start_node: 0
        }
        while len(queue) > 0 and not self.endSearch:
            fn = {}
            s = queue.pop(0)
            self.visited.append(s)
            print("Drive to", s, " Estate", end="\n")
            first_closed_index: int = -1
            for i in graph.neighbors(s):
                if i in self.closed:
                    minimum = min(self.closed.index(i), first_closed_index)
                    first_closed_index = self.closed.index(i) if first_closed_index is -1 else minimum
                    continue
                if len(list(graph.neighbors(s))) is 1:
                    self.closed.append(s)
                current_weight = graph.get_edge_data(s, i).get('weight')
                fn[i] = float(self.heuristics.get(i)) + float(current_weight) + cost_so_far.get(s)
            if len(fn) < 1 and first_closed_index > -1:
                key = self.closed[first_closed_index]
                self.closed.pop(first_closed_index)
                current_weight = graph.get_edge_data(s, key).get('weight')
                fn[key] = float(self.heuristics.get(key)) + float(current_weight) + cost_so_far.get(s)
            if len(fn) < 1:
                raise Exception("No Path to Destination Exists!")
            min_key = self.get_min_key(fn)
            if min_key in self.visited:
                index = self.visited.index(min_key)
                self.closed.append(self.visited[index + 1])
                self.closed.append(self.visited[index - 1])
            cost_so_far[min_key] = float(cost_so_far.get(s)) + float(graph.get_edge_data(s, min_key).get('weight'))
            queue.append(min_key)
            if min_key is goal_node:
                self.endSearch = True
                self.visited.append(min_key)
                break

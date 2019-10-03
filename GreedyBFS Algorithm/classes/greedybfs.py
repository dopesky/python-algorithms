import networkx as nx


class GreedyBFS:
    def __init__(self):
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

    def g_bfs(self, graph: nx.Graph, start_node, goal_node):
        queue = [start_node]
        while len(queue) > 0 and not self.endSearch:
            gn = {}
            s = queue.pop(0)
            self.visited.append(s)
            print("Drive to", s, " Estate", end="\n")
            for i in graph.neighbors(s):
                gn[i] = float(self.heuristics.get(i))
            if len(gn) < 1:
                raise Exception("No Path to Destination Exists!")
            min_key = self.get_min_key(gn)
            queue.append(min_key)
            if min_key is goal_node:
                self.endSearch = True
                self.visited.append(min_key)
                break

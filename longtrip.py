import numpy as np




class Board(object):
    """docstring for Board"""
    class Node(object):
        """docstring for Node"""
        def __init__(self,y,x):
            self.x = x
            self.y = y
            self.coor = [y, x]
            self.north_node = None
            self.south_node = None
            self.east_node = None
            self.west_node = None
            self.south_road = None
            self.west_road = None
            self.east_road = None
            self.neighbours = []
            self.connected_roads = 0

        def __str__(self):
            return f"({self.y},{self.x})"

        def activate_road_to_node(self, node):
            if node is self.north_node:
                self.north_road.active = True
            elif node is self.south_node:
                self.south_road.active = True
            elif node is self.east_node:
                self.east_road.active = True
            elif node is self.west_node:
                self.west_road.active = True
            else:
                assert(False)

    class Road(object):
        """docstring for Road."""

        def __init__(self):
            self.active = False

    def __init__(self):
        self.nodes = np.empty([8,8], dtype=object)
        self.init_nodes()
        self.init_neighbours()
        self.init_roads()

    def init_nodes(self):
        for y in range(8):
            for x in range(8):
                self.nodes[y,x] = self.Node(y,x)

    def init_neighbours(self):
        for row_num, row in enumerate(self.nodes):
            for col_num, node in enumerate(row):
                if col_num < 7:
                    node.east_node = self.nodes[row_num, col_num+1]
                    node.neighbours.append(node.east_node)
                if row_num < 7:
                    node.south_node = self.nodes[row_num+1, col_num]
                    node.neighbours.append(node.south_node)
                if col_num > 0:
                    node.west_node = self.nodes[row_num, col_num-1]
                    node.neighbours.append(node.west_node)
                if row_num > 0:
                    node.north_node = self.nodes[row_num-1, col_num]
                    node.neighbours.append(node.north_node)

    def init_roads(self):
        for row_num, row in enumerate(self.nodes):
            for col_num, node in enumerate(row):
                if col_num < 7:
                    node.east_road = self.Road()
                if row_num < 7:
                    node.south_road = self.Road()
                if col_num > 0:
                    node.west_road = node.west_node.east_road
                if row_num > 0:
                    node.north_road = node.north_node.south_road

    def init_fist_roads(self):
        for node in self.nodes.flatten():
                if len(node.neighbours) == 2:
                    for n in node.neighbours:
                        node.activate_road_to_node(n)

    def draw_board(self):
        for row_num, row in enumerate(self.nodes):
            mid_line = ''
            for col_num, node in enumerate(row):
                if row_num < 7:
                    mid_line += '|   ' if node.south_road.active else '    ';
                if col_num < 7:
                    print('o - ' if node.east_road.active else 'o   ', end='')
                else:
                    print('o', end='')

            if row_num < 7:
                print('\n', mid_line, sep='')


def test(board):
    board.nodes[0,5].activate_road_to_node(board.nodes[1,5])
    for node in board.nodes.flatten():
        for n in node.neighbours:
            print(n)



def main():
     board = Board()
     # test(board)
     board.init_fist_roads()
     board.draw_board()


if __name__ == '__main__':
    main()

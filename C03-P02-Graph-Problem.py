import csv

class System:
    steps = [   
        [-1,0], # Top Step
        [0,1],  # Right Step
        [1,0], # Bottom Step
        [0,-1] # Left Step
    ]
    
    def __init__(self):
        self.star_city = list()
        self.star_city_rows = 0
        self.star_city_cols = 0
        
    def config_system(self, file):
        data_file = open(file, 'r')
        reader = csv.reader(data_file)
        self.star_city = list()
        for row in reader:
            self.star_city.append(row)
        self.star_city_rows = len(self.star_city)
        self.star_city_cols = len(self.star_city[0])

    def check_limits(self, row_num, col_num):
        if 0 <= row_num < self.star_city_rows and 0 <= col_num < self.star_city_cols:
            return True
        return False

    def get_neighbours(self, row, col):
        neighbours = []
        for i in System.steps:
            if self.check_limits(row+i[0], col+i[1]):
                if self.star_city[row+i[0]][col+i[1]] <= self.star_city[row][col] and (row+i[0], col+i[1]) not in neighbours:
                    neighbours.append((row+i[0], col+i[1]))
        return neighbours

    def find_route(self,source,destination):
        
        _Queue = []
        for iter1 in range (self.star_city_rows +1):
            for iter2 in range(self.star_city_cols +1):
                visited = [[False]*(iter1)]*(iter2)

        _Queue.append(source)
        visited[source[0]][source[1]] = True

        path = []

        while len(_Queue)!=0:
            v = _Queue.pop(0)
            path.append(v)
            neighbours = self.get_neighbours(v[0], v[1])


            for i in neighbours:
                if i==destination:
                    path.append(i)
                    return path
                if not visited[i[0]][i[1]]:
                    _Queue.append(i)
                    visited[i[0]][i[1]]=True

        flag = True

    def Bluevalley_to_Smallville_route(self):
        
        flag = False
        route = test_system1.find_route((3,0),(3,4))
        print(f"\n\nTo reach city Smallville from city Blue Valley the nodes traversed are-")
        for nodenum, node in enumerate(route):
            if nodenum != len(route)-1:
                print(f"({node[0]}, {node[1]}) ---->",end=" ")
            else:
                print(f"({node[0]}, {node[1]})", end=" ")
            if flag == True:
                break

        
if __name__ == "__main__":
    test_system1 = System()
    
    #Getting data in 2D matrix
    test_system1.config_system('city_data.csv')
    
    #Finding path between Source node to Destination node
    route = test_system1.find_route((3,0),(4,2))
    print(f"\n\nTo reach Node (4,2) from Node (3,0) the nodes traversed are-")
    for nodenum, node in enumerate(route):
        if nodenum != len(route)-1:
            print(f"({node[0]}, {node[1]}) ---->", end=" ")
        else:
            print(f"({node[0]}, {node[1]})", end=" ")
    
    #Finding path between Bluevalley to Smallville   
    test_system1.Bluevalley_to_Smallville_route()

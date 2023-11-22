import random

class CityGrid():
    '''the class represents the city as a grid
       of dimensions MxN, where each grid cell
       stores information about the possibility
       of placing a telecommunications tower in it'''
    def __init__(self, m: int, n: int, blocked_ratio: float = 0.3):
        self._width = m
        self._height = n
        self._grid = [[1] * m for i in range(n)]
        self._blocked_count = int(n * m * random.uniform(blocked_ratio, 1))
        for block in range(self._blocked_count):
            while True:
                i = random.randint(0, m - 1)
                j = random.randint(0, n - 1)
                if self._grid[i][j] == 1:
                    self._grid[i][j] = 0
                    break   

    def get_grid(self) -> list[list]:
        return self._grid            
    
grid = CityGrid(10,10)
print(grid._blocked_count)   
print(grid.get_grid())    
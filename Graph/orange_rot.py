from typing import List


class Solution:
    # 还有可能1个新鲜橘子而且没有腐烂的橘子
    # 这中情况需要返回-1
    # 我的想法是统计所有新腐烂的橘子，是否等于所有的新鲜橘子
    # 如果等于，返回腐烂的分钟数，不等于则返回-1
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten, fresh_orange = self.find_rottenOranges(grid)
        # 这里如果直接没有新鲜橘子，那就直接返回0
        if fresh_orange == 0:
            return 0
        minutes = -1
        while len(rotten) !=0:
            minutes += 1
            this_turn  = len(rotten)
            direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for i in range(this_turn):
                x, y = rotten.pop(0)
                for dx, dy in direction:
                    new_x = x + dx
                    new_y = y + dy
                    if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        fresh_orange -= 1
                        rotten.append((new_x, new_y))
        if fresh_orange != 0:
            return -1
        return minutes
    
    def find_rottenOranges(self, grid):
        rotten = []
        fresh_orange = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh_orange += 1
        return rotten, fresh_orange
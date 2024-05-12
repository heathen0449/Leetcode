class UnionFind:
    # 查找的时候节点标号是从0开始的

    def __init__(self, n):
        self.parent = [i for i in range(n)] 
        # self.rank = [0 for _ in range(n)]
    
    def find(self, x):
        # 要有路径压缩
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def join(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            self.parent[pv] = pu
        
    def is_connected(self, u, v):
        return self.find(u) == self.find(v)
    

a = UnionFind(10)
a.join(1, 2)
a.join(3,2)
print(a.is_connected(1, 3))
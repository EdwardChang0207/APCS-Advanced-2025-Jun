class King:
    def __init__(self, ri, ci, si, ti):
        self.r = ri
        self.c = ci
        self.s = si
        self.t = ti
    def move(self, game_map:list):
        self.r += self.s
        self.c += self.t
        
        return game_map
#inputs
n, m, k = list(map(int, input().split()))
kings = [King(*list(map(int, input().split()))) for _ in range(k)]

#game init
game_map = [[0 for _ in range(m)] for _ in range(n)]
for king in kings:
    game_map[king.r][king.c] = -1
while kings:
    for i in range(len(kings)):
        die_idx = []
        king = kings[i]
        game_map = king.move(game_map)
        print(*game_map,sep='\n')
        if (king.r >= n) or (king.r < 0) or (king.c >= m) or (king.c < 0):
            die_idx.append(i)
            continue
        if game_map[king.r][king.c] == -1:
            die_idx.append(i)
            continue
        
        game_map[king.r][king.c] += 1
        game_map[king.r][king.c] = -1
        
        if game_map[king.r][king.c] == 2:
            game_map[king.r][king.c] = 0
    print(die_idx)

    die_idx.reverse()
    for i in die_idx:
        x, y = kings[i].r, kings[i].c
        if x >= 0 and x < m and y >= 0 and y <= n:
            game_map[x][y] = 0
        kings.pop(i)
    print(*game_map,sep='\n')
bomb = sum([row.count(-1) for row in game_map])
print(bomb)
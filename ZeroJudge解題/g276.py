class King:
    def __init__(self, ri, ci, si, ti):
        self.r = ri
        self.c = ci
        self.s = si
        self.t = ti
    def move(self, game_map:list):
        game_map[self.c][self.r] = 'b'
        self.r += self.s
        self.s += self.t
        game_map[self.c][self.r] = 'k'
        return game_map
#inputs
m, n, k = list(map(int, input().split()))
kings = [King(*list(map(int, input().split()))) for _ in range(k)]

#game init
game_map = [['' for _ in range(m)] for _ in range(n)]
while kings:
    die_idx = []
    for i in range(len(kings)):
        king = kings[i]
        game_map = king.move(game_map)
        if king.r >= m or king.r < 0 or king.c >= n or king.c < 0:
            die_idx.append(i)
            continue
        if game_map[king.c][king.r] == 'b':
            die_idx.append(i)
    die_idx.reverse()
    for i in die_idx:
        x, y = kings[i].c, kings[i].r
        if x >= 0 and x < m and y >= 0 and y <= n:
            game_map[x][y] = ''
        kings.pop(i)
bomb = sum([row.count('b') for row in game_map])
print(bomb)
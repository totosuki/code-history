import random

class Maze:
    def __init__(self,width,height):
        # フレーム分の+2
        self.width = width + 2
        self.height = height + 2
        self.player_x = 1
        self.player_y = 1
        self.map = None
        self.goal = None
    

    def create_map(self):
        # 幅が下限値を下回っている場合、下限値に設定する
        minLimit = 5
        if self.width < minLimit:
            self.width = minLimit
            print(f"幅が{minLimit}以下の為{self.width}に設定しました")
        
        # 高さが下限値を下回っている場合、下限値に設定する
        if self.height < minLimit:
            self.height = minLimit
            print(f"高さが{minLimit}以下の為{self.height}に設定しました")

        # 幅が奇数でない場合、奇数に調整する
        if self.width % 2 == 0:
            self.width += 1
            print(f"幅が偶数のため、{self.width}に調整しました")
        
        # 高さが奇数でない場合、奇数に調整する
        if self.height % 2 == 0:
            self.height += 1
            print(f"高さが偶数のため、{self.height}に調整しました")

        self.width = self.width | 1

        # 掘る前の迷路配列を用意
        self.map = [[1] * self.width for _ in range(self.height)]

        # スタート位置(迷路生成の)
        start_x = 1
        start_y = 1
        # 枠作成
        self.map[start_y][start_x] = 0
        for i in range(self.height):
                self.map[i][0] = 1
                self.map[i][self.width-1] = 1
        for i in range(self.width):
                self.map[0][i] = 1
                self.map[self.height-1][i] = 1
        # プレイヤーの座標
        self.map[1][1] = 2

        # 迷路初期の表示
        # for row in self.map:
        #     print(row)

        # 穴掘り法の実装
        stack = [(start_x, start_y)]
        while stack:
            current_x, current_y = stack[-1]

            # 周囲の未探索セルを取得
            unvisited_neighbors = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_x, next_y = current_x + 2 * dx, current_y + 2 * dy
                if 0 <= next_x < self.width and 0 <= next_y < self.height:
                    if self.map[next_y][next_x] == 1:
                        unvisited_neighbors.append((next_x, next_y))

            if unvisited_neighbors:
                # ランダムに未探索セルを選択し、壁を取り除く
                next_x, next_y = random.choice(unvisited_neighbors)
                self.map[next_y][next_x] = 0

                # 探索済みのセルをスタックに追加
                stack.append((next_x, next_y))

                # 選択したセルとその隣接セルの間の壁を取り除く
                wall_x, wall_y = current_x + (next_x - current_x) // 2, current_y + (next_y - current_y) // 2
                self.map[wall_y][wall_x] = 0
            else:
                # 探索済みのセルをスタックから削除
                stack.pop()

    def find_farthest_point(self):
        distances = [[float('inf')] * self.width for _ in range(self.height)]
        start_x, start_y = 1, 1
        distances[start_y][start_x] = 0

        queue = [(start_x, start_y)]
        while queue:
            x, y = queue.pop(0)

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.map[ny][nx] == 0:
                    if distances[ny][nx] == float('inf'):
                        distances[ny][nx] = distances[y][x] + 1
                        queue.append((nx, ny))

        goal_x, goal_y = None, None
        max_distance = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == 0 and distances[y][x] > max_distance:
                    max_distance = distances[y][x]
                    goal_x, goal_y = x, y

        if goal_x is not None and goal_y is not None:
            self.map[goal_y][goal_x] = 3
            self.goal = [goal_y,goal_x]

    def move_up(self):
        if self.map[self.player_y-1][self.player_x] != 1:
            self.map[self.player_y][self.player_x] = 0
            self.player_y -= 1
            self.map[self.player_y][self.player_x] = 2

    def move_down(self):
        if self.map[self.player_y+1][self.player_x] != 1:
            self.map[self.player_y][self.player_x] = 0
            self.player_y += 1
            self.map[self.player_y][self.player_x] = 2

    def move_left(self):
        if self.map[self.player_y][self.player_x-1] != 1:
            self.map[self.player_y][self.player_x] = 0
            self.player_x -= 1
            self.map[self.player_y][self.player_x] = 2

    def move_right(self):
        if self.map[self.player_y][self.player_x+1] != 1:
            self.map[self.player_y][self.player_x] = 0
            self.player_x += 1
            self.map[self.player_y][self.player_x] = 2

    def print_map(self):
        for row in self.map:
            print(row)
        for row in self.map:
            line = ''.join(['＃' if cell == 1 else '　' for cell in row])
            print(line) 

    # map拡張関数numには拡張するマスが入るダメかも
    def expansion_map(self,num):
        container = []
        container_2 = []
        for i in self.map:
            for j in i: 
                for _ in range(num):
                    container.append(j)

        for _ in range(num):
            container_2.append(container)
        self.map = container_2

# # 迷路のサイズを指定して迷路を生成
# maze_width = 50
# maze_height = 12
# maze = Maze(maze_width,maze_height)
# maze.create_map()
# maze.find_farthest_point()
# maze.print_map()
# print(maze.goal[0],"と",maze.goal[1])

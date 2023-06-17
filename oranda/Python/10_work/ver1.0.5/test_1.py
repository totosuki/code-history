import random

class Stage:
    def __init__(self, width, height, complexity, density):
        self.width = width
        self.height = height
        self.complexity = complexity
        self.density = density
        self.map_data = None

    def generate_maze(self):
        # マップの初期化
        self.map_data = [['#' for _ in range(self.width)] for _ in range(self.height)]

        # 迷路生成用の開始位置をランダムに決定
        start_x = random.randint(0, self.width - 1)
        start_y = random.randint(0, self.height - 1)

        # 迷路生成開始
        self._generate_maze_recursive(start_x, start_y)

    def _generate_maze_recursive(self, x, y):
        if self.map_data[y][x] == '#':
            # タイルを空きスペースに変更
            self.map_data[y][x] = ' '

            # パラメータに基づいてランダムな方向に移動する
            for _ in range(self.complexity):
                direction_x = random.randint(-1, 1)
                direction_y = random.randint(-1, 1)
                new_x = x + direction_x
                new_y = y + direction_y

                if 0 < new_x < self.width - 1 and 0 < new_y < self.height - 1:
                    self._generate_maze_recursive(new_x, new_y)

    def print_map(self):
        for row in self.map_data:
            print(''.join(row))

    def reshape_map(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map_data[y][x] == '#':
                    if self._is_connected(x, y):
                        self.map_data[y][x] = ' '

    def _is_connected(self, x, y):
        # 上下左右のタイルが空きスペースかどうかを確認する
        up = y - 1 >= 0 and self.map_data[y - 1][x] == ' '
        down = y + 1 < self.height and self.map_data[y + 1][x] == ' '
        left = x - 1 >= 0 and self.map_data[y][x - 1] == ' '
        right = x + 1 < self.width and self.map_data[y][x + 1] == ' '

        # 縦または横のどちらかで繋がっているかを判定する
        return (up and down) or (left and right)


# マップのサイズやパラメータを指定して迷路生成
stage = Stage(40, 40, 3, 0)
stage.generate_maze()

# 生成される前のマップの表示
stage.print_map()
print(" ")

# 生成されたマップの整形
stage.reshape_map()

# 生成されたマップの表示
# stage.print_map()

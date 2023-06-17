import random

class Maze:
    # 初期化(map生成まで)
    def __init__(self,N,M):
        # マップの初期化
        map_data = [[1] * M for _ in range(N)]

        # 部屋と通路の最小サイズと最大サイズを設定
        min_room_size = 3
        max_room_size = 6

        # 部屋の生成
        rooms = []
        num_rooms = 0

        for _ in range(100):  # 最大100回の試行で部屋を生成
            w = random.randint(min_room_size, max_room_size)
            h = random.randint(min_room_size, max_room_size)
            x = random.randint(1, M - w - 1)
            y = random.randint(1, N - h - 1)

            new_room = Room(x, y, w, h)

            # 部屋が他の部屋と重なっていないか確認
            if not any(new_room.intersects(other_room) for other_room in rooms):
                # 部屋をマップに描画
                for i in range(new_room.x1, new_room.x2):
                    for j in range(new_room.y1, new_room.y2):
                        map_data[j][i] = 0

                # 部屋の中心座標を保存
                center_x, center_y = new_room.center()

                if num_rooms == 0:
                    # 最初の部屋の場合はプレイヤーの初期位置に設定
                    player_x, player_y = center_x, center_y
                else:
                    # 2つ目以降の部屋の場合は前の部屋から通路を作成
                    prev_room = rooms[num_rooms - 1]
                    prev_center_x, prev_center_y = prev_room.center()

                    # 部屋と部屋を繋ぐ通路を作成
                    if random.random() < 0.5:
                        # 水平に通路を延ばし、垂直につなぐ
                        self.create_h_tunnel(map_data, prev_center_x, center_x, prev_center_y)
                        self.create_v_tunnel(map_data, prev_center_y, center_y, center_x)
                    else:
                        # 垂直に通路を延ばし、水平につなぐ
                        self.create_v_tunnel(map_data, prev_center_y, center_y, prev_center_x)
                        self.create_h_tunnel(map_data, prev_center_x, center_x, center_y)

                # 生成された部屋を保存
                rooms.append(new_room)
                num_rooms += 1

        self.map_data = map_data
        self.player_x = player_x
        self.player_y = player_y
    
    def create_h_tunnel(self,map_data, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            map_data[y][x] = 0

    def create_v_tunnel(self,map_data, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            map_data[y][x] = 0    

    def move_up(self):
        if self.map_data[self.player_y-1][self.player_x] != 1:
            self.map_data[self.player_y][self.player_x] = 0
            self.player_y -= 1
            self.map_data[self.player_y][self.player_x] = 2

    def move_down(self):
        if self.map_data[self.player_y+1][self.player_x] != 1:
            self.map_data[self.player_y][self.player_x] = 0
            self.player_y += 1
            self.map_data[self.player_y][self.player_x] = 2

    def move_left(self):
        if self.map_data[self.player_y][self.player_x-1] != 1:
            self.map_data[self.player_y][self.player_x] = 0
            self.player_x -= 1
            self.map_data[self.player_y][self.player_x] = 2

    def move_right(self):
        if self.map_data[self.player_y][self.player_x+1] != 1:
            self.map_data[self.player_y][self.player_x] = 0
            self.player_x += 1
            self.map_data[self.player_y][self.player_x] = 2

class Room:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        return center_x, center_y

    def intersects(self, other):
        # 他の部屋との交差判定を行う
        return (
            self.x1 <= other.x2
            and self.x2 >= other.x1
            and self.y1 <= other.y2
            and self.y2 >= other.y1
        )

def print_map(map_data):
    for row in map_data:
        print(row)

# マップサイズの指定
map_width = 30
map_height = 20

# マップの生成(引数にはマップの大きさなどが入るが、「部屋と通路の最小サイズと最大サイズを設定」なども将来的には入れたい)
map_ = Maze(map_width,map_height)

# マップの表示
print_map(map_.map_data)

# プレイヤーの位置を表示
map_.map_data[map_.player_y][map_.player_x] = 3

# 更新されたマップの表示
print_map(map_.map_data)


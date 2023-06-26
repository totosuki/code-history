import random

'''
定義
0=道
1=壁
2=プレイヤー
3=ゴール
'''

class Stage:
    def __init__(self) -> None:
        self.map_data = None
        self.player_x = None
        self.player_y = None
        self.rooms = None

    def generate_maze(self, N, M):
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
        self.map_data[player_y][player_x] = 2
        self.player_x = player_x
        self.player_y = player_y
        self.rooms = rooms

    def create_h_tunnel(self,map_data, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            map_data[y][x] = 0

    def create_v_tunnel(self,map_data, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            map_data[y][x] = 0
        
    # ゴール作成関数
    def place_goal(self):
        # ランダムに部屋を選択
        room = random.choice(self.rooms)

        # 部屋内のランダムな座標をゴールとする
        goal_x = random.randint(room.x1 + 1, room.x2 - 1)
        goal_y = random.randint(room.y1 + 1, room.y2 - 1)

        # ゴールをマップに設置
        self.map_data[goal_y][goal_x] = 3

    # 扉作成関数
    def place_door(self):
        for room in self.rooms:
            # 各部屋の中心座標
            center_x = (room.x1 + room.x2) // 2
            center_y = (room.y1 + room.y2) // 2

            # 部屋と繋がる通路の中で、部屋に最も近い位置をドアにする
            min_distance = float('inf')
            door_x, door_y = None, None

            for x, y in room.get_connected_corridors(self.map_data):
                distance = abs(x - center_x) + abs(y - center_y)
                if distance < min_distance:
                    min_distance = distance
                    door_x, door_y = x, y

            # ドアを設置
            self.map_data[door_y][door_x] = 4


    def get_corridor(self,room1, room2):
        # 部屋1と部屋2の中心座標を取得
        center1_x, center1_y = room1.center()
        center2_x, center2_y = room2.center()

        corridor = []

        # 部屋1から部屋2への水平な通路を作成
        for x in range(center1_x, center2_x + 1):
            corridor.append((x, center1_y))

        # 部屋1から部屋2への垂直な通路を作成
        for y in range(center1_y, center2_y + 1):
            corridor.append((center2_x, y))

        return corridor
    
    # 動き関係の関数
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
    
    def print_stage(self):
        for row in self.map_data:
            print(row)

class Room:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
        self.edges = self.get_edges()

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
    
    def get_edges(self):
        # 部屋の4辺の座標を返す
        edges = []

        for x in range(self.x1, self.x2 + 1):
            edges.append((x, self.y1))
            edges.append((x, self.y2))

        for y in range(self.y1 + 1, self.y2):
            edges.append((self.x1, y))
            edges.append((self.x2, y))

        return edges
    
    def get_connected_corridors(self, map_data):
        connected_corridors = []

        for x, y in self.edges:
            # 隣接する座標の値が通路であれば、接続された通路として追加
            if map_data[y][x] == 0:
                connected_corridors.append((x, y))

        return connected_corridors

# マップサイズの指定
stage_width = 30
stage_height = 20

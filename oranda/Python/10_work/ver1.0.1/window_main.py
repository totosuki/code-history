# インポート関係
import pygame
import math
import game_map

# シーンの基底クラス
class Scene:
    def __init__(self):
        pass

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass

# ボタンクラス
class Button:
    def __init__(self, x, y, width, height, color, hover_color, text, text_color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_color = text_color
        self.action = action
        self.is_hovered = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered and self.action:
                self.action()

    def draw(self, screen):
        button_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, button_color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

# タイトル画面
class TitleScene(Scene):
    def __init__(self):
        super().__init__()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # ゲーム画面に切り替える
                return HelpScene()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    return TitleScene()
                elif event.key == pygame.K_g:
                    return GameScene()
                elif event.key == pygame.K_e:
                    return pygame.quit()
                elif event.key == pygame.K_h:
                    return HelpScene()

    def update(self):
        pass

    def render(self, screen):
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont("harenosora", 40)
        text = font.render("Click To Start", True, (0, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

# メニュー画面
class HelpScene:
    def __init__(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    return TitleScene()
                elif event.key == pygame.K_g:
                    return GameScene()
                elif event.key == pygame.K_e:
                    return pygame.quit()
                elif event.key == pygame.K_h:
                    return HelpScene()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return GameScene()

    def update(self):
        pass

    def render(self, screen):
        font_siz = 40
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont("harenosora", font_siz)
        font_2 = pygame.font.SysFont("Arial", font_siz)

        # write関数、描きたい文字と表示したい位置を設定して
        def write(text,width = WIDTH//2,height = HEIGHT//2,fonts=font):
            text = fonts.render(text,True,(0, 0 , 0))
            text_rect = text.get_rect(center = (width,height))
            screen.blit(text,text_rect)
        
        # wrt関数writeの省略系、センター寄せで記入されるのとテキストはlistで渡してほしい
        def wrt(text_list):

            count = 1
            margin = 1.5
            for text in text_list:
                text = font.render(text,True,( 0, 0 , 0))
                # 後で余白計算等をしないと計算狂うから気をつけて
                text_rect = text.get_rect(center = ( WIDTH // 2,( HEIGHT // 2 - font_siz * (len(text_list)/2+0.5) * margin) + count * font_siz * margin))
                screen.blit(text,text_rect)
                count += 1

        text_list = ["タイトル画面は[t]","ゲーム画面は[g]","終了は[e]"]
        wrt(text_list)

        # log
        # write("→",1380,600)
        # write("------------------------------------------------------------------------------------------",WIDTH // 2, HEIGHT // 2)

# ゲーム画面(迷路)
class GameScene(Scene):
    
    def __init__(self):
        super().__init__()
        # 迷路のサイズを指定して迷路を生成
        maze_width = 30
        maze_height = 30
        self.maze = game_map.Maze(maze_width,maze_height)
        self.map = self.maze.map_data

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    return TitleScene()
                elif event.key == pygame.K_g:
                    return GameScene()
                elif event.key == pygame.K_e:
                    return pygame.quit()
                elif event.key == pygame.K_h:
                    return HelpScene()
                elif event.key == pygame.K_UP:
                    self.maze.move_up()
                elif event.key == pygame.K_DOWN:
                    self.maze.move_down()
                elif event.key == pygame.K_LEFT:
                    self.maze.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.maze.move_right()

    def update(self):
        pass

    def render(self, screen):
        # 一回前の画面を綺麗に消す処理
        screen.fill((255, 255, 255))

        # 迷路を描画する処理
        siz = HEIGHT / len(self.map) if HEIGHT / len(self.map) < WIDTH / len(self.map[0]) else WIDTH / len(self.map[0])
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == 1:
                    pygame.draw.rect(screen, (0, 0, 0), (siz*x,siz*y,siz,siz),)
                if self.map[y][x] == 2:
                    pygame.draw.rect(screen, (0, 255, 255), (siz*x,siz*y,siz,siz),)
                if self.map[y][x] == 3:
                    pygame.draw.rect(screen, (255, 0, 0), (siz*x,siz*y,siz,siz),)

# ウィンドウのサイズを設定
WIDTH = 1440
HEIGHT = 650

# フレームレート
FPS = 30

# pygameを初期化し、ウィンドウを作成
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# タイトル画面の初期化
current_scene = TitleScene()

# ゲームループ
running = True
while running:
    # イベントの処理
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # 現在のシーンでイベントを処理
    next_scene = current_scene.handle_events(events)

    # シーンの切り替え
    if next_scene:
        current_scene = next_scene

    # 現在のシーンを更新
    current_scene.update()

    # 現在のシーンを描画
    current_scene.render(screen)

    # 画面の更新
    pygame.display.flip()

    # tick
    clock.tick(FPS)

# pygameの終了
pygame.quit()
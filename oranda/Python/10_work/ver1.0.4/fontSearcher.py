import pygame
import sys

# Pygameの初期化
pygame.init()

# ウィンドウのサイズ
width, height = 800, 600
size = (width, height)

# ウィンドウの作成
screen = pygame.display.set_mode(size)

# ウィンドウのタイトル
pygame.display.set_caption("Font Test")

# フォントのサイズ
font_size = 36

# フォントの描画位置
text_x = 50
text_y = 50
font_name_x = 50
font_name_y = 100

# フォントの描画色
color = (255, 255, 255)  # 白色

# フォントのリスト
fonts = pygame.font.get_fonts()

# 現在のフォントのインデックス
current_font_index = 0

# イベントループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # キーが押されたときの処理
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # 上キーが押されたとき、フォントを1つ前に変更
                current_font_index -= 1
                if current_font_index < 0:
                    current_font_index = len(fonts) - 1

            elif event.key == pygame.K_DOWN:
                # 下キーが押されたとき、フォントを1つ後に変更
                current_font_index += 1
                if current_font_index >= len(fonts):
                    current_font_index = 0

    # 描画用のフォントを取得
    font_name = fonts[current_font_index]
    font = pygame.font.SysFont(font_name, font_size)

    # テキストを描画
    text_surface = font.render("aあ", True, color)
    text_width, text_height = text_surface.get_size()

    # テキストをスクロール可能な領域の範囲内に制限する
    max_x = width - text_width
    max_y = height - text_height

    if text_x < 0:
        text_x = 0
    elif text_x > max_x:
        text_x = max_x

    if text_y < 0:
        text_y = 0
    elif text_y > max_y:
        text_y = max_y

    # ウィンドウをクリア
    screen.fill((0, 0, 0))

    # テキストを描画
    screen.blit(text_surface, (text_x, text_y))

    # 現在のフォント名を描画
    font_name_surface = font.render(font_name, True, color)
    screen.blit(font_name_surface, (font_name_x, font_name_y))

    # ウィンドウの更新
    pygame.display.flip()


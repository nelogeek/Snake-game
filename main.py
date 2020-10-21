import pygame
import sys
import random
import time


class Game():
    def __init__(self):
        # Р·Р°РґР°РµРј СЂР°Р·РјРµСЂС‹ СЌРєСЂР°РЅР°
        self.screen_width = 720
        self.screen_height = 460

        # РЅРµРѕР±С…РѕРґРёРјС‹Рµ С†РІРµС‚Р°
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(165, 42, 42)

        # Frame per second controller
        # Р±СѓРґРµС‚ Р·Р°РґР°РІР°С‚СЊ РєРѕР»РёС‡РµСЃС‚РІРѕ РєР°РґСЂРѕРІ РІ СЃРµРєСѓРЅРґСѓ
        self.fps_controller = pygame.time.Clock()

        # РїРµСЂРµРјРµРЅРЅР°СЏ РґР»СЏ РѕС‚РѕСЂР±СЂР°Р¶РµРЅРёСЏ СЂРµР·СѓР»СЊС‚Р°С‚Р°
        # (СЃРєРѕР»СЊРєРѕ РµРґС‹ СЃСЉРµР»Рё)
        self.score = 0

    def init_and_check_for_errors(self):
        """РќР°С‡Р°Р»СЊРЅР°СЏ С„СѓРЅРєС†РёСЏ РґР»СЏ РёРЅРёС†РёР°Р»РёР·Р°С†РёРё Рё
           РїСЂРѕРІРµСЂРєРё РєР°Рє Р·Р°РїСѓСЃС‚РёС‚СЃСЏ pygame"""
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print('Ok')

    def set_surface_and_title(self):
        """Р—Р°РґР°РµРј surface(РїРѕРІРµСЂС…РЅРѕСЃС‚СЊ РїРѕРІРµСЂС… РєРѕС‚РѕСЂРѕР№ Р±СѓРґРµС‚ РІСЃРµ СЂРёСЃРѕРІР°С‚СЊСЃСЏ)
        Рё СѓСЃС‚Р°РЅР°РІР»РёРІР°РµРј Р·Р°РіР°Р»РѕРІРѕРє РѕРєРЅР°"""
        self.play_surface = pygame.display.set_mode((
            self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake Game')

    def event_loop(self, change_to):
        """Р¤СѓРЅРєС†РёСЏ РґР»СЏ РѕС‚СЃР»РµР¶РёРІР°РЅРёСЏ РЅР°Р¶Р°С‚РёР№ РєР»Р°РІРёС€ РёРіСЂРѕРєРѕРј"""

        # Р·Р°РїСѓСЃРєР°РµРј С†РёРєР» РїРѕ РёРІРµРЅС‚Р°Рј
        for event in pygame.event.get():
            # РµСЃР»Рё РЅР°Р¶Р°Р»Рё РєР»Р°РІРёС€Сѓ
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = "DOWN"
                # РЅР°Р¶Р°Р»Рё escape
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # elif event.key == ord('r'):

        return change_to

    def refresh_screen(self):
        """РѕР±РЅРѕРІР»СЏРµРј СЌРєСЂР°РЅ Рё Р·Р°РґР°РµРј С„РїСЃ"""
        pygame.display.flip()
        game.fps_controller.tick(23)

    def show_score(self, choice=1):
        """РћС‚РѕР±СЂР°Р¶РµРЅРёРµ СЂРµР·СѓР»СЊС‚Р°С‚Р°"""
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render(
            'Score: {0}'.format(self.score), True, self.black)
        s_rect = s_surf.get_rect()
        # РґРµС„РѕР»С‚РЅС‹Р№ СЃР»СѓС‡Р°Р№ РѕС‚РѕР±СЂР°Р¶Р°РµРј СЂРµР·СѓР»СЊС‚Р°С‚ СЃР»РµРІР° СЃРІРµСЂС…Сѓ
        if choice == 1:
            s_rect.midtop = (80, 10)
        # РїСЂРё game_overe РѕС‚РѕР±СЂР°Р¶Р°РµРј СЂРµР·СѓР»СЊС‚Р°С‚ РїРѕ С†РµРЅС‚СЂСѓ
        # РїРѕРґ РЅР°РґРїРёСЃСЊСЋ game over
        else:
            s_rect.midtop = (360, 120)
        # СЂРёСЃСѓРµРј РїСЂСЏРјРѕСѓРіРѕР»СЊРЅРёРє РїРѕРІРµСЂС… surface
        self.play_surface.blit(s_surf, s_rect)

    def game_over(self):
        """Р¤СѓРЅРєС†РёСЏ РґР»СЏ РІС‹РІРѕРґР° РЅР°РґРїРёСЃРё Game Over Рё СЂРµР·СѓР»СЊС‚Р°С‚РѕРІ
        РІ СЃР»СѓС‡Р°Рµ Р·Р°РІРµСЂС€РµРЅРёСЏ РёРіСЂС‹ Рё РІС‹С…РѕРґ РёР· РёРіСЂС‹"""
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('Game over', True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        go_again = pygame.font.SysFont('monaco', 72).render(
            "Enter 'R'", True, self.red).get_rect().midtop
        go_again = (360, 40)
        self.play_surface.blit(go_surf, go_rect, go_again)
        self.show_score(0)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()


class Snake():
    def __init__(self, snake_color):
        # РІР°Р¶РЅС‹Рµ РїРµСЂРµРјРµРЅРЅС‹Рµ - РїРѕР·РёС†РёСЏ РіРѕР»РѕРІС‹ Р·РјРµРё Рё РµРіРѕ С‚РµР»Р°
        self.snake_head_pos = [100, 50]  # [x, y]
        # РЅР°С‡Р°Р»СЊРЅРѕРµ С‚РµР»Рѕ Р·РјРµРё СЃРѕСЃС‚РѕРёС‚ РёР· С‚СЂРµС… СЃРµРіРјРµРЅС‚РѕРІ
        # РіРѕР»РѕРІР° Р·РјРµРё - РїРµСЂРІС‹Р№ СЌР»РµРјРµРЅС‚, С…РІРѕСЃС‚ - РїРѕСЃР»РµРґРЅРёР№
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.snake_color = snake_color
        # РЅР°РїСЂР°РІР»РµРЅРёРµ РґРІРёР¶РµРЅРёРµ Р·РјРµРё, РёР·РЅР°С‡Р°Р»СЊРЅРѕ
        # Р·Р°РґР°РґРёРјСЃСЏ РІРїСЂР°РІРѕ
        self.direction = "RIGHT"
        # РєСѓРґР° Р±СѓРґРµС‚ РјРµРЅСЏС‚СЊСЃСЏ РЅР°РїСЂРІР»РµРЅРёРµ РґРІРёР¶РµРЅРёСЏ Р·РјРµРё
        # РїСЂРё РЅР°Р¶Р°С‚РёРё СЃРѕРѕС‚РІРµС‚СЃС‚РІСѓСЋС‰РёС… РєР»Р°РІРёС€
        self.change_to = self.direction

    def validate_direction_and_change(self):
        """Р�Р·РјРµРЅРёСЏРµРј РЅР°РїСЂР°РІР»РµРЅРёРµ РґРІРёР¶РµРЅРёСЏ Р·РјРµРё С‚РѕР»СЊРєРѕ РІ С‚РѕРј СЃР»СѓС‡Р°Рµ,
        РµСЃР»Рё РѕРЅРѕ РЅРµ РїСЂСЏРјРѕ РїСЂРѕС‚РёРІРѕРїРѕР»РѕР¶РЅРѕ С‚РµРєСѓС‰РµРјСѓ"""
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to

    def change_head_position(self):
        """Р�Р·РјРµРЅРёСЏРµРј РїРѕР»РѕР¶РµРЅРёРµ РіРѕР»РѕРІС‹ Р·РјРµРё"""
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += 10
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 10
        elif self.direction == "UP":
            self.snake_head_pos[1] -= 10
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 10

    def snake_body_mechanism(
            self, score, food_pos, screen_width, screen_height):
        # РµСЃР»Рё РІСЃС‚Р°РІР»СЏС‚СЊ РїСЂРѕСЃС‚Рѕ snake_head_pos,
        # С‚Рѕ РЅР° РІСЃРµС… С‚СЂРµС… РїРѕР·РёС†РёСЏС… РІ snake_body
        # РѕРєР°Р¶РµС‚СЃСЏ РѕРґРёРЅ Рё С‚РѕС‚ Р¶Рµ СЃРїРёСЃРѕРє СЃ РѕРґРёРЅР°РєРѕРІС‹РјРё РєРѕРѕСЂРґРёРЅР°С‚Р°РјРё
        # Рё РјС‹ Р±СѓРґРµРј СѓРїСЂР°РІР»СЏС‚СЊ Р·РјРµРµР№ РёР· РѕРґРЅРѕРіРѕ РєРІР°РґСЂР°С‚Р°
        self.snake_body.insert(0, list(self.snake_head_pos))
        # РµСЃР»Рё СЃСЉРµР»Рё РµРґСѓ
        if (self.snake_head_pos[0] == food_pos[0] and
                self.snake_head_pos[1] == food_pos[1]):
            # РµСЃР»Рё СЃСЉРµР»Рё РµРґСѓ С‚Рѕ Р·Р°РґР°РµРј РЅРѕРІРѕРµ РїРѕР»РѕР¶РµРЅРёРµ РµРґС‹ СЃР»СѓС‡Р°Р№РЅС‹Рј
            # РѕР±СЂР°Р·РѕРј Рё СѓРІРµР»РёС‡РёРІРµРј score РЅР° РѕРґРёРЅ
            food_pos = [random.randrange(1, screen_width/10)*10,
                        random.randrange(1, screen_height/10)*10]
            score += 1
        else:
            # РµСЃР»Рё РЅРµ РЅР°С€Р»Рё РµРґСѓ, С‚Рѕ СѓР±РёСЂР°РµРј РїРѕСЃР»РµРґРЅРёР№ СЃРµРіРјРµРЅС‚,
            # РµСЃР»Рё СЌС‚РѕРіРѕ РЅРµ СЃРґРµР»Р°С‚СЊ, С‚Рѕ Р·РјРµСЏ Р±СѓРґРµС‚ РїРѕСЃС‚РѕСЏРЅРЅРѕ СЂР°СЃС‚Рё
            self.snake_body.pop()
        return score, food_pos

    def draw_snake(self, play_surface, surface_color):
        """РћС‚РѕР±СЂР°Р¶Р°РµРј РІСЃРµ СЃРµРіРјРµРЅС‚С‹ Р·РјРµРё"""
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            # pygame.Rect(x,y, sizex, sizey)
            pygame.draw.rect(
                play_surface, self.snake_color, pygame.Rect(
                    pos[0], pos[1], 10, 10))

    def check_for_boundaries(self, game_over, screen_width, screen_height):
        """РџСЂРѕРІРµСЂРєР°, С‡С‚Рѕ СЃС‚РѕР»РєСѓРЅР»РёСЃСЊ СЃ РєРѕРЅС†Р°РјРё СЌРєСЂР°РЅР° РёР»Рё СЃР°РјРё СЃ СЃРѕР±РѕР№
        (Р·РјРµСЏ Р·Р°РєРѕР»СЊС†РµРІР°Р»Р°СЃСЊ)"""
        if any((
            self.snake_head_pos[0] > screen_width-10
            or self.snake_head_pos[0] < 0,
            self.snake_head_pos[1] > screen_height-10
            or self.snake_head_pos[1] < 0
        )):
            game_over()
        for block in self.snake_body[1:]:
            # РїСЂРѕРІРµСЂРєР° РЅР° С‚Рѕ, С‡С‚Рѕ РїРµСЂРІС‹Р№ СЌР»РµРјРµРЅС‚(РіРѕР»РѕРІР°) РІСЂРµР·Р°Р»СЃСЏ РІ
            # Р»СЋР±РѕР№ РґСЂСѓРіРѕР№ СЌР»РµРјРµРЅС‚ Р·РјРµРё (Р·Р°РєРѕР»СЊС†РµРІР°Р»РёСЃСЊ)
            if (block[0] == self.snake_head_pos[0] and
                    block[1] == self.snake_head_pos[1]):
                game_over()


class Food():
    def __init__(self, food_color, screen_width, screen_height):
        """Р�РЅРёС‚ РµРґС‹"""
        self.food_color = food_color
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_pos = [random.randrange(1, screen_width/10)*10,
                         random.randrange(1, screen_height/10)*10]

    def draw_food(self, play_surface):
        """РћС‚РѕР±СЂР°Р¶РµРЅРёРµ РµРґС‹"""
        pygame.draw.rect(
            play_surface, self.food_color, pygame.Rect(
                self.food_pos[0], self.food_pos[1],
                self.food_size_x, self.food_size_y))


game = Game()
snake = Snake(game.green)
food = Food(game.brown, game.screen_width, game.screen_height)

game.init_and_check_for_errors()
game.set_surface_and_title()

while True:
    snake.change_to = game.event_loop(snake.change_to)

    snake.validate_direction_and_change()
    snake.change_head_position()
    game.score, food.food_pos = snake.snake_body_mechanism(
        game.score, food.food_pos, game.screen_width, game.screen_height)
    snake.draw_snake(game.play_surface, game.white)

    food.draw_food(game.play_surface)

    snake.check_for_boundaries(
        game.game_over, game.screen_width, game.screen_height)

    game.show_score()
    game.refresh_screen()

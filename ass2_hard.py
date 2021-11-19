import pygame
import os
from pygame.locals import *
from ass2_store1 import *
from ass2_store2 import *
from ass2_store3 import *
from ass2_store4 import *

class hard:
    pygame.init()
    pygame.mixer.init()
    hit_block = pygame.mixer.Sound((os.path.join('hit_block.wav')))
    hit_enermy = pygame.mixer.Sound((os.path.join('hit_enermy.wav')))
    illusion_sound = pygame.mixer.Sound((os.path.join('illusion_sound.wav')))
    charge_sound = pygame.mixer.Sound((os.path.join('charge_sound.wav')))
    win_sound = pygame.mixer.Sound((os.path.join('win_sound.wav')))
    lose_sound = pygame.mixer.Sound((os.path.join('lose_sound.wav')))

    def __init__(self):
        self.block = BLOCK(3)
        self.ball = main_ball()
        self.enermy = enermies(2)
        self.illu_ball1 = illusion(0)
        self.illu_ball2 = illusion(2)
        self.illu_ball3 = illusion(4)
        self.power_ball = power_ball()
        self.hit = 0
        self.hit_count = 80
        self.ball_speed = 0.05
        self.block_speed = 0.06
        self.add_x = 0
        self.decision = 0
        self.run = True
        self.stop = False
        self.game_start = False
        self.arrow_key = False
        self.draw1 = True
        self.draw2 = True
        self.draw3 = True
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        self.illu1_move_up = False
        self.illu1_move_down = False
        self.illu1_move_left = False
        self.illu1_move_right = False
        self.illu2_move_up = False
        self.illu2_move_down = False
        self.illu2_move_left = False
        self.illu2_move_right = False
        self.illu3_move_up = False
        self.illu3_move_down = False
        self.illu3_move_left = False
        self.illu3_move_right = False
        self.power_move_down = False
        self.block_move_left = False
        self.block_move_right = False
        self.power_hit = False
        self.power_gain = False
        self.illu_sound_start = False
        self.illu_sound_end = False
        self.lose_sound_start = False
        self.lose_sound_end = False
        self.win_sound_start = False
        self.win_sound_end = False
        self.started = False
        self.endgame = False

    def restart(self):
        self.block = BLOCK(3)
        self.ball = main_ball()
        self.enermy = enermies(2)
        self.illu_ball1 = illusion(0)
        self.illu_ball2 = illusion(2)
        self.illu_ball3 = illusion(4)
        self.power_ball = power_ball()
        self.hit = 0
        self.hit_count = 80
        self.ball_speed = 0.05
        self.block_speed = 0.06
        self.add_x = 0
        self.decision = 0
        self.run = True
        self.stop = False
        self.game_start = False
        self.arrow_key = False
        self.draw1 = True
        self.draw2 = True
        self.draw3 = True
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        self.illu1_move_up = False
        self.illu1_move_down = False
        self.illu1_move_left = False
        self.illu1_move_right = False
        self.illu2_move_up = False
        self.illu2_move_down = False
        self.illu2_move_left = False
        self.illu2_move_right = False
        self.illu3_move_up = False
        self.illu3_move_down = False
        self.illu3_move_left = False
        self.illu3_move_right = False
        self.power_move_down = False
        self.block_move_left = False
        self.block_move_right = False
        self.power_hit = False
        self.power_gain = False
        self.illu_sound_start = False
        self.illu_sound_end = False
        self.lose_sound_start = False
        self.lose_sound_end = False
        self.win_sound_start = False
        self.win_sound_end = False
        self.started = False
        self.endgame = False

    #############################################   run   #############################################
    def RUN(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if not self.stop and event.key == K_SPACE and not self.started:
                        self.game_start = True
                        self.move_up = True
                        self.move_right = True
                        self.started = True
                    if self.game_start:
                        if event.key == K_LEFT:
                            self.block_move_left = True
                        if event.key == K_RIGHT:
                            self.block_move_right = True
                    if event.key == K_ESCAPE and self.stop:
                        self.decision = 1
                    if event.key == K_RETURN and self.stop:
                        self.decision = 2
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        self.block_move_left = False
                    if event.key == K_RIGHT:
                        self.block_move_right = False

            board.game_board(self)
            board.score_board(self)
            word.word(self, 3, self.hit_count)
            self.block.draw()
            self.ball.draw_ball(self.power_gain)
            self.enermy.draw()

            ##############################    ball movement    ##############################
            if self.move_up:
                self.ball.ball_y += self.ball_speed
                self.move_down = False
            if self.move_down:
                self.ball.ball_y -= self.ball_speed
                self.move_up = False
            if self.move_left:
                self.ball.ball_x -= self.ball_speed + 0.005
                self.move_right = False
            if self.move_right:
                self.ball.ball_x += self.ball_speed + 0.005
                self.move_left = False

            if self.illu1_move_up:
                self.illu_ball1.illu_ball_y += self.ball_speed - 0.025
                self.illu1_move_down = False
            if self.illu1_move_down:
                self.illu_ball1.illu_ball_y -= self.ball_speed - 0.025
                self.illu1_move_up = False
            if self.illu1_move_left:
                self.illu_ball1.illu_ball_x -= self.ball_speed + 0.005
                self.illu1_move_right = False
            if self.illu1_move_right:
                self.illu_ball1.illu_ball_x += self.ball_speed + 0.005
                self.illu1_move_left = False

            if self.illu2_move_up:
                self.illu_ball2.illu_ball_y += self.ball_speed - 0.025
                self.illu2_move_down = False
            if self.illu2_move_down:
                self.illu_ball2.illu_ball_y -= self.ball_speed - 0.025
                self.illu2_move_up = False
            if self.illu2_move_left:
                self.illu_ball2.illu_ball_x -= self.ball_speed + 0.005
                self.illu2_move_right = False
            if self.illu2_move_right:
                self.illu_ball2.illu_ball_x += self.ball_speed + 0.005
                self.illu2_move_left = False

            if self.illu3_move_up:
                self.illu_ball3.illu_ball_y += self.ball_speed - 0.025
                self.illu3_move_down = False
            if self.illu3_move_down:
                self.illu_ball3.illu_ball_y -= self.ball_speed - 0.025
                self.illu3_move_up = False
            if self.illu3_move_left:
                self.illu_ball3.illu_ball_x -= self.ball_speed + 0.005
                self.illu3_move_right = False
            if self.illu3_move_right:
                self.illu_ball3.illu_ball_x += self.ball_speed + 0.005
                self.illu3_move_left = False

            if self.power_move_down:
                self.power_ball.power_ball_y -= self.ball_speed - 0.025

            ##############################    block control    ##############################
            if self.block_move_left and self.block.block_x1 >= -1.75:
                self.block.block_x -= self.block_speed
            if self.block_move_right and self.block.block_x2 <= 5.28:
                self.block.block_x += self.block_speed

            ##############################    ball hit wall    ##############################
            if self.ball.ball_xright >= 5.38:
                self.move_right = False
                self.move_left = True
            if self.ball.ball_ytop >= 4:
                self.move_up = False
                self.move_down = True
            if self.ball.ball_xleft <= -1.85:
                self.move_left = False
                self.move_right = True
            if self.ball.ball_ybtm <= -3.99:
                self.lose_sound_start = True
                if self.lose_sound_start and not self.lose_sound_end:
                    pygame.mixer.Channel(5).play(self.lose_sound)
                    self.lose_sound_end = True
                sign.draw_lose(self)
            if self.ball.ball_ybtm <= -4.05:
                self.move_left = False
                self.move_right = False
                self.move_up = False
                self.move_down = False
                self.game_start = False
                self.stop = True
                break

            if self.illu_ball1.illu_ball_xright >= 5.38:
                self.illu1_move_right = False
                self.illu1_move_left = True
            if self.illu_ball1.illu_ball_ytop >= 4:
                self.illu1_move_up = False
                self.illu1_move_down = True
            if self.illu_ball1.illu_ball_xleft <= -1.85:
                self.illu1_move_left = False
                self.illu1_move_right = True

            if self.illu_ball2.illu_ball_xright >= 5.38:
                self.illu2_move_right = False
                self.illu2_move_left = True
            if self.illu_ball2.illu_ball_ytop >= 4:
                self.illu2_move_up = False
                self.illu2_move_down = True
            if self.illu_ball2.illu_ball_xleft <= -1.85:
                self.illu2_move_left = False
                self.illu2_move_right = True

            if self.illu_ball3.illu_ball_xright >= 5.38:
                self.illu3_move_right = False
                self.illu3_move_left = True
            if self.illu_ball3.illu_ball_ytop >= 4:
                self.illu3_move_up = False
                self.illu3_move_down = True
            if self.illu_ball3.illu_ball_xleft <= -1.85:
                self.illu3_move_left = False
                self.illu3_move_right = True

            if self.illu_ball1.illu_ball_ybtm <= -4:
                self.draw1 = False
            if self.illu_ball2.illu_ball_ybtm <= -4:
                self.draw2 = False
            if self.illu_ball3.illu_ball_ybtm <= -4:
                self.draw3 = False

            ###############################    ball hit block    ##############################
            if self.ball.ball_xbtm >= self.block.block_x1 and \
                    self.ball.ball_xbtm <= self.block.block_x2 and \
                    self.ball.ball_ybtm < self.block.block_y2 and \
                    self.ball.ball_ybtm > self.block.block_y1:
                pygame.mixer.Channel(1).play(self.hit_block)
                self.move_down = False
                self.move_up = True
                if self.block_move_left:
                    self.move_left = True
                if self.block_move_right:
                    self.move_left = False
                    self.move_right = True
                if self.power_hit:
                    self.power_gain = False
                    self.power_hit = False

            if self.illu_ball1.illu_ball_xbtm >= self.block.block_x1 and \
                    self.illu_ball1.illu_ball_xbtm <= self.block.block_x2 and \
                    self.illu_ball1.illu_ball_ybtm < self.block.block_y2 and \
                    self.illu_ball1.illu_ball_ybtm > self.block.block_y1:
                pygame.mixer.Channel(1).play(self.hit_block)
                self.illu1_move_down = False
                self.illu1_move_up = True
                if self.block_move_left:
                    self.illu1_move_left = True
                if self.block_move_right:
                    self.illu1_move_left = False
                    self.illu1_move_right = True

            if self.illu_ball2.illu_ball_xbtm >= self.block.block_x1 and \
                    self.illu_ball2.illu_ball_xbtm <= self.block.block_x2 and \
                    self.illu_ball2.illu_ball_ybtm < self.block.block_y2 and \
                    self.illu_ball2.illu_ball_ybtm > self.block.block_y1:
                pygame.mixer.Channel(1).play(self.hit_block)
                self.illu2_move_down = False
                self.illu2_move_up = True
                if self.block_move_left:
                    self.illu2_move_left = True
                if self.block_move_right:
                    self.illu2_move_left = False
                    self.illu2_move_right = True

            if self.illu_ball3.illu_ball_xbtm >= self.block.block_x1 and \
                    self.illu_ball3.illu_ball_xbtm <= self.block.block_x2 and \
                    self.illu_ball3.illu_ball_ybtm < self.block.block_y2 and \
                    self.illu_ball3.illu_ball_ybtm > self.block.block_y1:
                pygame.mixer.Channel(1).play(self.hit_block)
                self.illu3_move_down = False
                self.illu3_move_up = True
                if self.block_move_left:
                    self.illu3_move_left = True
                if self.block_move_right:
                    self.illu3_move_left = False
                    self.illu3_move_right = True

            if self.power_ball.power_ball_xbtm >= self.block.block_x1 and \
                    self.power_ball.power_ball_xbtm <= self.block.block_x2 and \
                    self.power_ball.power_ball_ybtm < self.block.block_y2 and \
                    self.power_ball.power_ball_ybtm > self.block.block_y1:
                pygame.mixer.Channel(4).play(self.charge_sound)
                self.power_gain = True
                self.add_x = 100


            ##############################   ball hit enermies   ##############################
            if self.win_sound_start and not self.win_sound_end:
                pygame.mixer.Channel(6).play(self.win_sound)
                self.win_sound_end = True
                self.win_sound_start = False
            if self.endgame:
                break
            if self.hit_count == 0:
                self.win_sound_start = True
                self.move_up = False
                self.move_down = False
                self.move_left = False
                self.move_right = False
                self.illu1_move_up = False
                self.illu1_move_down = False
                self.illu1_move_left = False
                self.illu1_move_right = False
                self.illu2_move_up = False
                self.illu2_move_down = False
                self.illu2_move_left = False
                self.illu2_move_right = False
                self.illu3_move_up = False
                self.illu3_move_down = False
                self.illu3_move_left = False
                self.illu3_move_right = False
                self.game_start = False
                sign.draw_win(self)
                self.stop = True
                self.endgame = True

            for i in range(80):
                if self.ball.ball_xtop >= self.enermy.enermies_x1[i] and \
                        self.ball.ball_xtop <= self.enermy.enermies_x2[i] and \
                        self.ball.ball_ytop >= self.enermy.enermies_y1[i] and \
                        self.ball.ball_ytop <= self.enermy.enermies_y2[i]:
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)
                    if not self.power_gain:
                        self.move_up = False
                        self.move_down = True
                    if self.power_gain:
                        self.power_hit = True
            for i in range(80):
                if self.ball.ball_xleft >= self.enermy.enermies_x1[i] and \
                        self.ball.ball_xleft <= self.enermy.enermies_x2[i] and \
                        self.ball.ball_yleft >= self.enermy.enermies_y1[i] and \
                        self.ball.ball_yleft <= self.enermy.enermies_y2[i]:
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)
                    if not self.power_gain:
                        self.move_left = False
                        self.move_right = True
                    if self.power_gain:
                        self.power_hit = True
            for i in range(80):
                if self.ball.ball_xright >= self.enermy.enermies_x1[i] and \
                        self.ball.ball_xright <= self.enermy.enermies_x2[i] and \
                        self.ball.ball_yright >= self.enermy.enermies_y1[i] and \
                        self.ball.ball_yright <= self.enermy.enermies_y2[i]:
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)
                    if not self.power_gain:
                        self.move_right = False
                        self.move_left = True
                    if self.power_gain:
                        self.power_hit = True
            for i in range(80):
                if self.ball.ball_xbtm >= self.enermy.enermies_x1[i] and \
                        self.ball.ball_xbtm <= self.enermy.enermies_x2[i] and \
                        self.ball.ball_ybtm >= self.enermy.enermies_y1[i] and \
                        self.ball.ball_ybtm <= self.enermy.enermies_y2[i]:
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)
                    if not self.power_gain:
                        self.move_down = False
                        self.move_up = True
                    if self.power_gain:
                        self.power_hit = True

            for i in range(80):
                if self.illu_ball1.illu_ball_xtop >= self.enermy.enermies_x1[i] and \
                        self.illu_ball1.illu_ball_xtop <= self.enermy.enermies_x2[i] and \
                        self.illu_ball1.illu_ball_ytop >= self.enermy.enermies_y1[i] and \
                        self.illu_ball1.illu_ball_ytop <= self.enermy.enermies_y2[i]:
                    self.illu1_move_up = False
                    self.illu1_move_down = True
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)
            for i in range(80):
                if self.illu_ball1.illu_ball_xleft >= self.enermy.enermies_x1[i] and \
                        self.illu_ball1.illu_ball_xleft <= self.enermy.enermies_x2[i] and \
                        self.illu_ball1.illu_ball_yleft >= self.enermy.enermies_y1[i] and \
                        self.illu_ball1.illu_ball_yleft <= self.enermy.enermies_y2[i]:
                    self.illu1_move_left = False
                    self.illu1_move_right = True
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)
            for i in range(80):
                if self.illu_ball1.illu_ball_xright >= self.enermy.enermies_x1[i] and \
                        self.illu_ball1.illu_ball_xright <= self.enermy.enermies_x2[i] and \
                        self.illu_ball1.illu_ball_yright >= self.enermy.enermies_y1[i] and \
                        self.illu_ball1.illu_ball_yright <= self.enermy.enermies_y2[i]:
                    self.illu1_move_right = False
                    self.illu1_move_left = True
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)
            for i in range(80):
                if self.illu_ball1.illu_ball_xbtm >= self.enermy.enermies_x1[i] and \
                        self.illu_ball1.illu_ball_xbtm <= self.enermy.enermies_x2[i] and \
                        self.illu_ball1.illu_ball_ybtm >= self.enermy.enermies_y1[i] and \
                        self.illu_ball1.illu_ball_ybtm <= self.enermy.enermies_y2[i]:
                    self.illu1_move_down = False
                    self.illu1_move_up = True
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)

            for i in range(80):
                if self.illu_ball2.illu_ball_xtop >= self.enermy.enermies_x1[i] and \
                        self.illu_ball2.illu_ball_xtop <= self.enermy.enermies_x2[i] and \
                        self.illu_ball2.illu_ball_ytop >= self.enermy.enermies_y1[i] and \
                        self.illu_ball2.illu_ball_ytop <= self.enermy.enermies_y2[i]:
                    self.illu2_move_up = False
                    self.illu2_move_down = True
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)
            for i in range(80):
                if self.illu_ball2.illu_ball_xleft >= self.enermy.enermies_x1[i] and \
                        self.illu_ball2.illu_ball_xleft <= self.enermy.enermies_x2[i] and \
                        self.illu_ball2.illu_ball_yleft >= self.enermy.enermies_y1[i] and \
                        self.illu_ball2.illu_ball_yleft <= self.enermy.enermies_y2[i]:
                    self.illu2_move_left = False
                    self.illu2_move_right = True
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)
            for i in range(80):
                if self.illu_ball2.illu_ball_xright >= self.enermy.enermies_x1[i] and \
                        self.illu_ball2.illu_ball_xright <= self.enermy.enermies_x2[i] and \
                        self.illu_ball2.illu_ball_yright >= self.enermy.enermies_y1[i] and \
                        self.illu_ball2.illu_ball_yright <= self.enermy.enermies_y2[i]:
                    self.illu2_move_right = False
                    self.illu2_move_left = True
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)
            for i in range(80):
                if self.illu_ball2.illu_ball_xbtm >= self.enermy.enermies_x1[i] and \
                        self.illu_ball2.illu_ball_xbtm <= self.enermy.enermies_x2[i] and \
                        self.illu_ball2.illu_ball_ybtm >= self.enermy.enermies_y1[i] and \
                        self.illu_ball2.illu_ball_ybtm <= self.enermy.enermies_y2[i]:
                    self.illu2_move_down = False
                    self.illu2_move_up = True
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)

            for i in range(80):
                if self.illu_ball3.illu_ball_xtop >= self.enermy.enermies_x1[i] and \
                        self.illu_ball3.illu_ball_xtop <= self.enermy.enermies_x2[i] and \
                        self.illu_ball3.illu_ball_ytop >= self.enermy.enermies_y1[i] and \
                        self.illu_ball3.illu_ball_ytop <= self.enermy.enermies_y2[i]:
                    self.illu3_move_up = False
                    self.illu3_move_down = True
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)
            for i in range(80):
                if self.illu_ball3.illu_ball_xleft >= self.enermy.enermies_x1[i] and \
                        self.illu_ball3.illu_ball_xleft <= self.enermy.enermies_x2[i] and \
                        self.illu_ball3.illu_ball_yleft >= self.enermy.enermies_y1[i] and \
                        self.illu_ball3.illu_ball_yleft <= self.enermy.enermies_y2[i]:
                    self.illu3_move_left = False
                    self.illu3_move_right = True
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)
            for i in range(80):
                if self.illu_ball3.illu_ball_xright >= self.enermy.enermies_x1[i] and \
                        self.illu_ball3.illu_ball_xright <= self.enermy.enermies_x2[i] and \
                        self.illu_ball3.illu_ball_yright >= self.enermy.enermies_y1[i] and \
                        self.illu_ball3.illu_ball_yright <= self.enermy.enermies_y2[i]:
                    self.illu3_move_right = False
                    self.illu3_move_left = True
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)
            for i in range(80):
                if self.illu_ball3.illu_ball_xbtm >= self.enermy.enermies_x1[i] and \
                        self.illu_ball3.illu_ball_xbtm <= self.enermy.enermies_x2[i] and \
                        self.illu_ball3.illu_ball_ybtm >= self.enermy.enermies_y1[i] and \
                        self.illu_ball3.illu_ball_ybtm <= self.enermy.enermies_y2[i]:
                    self.illu3_move_down = False
                    self.illu3_move_up = True
                    self.enermy.enermies_x1[i] = self.enermy.enermies_x1[i] + 100
                    self.enermy.enermies_x2[i] = self.enermy.enermies_x2[i] + 100
                    self.hit += 1
                    self.hit_count -= 1
                    pygame.mixer.Channel(2).play(self.hit_enermy)

            ##############################    add skill    ##############################
            if self.hit == 10 and not self.illu_sound_end:
                self.illu_sound_start = True
            if self.hit >= 10:
                self.illu_ball1.draw_illu(self.draw1)
                self.illu1_move_down = True
            if self.hit == 11:
                self.illu_sound_end = False

            if self.hit == 20 and not self.illu_sound_end:
                self.illu_sound_start = True
            if self.hit >= 20:
                self.illu_ball2.draw_illu(self.draw2)
                self.illu2_move_down = True
            if self.hit == 21:
                self.illu_sound_end = False

            if self.hit == 30 and not self.illu_sound_end:
                self.illu_sound_start = True
            if self.hit >= 30:
                self.illu_ball3.draw_illu(self.draw3)
                self.illu3_move_down = True
            if self.hit == 31:
                self.illu_sound_end = False

            if self.hit == 40 and not self.illu_sound_end:
                self.illu_sound_start = True
            if self.hit >= 40:
                self.power_ball.draw_power(self.add_x)
                self.power_move_down = True
            if self.hit == 41:
                self.illu_sound_end = False

            if self.illu_sound_start:
                pygame.mixer.Channel(3).play(self.illusion_sound)
                self.illu_sound_start = False
                self.illu_sound_end = True

            pygame.display.flip()
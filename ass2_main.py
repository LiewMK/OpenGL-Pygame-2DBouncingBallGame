import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ass2_easy import *
from ass2_normal import *
from ass2_hard import *

class main_menu:
    pygame.mixer.init()
    pygame.mixer.music.load((os.path.join('menu_music.wav')))
    pygame.mixer.music.play(-1)
    def __init__(self):
        self.easy = easy()
        self.normal = normal()
        self.hard = hard()
        self.click = 0
        self.arrow_y = 0
        self.decision = 0
        self.run = True
        self.info_win = False
        self.easy_win = False
        self.run_easy_game = True
        self.run_normal_game = True
        self.run_hard_game = True

    def bg(self):
        glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        textureSurface = pygame.image.load((os.path.join('bouncingball_mainmenu.png')))
        textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
        width = textureSurface.get_width()
        height = textureSurface.get_height()
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, glGenTextures(1))
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    def bg_rect(self):
        if not self.info_win:
            self.bg()
            glBegin(GL_QUADS)
            glTexCoord2f(0, 0)
            glVertex3f(-7.7, -5.75, 0)
            glTexCoord2f(1, 0)
            glVertex3f(7.7, -5.75, 0)
            glTexCoord2f(1, 1)
            glVertex3f(7.7, 5.75, 0)
            glTexCoord2f(0, 1)
            glVertex3f(-7.7, 5.75, 0)
            glEnd()
            glDeleteTextures(1)

    def info(self):
        glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        textureSurface = pygame.image.load((os.path.join('bouncingball_info.png')))
        textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
        width = textureSurface.get_width()
        height = textureSurface.get_height()
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, glGenTextures(1))
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    def info_rect(self):
        self.info()
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-7.7, -5.75, 0)
        glTexCoord2f(1, 0)
        glVertex3f(7.7, -5.75, 0)
        glTexCoord2f(1, 1)
        glVertex3f(7.7, 5.75, 0)
        glTexCoord2f(0, 1)
        glVertex3f(-7.7, 5.75, 0)
        glEnd()
        glDeleteTextures(1)

    def arrow(self):
        if not self.info_win:
            glBegin(GL_TRIANGLES)
            glColor3f(0.6, 0, 0)
            glVertex3f(1.77, 0.3 + self.arrow_y, 5)
            glVertex3f(1.77, 0.6 + self.arrow_y, 5)
            glVertex3f(2.04, 0.45 + self.arrow_y, 5)
            glEnd()

    def RUN(self):
        pygame.init()
        glutInit(sys.argv)
        display = (800, 600)
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        pygame.display.set_caption('Bouncing Ball')
        glViewport(0, 0, display[0], display[1])
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, (display[0] / display[1]), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0, 0, -10)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_DOWN and self.click < 4 and not self.info_win and not self.easy_win:
                        self.arrow_y -= 0.75
                        self.click += 1
                    if event.key == K_UP and self.click > 0 and not self.info_win and not self.easy_win:
                        self.arrow_y += 0.75
                        self.click -= 1
                    if event.key == K_RETURN and self.click == 0:
                        self.info_win = True
                    if event.key == K_ESCAPE and self.info_win:
                        self.info_win = False
                    if event.key == K_RETURN and self.click == 1:
                        self.easy.restart()
                        self.run_easy_game = True
                        self.easygame()
                    if event.key == K_RETURN and self.click == 2:
                        self.normal.restart()
                        self.run_normal_game = True
                        self.normalgame()
                    if event.key == K_RETURN and self.click == 3:
                        self.hard.restart()
                        self.run_hard_game = True
                        self.hardgame()
                    if event.key == K_RETURN and self.click == 4:
                        pygame.quit()
                        quit()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.info_rect()
            self.bg_rect()
            self.arrow()

            pygame.display.flip()

    def easygame(self):
        while self.run_easy_game:
            pygame.mixer.music.load((os.path.join('easy_music.wav')))
            pygame.mixer.music.play(-1)
            glPushMatrix()
            glTranslatef(0, 0, 2.8)
            self.easy.RUN()
            glPopMatrix()
            self.decision = self.easy.decision
            if self.decision == 1:
                self.run_easy_game = False
                pygame.mixer.music.load((os.path.join('menu_music.wav')))
                pygame.mixer.music.play(-1)
            if self.decision == 2:
                self.easy.restart()


    def normalgame(self):
        while self.run_normal_game:
            pygame.mixer.music.load((os.path.join('normal_music.wav')))
            pygame.mixer.music.play(-1)
            glPushMatrix()
            glTranslatef(0, 0, 2.8)
            self.normal.RUN()
            glPopMatrix()
            self.decision = self.normal.decision
            if self.decision == 1:
                self.run_normal_game = False
                pygame.mixer.music.load((os.path.join('menu_music.wav')))
                pygame.mixer.music.play(-1)
            if self.decision == 2:
                self.normal.restart()

    def hardgame(self):
        while self.run_hard_game:
            pygame.mixer.music.load((os.path.join('hard_music.wav')))
            pygame.mixer.music.play(-1)
            glPushMatrix()
            glTranslatef(0, 0, 2.8)
            self.hard.RUN()
            glPopMatrix()
            self.decision = self.hard.decision
            if self.decision == 1:
                self.run_hard_game = False
                pygame.mixer.music.load((os.path.join('menu_music.wav')))
                pygame.mixer.music.play(-1)
            if self.decision == 2:
                self.hard.restart()

if __name__ == "__main__":
    main_menu().RUN()
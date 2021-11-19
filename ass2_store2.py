from OpenGL.GL import *
import random

#############################################   block   #############################################
class BLOCK:
    def __init__(self,  mode):
        self.block_x1 = 0
        self.block_x2 = 0
        self.block_y1 = 0
        self.block_y2 = 0
        self.block_x = 0
        self.mode = mode

    def draw(self):
        if self.mode == 1:
            self.block_x1 = 0.8 + self.block_x
            self.block_x2 = 2.4 + self.block_x
        if self.mode == 2:
            self.block_x1 = 0.9 + self.block_x
            self.block_x2 = 2.3 + self.block_x
        if self.mode == 3:
            self.block_x1 = 1.0 + self.block_x
            self.block_x2 = 2.2 + self.block_x
        self.block_y1 = -3.5
        self.block_y2 = -3.28

        glBegin(GL_QUADS)
        glColor(1, 0.6, 0.2)
        glVertex2f(self.block_x1, self.block_y1)
        glColor(1, 0.6, 0.2)
        glVertex2f(self.block_x2, self.block_y1)
        glColor(1, 1, 0.6)
        glVertex2f(self.block_x2, self.block_y2)
        glColor(1, 1, 0.6)
        glVertex2f(self.block_x1, self.block_y2)
        glEnd()

        glBegin(GL_QUADS)
        glColor(0.8, 0, 0)
        glVertex2f(self.block_x1, self.block_y1)
        glColor(0.8, 0, 0)
        glVertex2f(self.block_x1 + 0.2, self.block_y1)
        glColor(0.8, 0, 0)
        glVertex2f(self.block_x1 + 0.2, self.block_y2)
        glColor(0.8, 0, 0)
        glVertex2f(self.block_x1, self.block_y2)
        glEnd()

        glBegin(GL_QUADS)
        glColor(0.8, 0, 0)
        glVertex2f(self.block_x2 - 0.2, self.block_y1)
        glColor(0.8, 0, 0)
        glVertex2f(self.block_x2, self.block_y1)
        glColor(0.8, 0, 0)
        glVertex2f(self.block_x2, self.block_y2)
        glColor(0.8, 0, 0)
        glVertex2f(self.block_x2 - 0.2, self.block_y2)
        glEnd()

        glColor(0, 0, 0)
        glBegin(GL_LINES)
        glVertex2f(self.block_x1, self.block_y1)
        glVertex2f(self.block_x2, self.block_y1)
        glVertex2f(self.block_x2, self.block_y1)
        glVertex2f(self.block_x2, self.block_y2)
        glVertex2f(self.block_x2, self.block_y2)
        glVertex2f(self.block_x1, self.block_y2)
        glVertex2f(self.block_x1, self.block_y2)
        glVertex2f(self.block_x1, self.block_y1)
        glEnd()

        glColor(0, 0, 0)
        glBegin(GL_LINES)
        glVertex2f(self.block_x1 + 0.2, self.block_y1)
        glVertex2f(self.block_x1 + 0.2, self.block_y2)
        glEnd()

        glColor(0, 0, 0)
        glBegin(GL_LINES)
        glVertex2f(self.block_x2 - 0.2, self.block_y2)
        glVertex2f(self.block_x2 - 0.2, self.block_y1)
        glEnd()


#############################################   enermy   #############################################
class enermies:
    def __init__(self, mode):
        self.enermy_x1 = -1.7
        self.enermy_x2 = -1.05
        self.enermy_y1 = 3.6
        self.enermy_y2 = 3.9
        self.enermies_x1 = []
        self.enermies_x2 = []
        self.enermies_y1 = []
        self.enermies_y2 = []
        self.random = []
        self.mode = mode

    def draw(self):
        if self.mode == 1:
            for j in range(6):
                for i in range(10):
                    if len(self.enermies_x1) < 60:
                        self.enermies_x1.append(self.enermy_x1 + 0.7 * i)
                    if len(self.enermies_x2) < 60:
                        self.enermies_x2.append(self.enermy_x2 + 0.7 * i)
                    if len(self.enermies_y1) < 60:
                        self.enermies_y1.append(self.enermy_y1 - 0.35 * j)
                    if len(self.enermies_y2) < 60:
                        self.enermies_y2.append(self.enermy_y2 - 0.35 * j)
            rand = (random.randint(0, 5))
            if len(self.random) < 60:
                self.random.append(rand)

        if self.mode == 2:
            for j in range(8):
                for i in range(10):
                    if len(self.enermies_x1) < 80:
                        self.enermies_x1.append(self.enermy_x1 + 0.7 * i)
                    if len(self.enermies_x2) < 80:
                        self.enermies_x2.append(self.enermy_x2 + 0.7 * i)
                    if len(self.enermies_y1) < 80:
                        self.enermies_y1.append(self.enermy_y1 - 0.35 * j)
                    if len(self.enermies_y2) < 80:
                        self.enermies_y2.append(self.enermy_y2 - 0.35 * j)
            rand = (random.randint(0, 5))
            if len(self.random) < 80:
                self.random.append(rand)

        for i in range(len(self.random)):
            if self.random[i] == 0:
                glBegin(GL_QUADS)
                glColor(0, 1, 1)
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glColor(0, 1, 1)
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glColor(1, 1, 1)
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glColor(1, 1, 1)
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glEnd()
                glColor(0, 0, 0)
                glBegin(GL_LINES)
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glEnd()

            if self.random[i] == 1:
                glBegin(GL_QUADS)
                glColor(0.498, 0, 1)
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glColor(0.498, 0, 1)
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glColor(1, 1, 1)
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glColor(1, 1, 1)
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glEnd()
                glColor(0, 0, 0)
                glBegin(GL_LINES)
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glEnd()

            if self.random[i] == 2:
                glBegin(GL_QUADS)
                glColor(0, 0.8, 0.4)
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glColor(0, 0.8, 0.4)
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glColor(1, 1, 1)
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glColor(1, 1, 1)
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glEnd()

                glColor(0, 0, 0)
                glBegin(GL_LINES)
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glEnd()

            if self.random[i] == 3:
                glBegin(GL_QUADS)
                glColor(0.8, 0.8, 0)
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glColor(0.8, 0.8, 0)
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glColor(1, 1, 1)
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glColor(1, 1, 1)
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glEnd()
                glColor(0, 0, 0)
                glBegin(GL_LINES)
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glEnd()

            if self.random[i] == 4:
                glBegin(GL_QUADS)
                glColor(0.8, 0, 0.4)
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glColor(0.8, 0, 0.4)
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glColor(1, 1, 1)
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glColor(1, 1, 1)
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glEnd()
                glColor(0, 0, 0)
                glBegin(GL_LINES)
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glEnd()

            if self.random[i] == 5:
                glBegin(GL_QUADS)
                glColor(0.8, 0, 0.8)
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glColor(0.8, 0, 0.8)
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glColor(1, 1, 1)
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glColor(1, 1, 1)
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glEnd()
                glColor(0, 0, 0)
                glBegin(GL_LINES)
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y1[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x2[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y2[i])
                glVertex2f(self.enermies_x1[i], self.enermies_y1[i])
                glEnd()
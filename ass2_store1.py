from OpenGL.GL import *
from OpenGL.GLUT import *

#############################################   board   #############################################
class board:
    def score_board(self):
        glBegin(GL_QUADS)
        glColor(0, 0.4, 0.4)
        glVertex2f(-5.6, -4.5)
        glColor(0, 0.4, 0.4)
        glVertex2f(-2, -4.5)
        glColor(0, 0.4, 0.4)
        glVertex2f(-2, 4.5)
        glColor(0, 0.4, 0.4)
        glVertex2f(-5.6, 4.5)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0, 0, 0.4)
        glVertex2f(-5.4, -4)
        glColor(0, 0, 0.4)
        glVertex2f(-2.125, -4)
        glColor(0, 0, 0.4)
        glVertex2f(-2.125, 4)
        glColor(0.564, 0, 1)
        glVertex2f(-5.4, 4)
        glEnd()

    def game_board(self):
        x1 = -2
        x2 = -1.2
        y1 = -5
        y2 = -4.6
        x11 = -2.4
        x22 = -1.6
        y11 = -4.6
        y22 = -4.2
        for j in range(12):
            for i in range(10):
                glBegin(GL_QUADS)
                glColor(0.4, 0.2, 0)
                glVertex2f(x1 + 0.8 * i, y1 + 0.8 * j)
                glColor(0.4, 0.2, 0)
                glVertex2f(x2 + 0.8 * i, y1 + 0.8 * j)
                glColor(0.4, 0.2, 0)
                glVertex2f(x2 + 0.8 * i, y2 + 0.8 * j)
                glColor(1, 0.6, 0.2)
                glVertex2f(x1 + 0.8 * i, y2 + 0.8 * j)
                glEnd()
        for j in range(12):
            for i in range(10):
                glBegin(GL_QUADS)
                glColor(0.4, 0.2, 0)
                glVertex2f(x11 + 0.8 * i, y11 + 0.8 * j)
                glColor(0.4, 0.2, 0)
                glVertex2f(x22 + 0.8 * i, y11 + 0.8 * j)
                glColor(0.4, 0.2, 0)
                glVertex2f(x22 + 0.8 * i, y22 + 0.8 * j)
                glColor(1, 0.6, 0.2)
                glVertex2f(x11 + 0.8 * i, y22 + 0.8 * j)
                glEnd()
        for j in range(12):
            for i in range(10):
                glBegin(GL_LINES)
                glColor(0, 0, 0)
                glVertex2f(x1 + 0.8 * i, y1 + 0.8 * j)
                glVertex2f(x2 + 0.8 * i, y1 + 0.8 * j)
                glVertex2f(x2 + 0.8 * i, y1 + 0.8 * j)
                glVertex2f(x2 + 0.8 * i, y2 + 0.8 * j)
                glVertex2f(x2 + 0.8 * i, y2 + 0.8 * j)
                glVertex2f(x1 + 0.8 * i, y2 + 0.8 * j)
                glVertex2f(x1 + 0.8 * i, y2 + 0.8 * j)
                glVertex2f(x1 + 0.8 * i, y1 + 0.8 * j)
                glEnd()
        for j in range(12):
            for i in range(10):
                glBegin(GL_LINES)
                glColor(0, 0, 0)
                glVertex2f(x11 + 0.8 * i, y11 + 0.8 * j)
                glVertex2f(x22 + 0.8 * i, y11 + 0.8 * j)
                glVertex2f(x22 + 0.8 * i, y11 + 0.8 * j)
                glVertex2f(x22 + 0.8 * i, y22 + 0.8 * j)
                glVertex2f(x22 + 0.8 * i, y22 + 0.8 * j)
                glVertex2f(x11 + 0.8 * i, y22 + 0.8 * j)
                glVertex2f(x11 + 0.8 * i, y22 + 0.8 * j)
                glVertex2f(x11 + 0.8 * i, y11 + 0.8 * j)
                glEnd()

        glBegin(GL_QUADS)
        glColor(0, 0, 0)
        glVertex2f(-2, -4.5)
        glColor(0, 0, 0)
        glVertex2f(-1.85, -4.5)
        glColor(0, 0, 0)
        glVertex2f(-1.85, 4.5)
        glColor(0, 0, 0)
        glVertex2f(-2, 4.5)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0, 0, 0)
        glVertex2f(5.38, -4.5)
        glColor(0, 0, 0)
        glVertex2f(5.6, -4.5)
        glColor(0, 0, 0)
        glVertex2f(5.6, 4.5)
        glColor(0, 0, 0)
        glVertex2f(5.38, 4.5)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0, 0, 0)
        glVertex2f(-2, -4.5)
        glColor(0, 0, 0)
        glVertex2f(5.6, -4.5)
        glColor(0, 0, 0)
        glVertex2f(5.6, -4)
        glColor(0, 0, 0)
        glVertex2f(-2, -4)
        glEnd()
        glBegin(GL_QUADS)
        glColor(0, 0, 0)
        glVertex2f(-2, 4)
        glColor(0, 0, 0)
        glVertex2f(5.6, 4)
        glColor(0, 0, 0)
        glVertex2f(5.6, 4.5)
        glColor(0, 0, 0)
        glVertex2f(-2, 4.5)
        glEnd()


#############################################   word   #############################################
class word:
    def word(self, mode, hit_count):
        self.hit_count = hit_count
        glColor(1, 1, 0.2)
        glRasterPos(-4.53, 3.44)
        glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'- MODE -')
        if mode == 1:
            glColor(1, 1, 1)
            glRasterPos(-4.18, 2.92)
            glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'EASY')
        if mode == 2:
            glColor(1, 1, 1)
            glRasterPos(-4.43, 2.92)
            glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'NORMAL')
        if mode == 3:
            glColor(1, 1, 1)
            glRasterPos(-4.18, 2.92)
            glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'HARD')
        glColor(1, 1, 0.2)
        glRasterPos(-5, 2.14)
        glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'- BALL SPEED -')
        if mode == 1:
            glColor(1, 1, 1)
            glRasterPos(-4, 1.62)
            glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'0.02')
        if mode == 2:
            glColor(1, 1, 1)
            glRasterPos(-4, 1.62)
            glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'0.04')
        if mode == 3:
            glColor(1, 1, 1)
            glRasterPos(-4, 1.62)
            glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'0.05')
        glColor(1, 1, 0.2)
        glRasterPos(-5.32, 0.84)
        glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'- PLANK LENGTH -')
        if mode == 1:
            glColor(1, 1, 1)
            glRasterPos(-3.95, 0.32)
            glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'2.0')
        if mode == 2:
            glColor(1, 1, 1)
            glRasterPos(-3.95, 0.32)
            glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'1.8')
        if mode == 3:
            glColor(1, 1, 1)
            glRasterPos(-3.94, 0.32)
            glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'1.6')
        glColor(1, 1, 0.2)
        glRasterPos(-5, -0.54)
        glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'- BLOCK LEFT -')
        score = str(self.hit_count)
        glColor(1, 1, 1)
        glRasterPos(-3.9, -1.06)
        for i in range(len(score)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(score[i]))
        glColor(1, 1, 0.2)
        glRasterPos(-5.3, -1.95)
        glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'Functions')
        glColor(1, 1, 0.2)
        glRasterPos(-5.3, -1.97)
        glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'________')
        glColor(1, 1, 0.2)
        glRasterPos(-5.3, -2.4)
        glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'START   :  space')
        glColor(1, 1, 0.2)
        glRasterPos(-5.3, -2.8)
        glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'BLOCK  :  left / right')
        glColor(1, 1, 0.2)
        glRasterPos(-5.3, -3.2)
        glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'BACK     :  esc')
        glColor(1, 1, 0.2)
        glRasterPos(-5.3, -3.6)
        glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, b'RESTART  :  enter')

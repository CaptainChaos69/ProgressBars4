from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
from direct.gui.DirectGui import *

confVars = """
window-title Progress Bars
"""

loadPrcFileData("", confVars)

class Bars(ShowBase):
    def __init__(self, am):
        self.am = am
        super().__init__()

        self.v1 = am[0]
        self.r1 = am[1]
        self.v2 = am[2]
        self.r2 = am[3]
        self.v3 = am[4]
        self.r3 = am[5]

        self.bar1 = DirectWaitBar(text=str(self.v1) + " / " + str(self.r1), range=self.r1, value=self.v1, pos=(0, .4, .4), scale=1)

        self.bar2 = DirectWaitBar(text=str(self.v2) + " / " + str(self.r2), range=self.r2, value=self.v2, pos=(0, .4, .1), scale=1)

        self.bar3 = DirectWaitBar(text=str(self.v3) + " / " + str(self.r3), range=self.r3, value=self.v3, pos=(0, .4, -.2), scale=1)

        while self.v1 <= self.r1:
            self.bar1 = DirectWaitBar(text=str(self.v1) + " / " + str(self.r1), range=self.r1, value=self.v1, pos=(0, .4, .4), scale=1)
            self.v1 += 1

        while self.v2 <= self.r2:
            self.bar2 = DirectWaitBar(text=str(self.v2) + " / " + str(self.r2), range=self.r2, value=self.v2, pos=(0, .4, .1), scale=1)
            self.v2 += 1

        while self.v3 <= self.r3:
            self.bar3 = DirectWaitBar(text=str(self.v3) + " / " + str(self.r3), range=self.r3, value=self.v3, pos=(0, .4, -0.2), scale=1)
            self.v3 += 1

def endApp():
    game.finalizeExit()

b = DirectButton(text=("Stop Animation"), scale=.05, command=endApp, pos=(0, 0, -0.8))

game = Bars([0, 1000, 200, 400, 450, 550])
game.run()

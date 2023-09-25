from panda3d.core import loadPrcFile

loadPrcFile("configure.prc")
from direct.showbase.DirectObject import DirectObject
from direct.showbase.ShowBase import ShowBase 

from direct.gui.DirectGui import (
 DirectFrame,
 DirectLabel,
 DirectButton)

class screen(DirectObject):
     def __init__(self):
       self.frameMain = DirectFrame(
       frameColor = (0, 0, 0, 0.75))
       self.frameMain.setTransparency(1)
       self.lbl_KO = DirectLabel(
         text = "Crazy Mine",
         text_fg = (1,1,1,1),
         scale = 1,
         pos = (0, 0, 0),
         frameColor = (0,0,0,0))

       self.lbl_KO.setTransparency(1)
       self.lbl_KO.reparentTo(self.frameMain)
      
       self.btnContinue = DirectButton(
        text = "CONTINUE",
        text_fg = (1,1,1,1),
        scale = 0.1,
        pad = (0.15, 0.15),
        pos = (0, 0, -0.8),
        frameColor = (
          (0.2,0.2,0.2,0.8),
          (0.4,0.4,0.4,0.8),
          (0.4,0.4,0.4,0.8),
          (0.1,0.1,0.1,0.8),
            ),
        relief = 1,
        extraArgs = ["KoScreen-Back"],
        pressEffect = False,
        rolloverSound = None,
        clickSound = None)
       self.btnContinue.setTransparency(1)
       self.btnContinue.reparentTo(self.frameMain)
       self.hide()
   
     def hide(self):
       self.frameMain.hide()


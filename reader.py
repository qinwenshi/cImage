from cImage import *

class BreakIt(Exception): pass

win = ImageWin("My Window",800,640)
oImage = FileImage('cattt.gif')
print(oImage.getWidth(), oImage.getHeight())
oImage.draw(win)
myImage = oImage.copy()
#code = msg.encode('base64','strict')
msg = ""

def read() :
    msg = ""
    for row in range(myImage.getHeight()):
        for col in range(myImage.getWidth()):
            v = myImage.getPixel(col,row)

            if v.red == 0 and v.green == 0 and v.blue == 0: 
                return msg
            elif v.red == 255 and v.green == 255 and v.blue == 255:
                msg = ""
            else: 
                char = chr(v.red)
                msg = msg + char
print read()
myImage.setPosition(myImage.getWidth()+1,0)
myImage.draw(win)
print(win.getMouse())
#print(myImage.toList())
win.exitOnClick()

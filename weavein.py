from cImage import *

win = ImageWin("My Window",800,640)
oImage = FileImage('cat.gif')
print(oImage.getWidth(), oImage.getHeight())
oImage.draw(win)
myImage = oImage.copy()
msg = "This is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an imageThis is an image"
#code = msg.encode('base64','strict')

index = -1

for row in range(myImage.getHeight()):
    for col in range(myImage.getWidth()):
        v = myImage.getPixel(col,row)
        if  index <len(msg) and index >= 0:
            v.red = ord(msg[index])
            v.green = v.green
            v.blue = v.blue
            index = index + 1
        elif index == -1:
            v.red = 255
            v.greed = 255
            v.blue = 255
            index = index + 1
        elif index == len(msg):
            v.red = 0
            v.green = 0
            v.blue = 0
            index = index + 1            
        else:
            v.red = v.red
            v.green = v.green
            v.blue = v.blue
#       x = map(lambda x: 255-x, v)
        myImage.setPixel(col,row,v)
myImage.setPosition(myImage.getWidth()+1,0)
myImage.draw(win)
print(win.getMouse())
myImage.save('some.gif')
#print(myImage.toList())
win.exitOnClick()

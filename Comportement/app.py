import threading

class Camera():
    image = 1
    def __init__(self):
        self.te = 0
    def Start(self):
        while(True):
            self.image = self.image + 1


class ColorAquisition():
    def __init__(self,camera):
        self.camera = camera
    def Start(self):
        while(True):
            print self.camera.image

cam = Camera()
color = ColorAquisition(cam)
print("début") 
tcam = threading.Thread(target=cam.Start, args=())
tcolor = threading.Thread(target=color.Start)
tcam.start()
tcolor.start()
print("fin")



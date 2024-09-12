import ctypes
import os
def cw(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,
                                               0, image_path, 3)
class Zoro(object):
    def __init__(self):
        self.count=59
    def hchc(self):
        return 'Image{}.jpg'.format(self.count)
    def mainloop(self):
        cw(os.getcwd()+os.sep+'zoro'+os.sep+self.hchc())
        self.count+=1
        if self.count==2410:
            self.count=59
if __name__=='__main__':
    cls=Zoro()
    while True:
        cls.mainloop()

print('Loading...')
import ctypes
import os
import zipfile
import shutil
path=os.getcwd()+os.sep+'zoro'
try:
    shutil.rmtree(path)
except:
    pass
try:
    os.mkdir(path)
except:
    pass
lst=['part1.zip','part2.zip','part3.zip']
def uz(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
for i in lst:
    uz(i,path)
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
cls=Zoro()
input('Press "Enter" to run.')
print('Program is running.')
while True:
    cls.mainloop()
            

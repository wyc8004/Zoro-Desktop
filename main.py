print('Now program is loading')
import ctypes
import os
import zipfile
import shutil
def unzip_file(zip_path,extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
zip_file_path = os.getcwd()+os.sep+'zoro.zip'
try:
    shutil.rmtree(os.getcwd()+os.sep+'zoro')
    os.mkdir(os.getcwd()+os.sep+'zoro')
except:
    pass
extract_to_path = os.getcwd()
unzip_file(zip_file_path, extract_to_path)
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
input('Press enter to start run.')
cls=Zoro()
while True:
    cls.mainloop()
            

from PIL import Image
import os

fPath = 'imgs/original/'
fDistPath = 'imgs/resizing/'

fList = os.listdir(fPath)
fList.sort()


# img 비율 유지하여 resizing & save
def setResizeImg(basewidth=600, imgPath="", imgName=""):
    img = Image.open(imgPath+imgName)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img_resize = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img_resize.save(fDistPath+imgName+'_resizing.jpg')

for img in fList:
    setResizeImg(imgPath=fPath, imgName=img)




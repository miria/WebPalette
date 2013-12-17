import cv2.cv as cv
from PIL import Image

class SizeProcessor(object):

    def __init__(self, width, height):
        self._width = width
        self._height= height
        
    def process(self, image):
        if not image:
            return None
        (width, height) = image['dimensions']
        if width < self._width or height < self._height:
            print "Skipping "+image['image_id']+" : Invalid dimensions ("+str(width)+" x "+str(height)+")"
            return None
        center_width = width/2
        center_height = height/2
        #img = cv.LoadImage(image['path'], 1)
        #cropped = cv.CreateImage((self._width, self._height), 8, 3)
        # print "dimensions %d %d %d %d " % (center_width-(self._width/2), center_height-(self._height/2), center_width+(self._width/2), center_height+(self._height/2))
        #area = cv.GetSubRect(img, (center_width-(self._width/2), center_height-(self._height/2), center_width+(self._width/2), center_height+(self._height/2)))
        #cv.Copy(area, cropped)
        #cv.SaveImage(image['path'], cropped)
        img = Image.open(image['path'], 'r')
        cropped = img.crop((center_width-(self._width/2), center_height-(self._height/2), center_width+(self._width/2), center_height+(self._height/2)))
        cropped.save(image['path'])
        return image
    
    def cleanup(self):
        pass

from PIL import Image as PILImage
from PIL.ImageColor import getcolor


'''
Created on Dec 9, 2012

@author: miria
'''

class HeaderColorProcessor(object):
    '''
    Calculates the correct color overlay for text on an image.
    For example, if the image is dark, then return a light color and vice versa.
    '''


    def __init__(self, text_box):
        self._text_box = text_box
        
    def process(self, image):
        if not image:
            return None
        img = PILImage.open(image['path'], 'r')
        img = img.crop(self._text_box)
        colors = sorted(img.getcolors(img.size[0]*img.size[1]), reverse=True)
        sat_list = []
        for (_, color) in colors[:100]:
            sat_list.append(self.get_saturation(color))
        avg_sat = sum(sat_list)/100
        if (avg_sat < 100):
            image["header_color"] = image["light_color"]
        elif (avg_sat < 200):
            image["header_color"] = image["dark_color"]
        else:
            image["header_color"] = image["medium_color"]
        image["text_left"] = self._text_box[0]
        image["text_upper"] = self._text_box[1]
        image["text_right"] = self._text_box[2]
        image["text_lower"] = self._text_box[3]
        return image
    
    def cleanup(self):
        pass
            
    def get_saturation(self, rgb_tuple):
        try:
            return getcolor('rgb'+repr(rgb_tuple), 'L') 
        except:
            print "Bad tuple "+repr(rgb_tuple)
            return 51  
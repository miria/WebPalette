from PIL import Image as PILImage
from PIL.ImageColor import getcolor

class ColorProcessor(object):
    
    def process(self, image):
        if not image:
            return None
        (darks, mids, lights) = self.get_colors(image)
        if not darks or not mids or not lights:
            print "Skipping "+image['image_id']+" : Not enough color variance"
            return None
        image['light_color'] = self.get_web_color(lights[0])
        image['medium_color'] = self.get_web_color(mids[0])
        image['dark_color'] = self.get_web_color(darks[0])
        return image
    
    def cleanup(self):
        pass
    
    def get_colors(self, image):
        img = PILImage.open(image['path'], 'r')
        colors = sorted(img.getcolors(img.size[0]*img.size[1]), reverse=True)
        print colors
        dark = []
        medium = []
        light = []
        for (_, color) in colors:
            sat = self.get_saturation(color)
            if sat <= 50: dark.append(color)
            elif sat > 100 and sat < 150: medium.append(color)
            elif sat > 200: light.append(color)        
        return (dark,medium,light)

    def get_saturation(self, rgb_tuple):
        try:
            return getcolor('rgb'+repr(rgb_tuple), 'L') 
        except:
            print "Bad tuple "+repr(rgb_tuple)
            return 51   

    def get_web_color(self, rgb_tuple):
        return '#%02x%02x%02x' % rgb_tuple
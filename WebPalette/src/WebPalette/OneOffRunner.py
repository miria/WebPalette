import sys
from WebPalette.data.Image import Image
from WebPalette.config import Config
from PIL import Image as PILImage



class PaletteRunner(object):

    
    def __init__(self, config_path, *images):
        self.config_path = config_path
        self.image_list = images
        print self.image_list
        
    def run(self):
        self.config = Config.Config(self.config_path)
        image_id = 0
        for image in self.image_list:
            img = PILImage.open(image)
            print img.size
            img_obj = Image(image_id=image_id, path=image, width=img.size[0], height=img.size[1])
            
            for p in self.config.get_processors():
                image = p.process(img_obj)
                print img_obj
                        
        for p in self.config.get_processors():
            p.cleanup()

if __name__ == '__main__':
    print sys.argv
    palette = PaletteRunner(sys.argv[1], *sys.argv[2:])
    palette.run()
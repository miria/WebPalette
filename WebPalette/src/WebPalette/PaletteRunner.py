import sys
from WebPalette.config import Config

class PaletteRunner(object):

    
    def __init__(self, config_path):
        self.config_path = config_path
        
    def run(self):
        self.config = Config.Config(self.config_path)
        images = []
        for s in self.config.get_services():
            images += s.get_photos()
            print "Service %s downloaded %d images" % (s.get_name(), len(images))

        processed_images = []
        count = 0
        print "Beginning download"
        for image in images:
            
            for p in self.config.get_processors():
                image = p.process(image)
                print image
            
            
            if image:    
                processed_images.append(image)
            count += 1
            if count % 1 == 0:
                print "Processed %d" % count
            
        print "Post-process: %d images" % len(processed_images)
        
        for o in self.config.get_outputs():
            o.write_images(processed_images)
            print "Wrote %s" % repr(o)

        for p in self.config.get_processors():
            p.cleanup()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "WebPalette expects a path to a config file!"
        sys.exit(1)
    palette = PaletteRunner(sys.argv[1])
    palette.run()
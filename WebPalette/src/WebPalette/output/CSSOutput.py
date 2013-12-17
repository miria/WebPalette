import os
import shutil
from random import randint

ATTRIBUTION_SKELETON = """<html><head/><body>
        Image by <a href="%(url)s">%(attribution)s</a> via %(source)s
        </body></html>"""
        
CSS_SKELETON = """
        header {
            background-image:url('%(relative_url)s');
            
        }
        .header.text {
            position:absolute;
            top:$(text_u)spx; 
            left:$(text_l)spx;
            color: %(header_color)s;
            width:300px; 
        }
        .light {
            color: %(light_color)s;
        }
        .medium {
            color: %(medium_color)s;
        }
        .dark {
            color: %(dark_color)s;
        }
        """
        
class CSSOutput(object):
    def __init__(self, base_dir, img_count, domain_prefix=""):
        self._base_dir = base_dir
        self._img_count = img_count
        self._domain_prefix = domain_prefix
    
    def write_images(self, images):
        count = 0
        template_dir = os.path.join(self._base_dir, "web_palette")
        if not os.path.exists(template_dir):
            os.mkdir(template_dir)
        while images and count < self._img_count:
            idx = randint(0, len(images)-1)
            image = images.pop(idx)
            print image
            image_path = "image_%d.jpg" % count
            shutil.copy(image['path'], os.path.join(template_dir, image_path))
            fh = open(os.path.join(template_dir, "attribution_%d.html" % count), 'w')
            fh.write(ATTRIBUTION_SKELETON % image)
            fh.close()
            image['relative_url'] = self._domain_prefix+"web_palette/image_%d.jpg" % count
            fh = open(os.path.join(template_dir, "style_%d.css" % count), 'w')
            fh.write(CSS_SKELETON % image)
            fh.close()
            count += 1
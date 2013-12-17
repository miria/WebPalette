import os
import shutil
from urllib import urlretrieve

class DownloadProcessor(object):
    
    def __init__(self, base_path):
        self._base_path = base_path
        if not os.path.exists(base_path):
            os.mkdir(base_path)

    def process(self, image):
        if not image:
            return None
        file_path = os.path.join(self._base_path, "image_%s.jpg" % image['image_id'])
        image['path'] = file_path
        print "Fetching "+image['url']
        urlretrieve(image['url'], file_path)
        return image
        
    def cleanup(self):
        pass
        #shutil.rmtree(self._base_path)
        
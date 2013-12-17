from urllib2 import urlopen
from urllib import urlencode

#
# Providers abstract the actual fetching of the data from the classes
# to allow the service parsing to be mocked out better.
#
class HTTPProvider(object):

    def fetch_data(self, base_url, **kw):
        self.url = build_URL(base_url, kw)
        fh = urlopen(self.url)
        data = fh.read()
        fh.close()
        return data
    
    def get_URL(self):
        return self.url
    

class FileProvider(object):
    
    def __init__(self, file_path):
        self.file_path = file_path
        
    def fetch_data(self, base_url, **kw):
        self.url = build_URL(base_url, kw)
        fh = open(self.file_path, 'r')
        data = fh.read()
        fh.close()
        return data
    
    def get_URL(self):
        return self.url
    
def build_URL(base_url, kw):
    return base_url.rstrip("?")+"?"+urlencode(kw, True)
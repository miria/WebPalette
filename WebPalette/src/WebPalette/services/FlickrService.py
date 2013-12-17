from WebPalette.data.Image import Image
from WebPalette.services.Providers import HTTPProvider
import time
import json

BASE_URL = "http://api.flickr.com/services/rest/"
# TODO: Maybe instead of providers there is a generic service that looks at the url?
# downloads a file or uses http
class FlickrService(object):
    
    def get_name(self):
        return "FlickrService"
    
    def __init__(self, key=None, secret=None, album_id=None, provider=None, **_):
        self.api_key = key
        self.api_secret = secret
        self.album_id = album_id
        self.provider = provider
        print "Starting FlickrWeb with key "+key
        if not provider:
            self.provider = HTTPProvider()
        
        
    def get_interesting_photos(self, page=1, per_page=100):
        data = self.provider.fetch_data(BASE_URL, method="flickr.photos.search", per_page=per_page, 
                              page=page, extras="url_l,owner_name,license", license="1,2,3,4,5,6,7,8", 
                              safe_search=1, sort="interestingness-desc", format="json",
                              min_upload_date=int(time.time())-60*60*24, content_type=1,
                              api_key=self.api_key, nojsoncallback=1)
        data = json.loads(data)
        return self._process_flickr_images(data)

    
    def get_album_images(self, page=1, per_page=100):       
        data = self.provider.fetch_data(BASE_URL, method="flickr.photos.search", per_page=per_page, 
                              page=page, extras="url_l,owner_name,license", license="1,2,3,4,5,6,7,8", 
                              safe_search=1, sort="interestingness-desc", format="json",
                              min_upload_date=int(time.time())-60*60*24, content_type=1,
                              api_key=self.api_key, nojsoncallback=1)
        data = json.loads(data)
        return self._process_flickr_images(data)
    
    def _process_flickr_images(self, data):
        if data['stat'] == 'fail':  
            raise Exception("API Error: "+data['message'])

        filtered = []
        for photo in data['photos']['photo']:            
            if 'url_l' not in photo:
                continue
            if int(photo["ispublic"]) == 0:
                continue
#            print photo
            img = Image(url=photo['url_l'], title=photo['title'], attribution=photo['ownername'], 
                     image_id=photo['id'], owner_id=photo['owner'], 
                     height=photo['height_l'], width=photo['width_l'], source="flickr")
            filtered.append(img)
        return filtered 
        
    def get_photos(self, page=1, per_page=100):
        if self.album_id:
            return self.get_album_images(page, per_page)
        return self.get_interesting_photos(page, per_page)

        
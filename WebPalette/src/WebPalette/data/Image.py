
mandatory_keys = ['url', 'title', 'attribution', 'image_id', 'owner_id', 'height', 'width', 'source']

class Image(dict):
    
    def __init__(self, **kw):
        self.update(**kw)
        for k in mandatory_keys:
            if k not in self:
                raise Exception("Image is missing value "+k)
        self['height'] = int(self['height'])
        self['width'] = int(self['width'])
        
    def __getitem__(self, key):
        if key == "dimensions":
            return (self['width'], self['height'])
        return dict.__getitem__(self,key)
    
    def get(self, key, x=None):
        if not key in self and key not in ('dimensions'):
            return x
        return self[key]
        
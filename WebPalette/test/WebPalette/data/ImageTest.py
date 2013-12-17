import unittest
from WebPalette.data.Image import Image

class Test(unittest.TestCase):

    def testInitImageMissingParam(self):
        self.assertRaises(Exception, Image, None, {'param1':"i fail"})


    def testInitImageBadIntCast(self):
        params = {'url':'something', 'title':'something', 'attribution':'something', 
             'image_id':'something', 'owner_id':'something', 'height':'6', 
             'width':'something', 'source':'something'}
        self.assertRaises(Exception, Image, None, params)
        params['height'] = 'something'
        params['width'] = '5'
        self.assertRaises(Exception, Image, None, params)


    def testInitImage(self):
        img =Image(url='my_url', title='untitled', attribution='jane doe', 
             image_id='123abc', owner_id='cba321', height='6', 
             width='5', source='unittest')
        self.assertEquals(img['url'], 'my_url')
        self.assertEquals(img['width'], 5)
        
    def testImageGet(self):
        img =Image(url='my_url', title='untitled', attribution='jane doe', 
             image_id='123abc', owner_id='cba321', height='6', 
             width='5', source='unittest')
        self.assertEquals(img['url'], 'my_url')
        self.assertEquals(img.get('url'), 'my_url')
        
    def testImageDimensions(self):
        img =Image(url='my_url', title='untitled', attribution='jane doe', 
             image_id='123abc', owner_id='cba321', height='6', 
             width='5', source='unittest')
        self.assertEquals(img['dimensions'], (6,5))
        self.assertEquals(img.get('dimensions'), (6,5))
        

if __name__ == "__main__":
    unittest.main()
import cv2.cv as cv

class FaceProcessor(object):
    _min_size = (5, 5)
    _image_scale = 2
    _haar_scale = 1.2
    _min_neighbors = 2
    _haar_flags = 0
    
    def __init__(self, classifier_paths):
        self._classifiers = []
        for c in classifier_paths:
            cascade = cv.Load(c)
            self._classifiers.append(cascade)

    # TODO: maybe only embellish objects with faces and not return t/f
    def process(self, image):
        if not image:
            return None
        self.detect_faces(image)
        # Only return images that don't contain faces
        if not image['faces']:
            return image
        return None  
    
    def cleanup(self):
        pass      

    def detect_faces(self, image):
        img = cv.LoadImage(image['path'], 1)
        gray_img = cv.CreateImage((img.width,img.height), 8, 1)
        small_img = cv.CreateImage((cv.Round(img.width / self._image_scale),
                   cv.Round (img.height / self._image_scale)), 8, 1)

        # convert color input image to grayscale
        cv.CvtColor(img, gray_img, cv.CV_BGR2GRAY)

        # scale input image for faster processing
        cv.Resize(gray_img, small_img, cv.CV_INTER_LINEAR)
        cv.EqualizeHist(small_img, small_img)

        faces = []
        for classifier in self._classifiers:
            faces += cv.HaarDetectObjects(small_img, classifier, cv.CreateMemStorage(0),
                        self._haar_scale, self._min_neighbors, self._haar_flags, self._min_size)
        
        image['faces'] = faces
        if faces:
            print "Has faces :("
            return None
        return image

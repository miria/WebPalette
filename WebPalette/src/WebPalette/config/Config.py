import ConfigParser
import os
from WebPalette.services import FlickrService
from WebPalette.processor import DownloadProcessor, FaceProcessor, SizeProcessor, ColorProcessor, HeaderColorProcessor
from WebPalette.output import CSSOutput, HTMLDebugOutput

class Config(object):
    _processors = []
    _outputs = []
    _services = []
    
    def __init__(self, base_path=None):
        if base_path:
            parse(base_path, self)
    
    def get_processors(self):
        return self._processors
    
    def get_outputs(self):
        return self._outputs
    
    def get_services(self):
        return self._services
    
    def set_processors(self, processors):
        self._processors = processors
    
    def set_outputs(self, outputs):
        self._outputs = outputs
    
    def set_services(self, services):
        self._services = services
    

def parse(config_path, config):
        parser = ConfigParser.ConfigParser()
        parser.read(config_path)
        _init_services(parser, config)
        _init_outputs(parser, config)
        _init_processors(parser, config)
        
def _init_services(parser, config):
    services = []
    for key in parser.options("services"):
        if parser.getboolean("services", key):
            service_conf = dict(parser.items(key))
            class_name = key.capitalize()+"Service"
            if class_name == 'FlickrService':
                service = FlickrService.FlickrService(**service_conf)
            print type(service)
            services.append(service)
    config.set_services(services)
    
def _init_processors(parser, config):
    processors = []
    base_path = parser.get("output", "base_dir")
    tmp_base_path = os.path.join(base_path, "tmp")
    if not os.path.exists(tmp_base_path):
        os.mkdir(tmp_base_path)
    processors.append(DownloadProcessor.DownloadProcessor(tmp_base_path))
    
    if parser.getboolean("face_detector", "enabled"):
        haar_paths = [v for (n,v) in parser.items("face_detector") if n.startswith("haar_cascade_path")]
        processors.append(FaceProcessor.FaceProcessor(haar_paths))
        
    width = parser.getint("output", "width")
    height = parser.getint("output", "height")
    processors.append(SizeProcessor.SizeProcessor(width, height))
    processors.append(ColorProcessor.ColorProcessor())
    if parser.get("output", "header_text"):
        coords=parser.get("output", "header_text").split(",")
        if len(coords) != 4:
            raise Exception("Invalid header_text value %s : Expected left, upper, right, bottom" %  ",".join(coords))
        processors.append(HeaderColorProcessor.HeaderColorProcessor(([int(i) for i in coords])))
    config.set_processors(processors)
    print "Processors : %s " % repr(processors)
                
def _init_outputs(parser, config):
    outputs = []
    base_dir = parser.get("output", "base_dir")
    max_images = parser.getint("output", "max_images")
    domain_prefix = ""
    if parser.has_option("output", "domain_prefix"):
        domain_prefix = parser.get("output", "domain_prefix")
        
    if (parser.getboolean("output", "debug")):
        outputs.append(HTMLDebugOutput.HTMLDebugOutput(base_dir))
    outputs.append(CSSOutput.CSSOutput(base_dir, max_images, domain_prefix))
    

        
    config.set_outputs(outputs)
            

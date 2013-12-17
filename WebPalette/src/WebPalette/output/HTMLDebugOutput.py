import os
import time

class HTMLDebugOutput(object):

    def __init__(self, base_dir):
        self._base_dir = base_dir

    def write_images(self, images):
        fho = open(os.path.join(self._base_dir, "debug_page.html"), 'w')
        fho.write("<html><head><title>Debug Output - "+time.ctime()+"</title></head>")
        fho.write("<body><table>")
        for image in images:
            fho.write("<tr><td width=\"101\">")
            for s in ("dark", "medium", "light"):
                fho.write("<div style=\"width:100;background-color:"+image[s+"_color"]+";\">&nbsp;</div>")
            fho.write("</td>")
            fho.write("<td><img src=\""+image['path']+"\"></td></tr>")
        fho.write("</body></html>")
        fho.close()
from qgis.core import QgsPoint
from qgis.PyQt.QtGui import QImage
from qgis.PyQt.QtCore import QSize
from qgis.core import QgsMapRendererCustomPainterJob
from qgis.core import QgsCoordinateReferenceSystem, QgsCoordinateTransform
from PyQt5.QtGui import QPainter
import cv2
import os
def do_screenshot(canvas):
    filepath = os.path.join(os.getcwd(), 'out.png')
    

    canvas.saveAsImage(filepath)
    image = cv2.imread(filepath)


    # Return the top left and bottom right coordinates and the QImage object
    return image

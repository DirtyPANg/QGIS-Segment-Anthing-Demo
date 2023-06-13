from qgis.core import (QgsField, QgsFeature, QgsGeometry, 
                       QgsVectorLayer, QgsProject)
from qgis.core import QgsVectorLayer, QgsFields, QgsFeature, QgsPoint, QgsGeometry, QgsWkbTypes, QgsVectorFileWriter
from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsSimpleFillSymbolLayer, QgsSingleSymbolRenderer, QgsFillSymbol
from qgis.PyQt.QtGui import QColor
from qgis.PyQt.QtCore import Qt
def draw_polygon(layer, geo_contours, feature_name="auto"):
    # Get the data provider from the layer
    pr = layer.dataProvider()
    

    # Add fields if necessary
    if not pr.fields():
        pr.addAttributes([QgsField("name", QVariant.String)])
        layer.updateFields()

    for points in geo_contours:
        # Add a feature
        fet = QgsFeature()
        fet.setGeometry(QgsGeometry.fromPolygonXY([points]))  # Use the list of points here
        fet.setAttributes([feature_name])
        pr.addFeatures([fet])


    # Update layer's extent when new features have been added
    layer.updateExtents()




def set_layer_style(layer, color=QColor( 50, 255, 100), width=0.5):
    # Create a new symbol layer (Simple Fill)
    color.setAlphaF(0.1)

    symbol_layer = QgsSimpleFillSymbolLayer(style=Qt.NoBrush,    # Outline color
                                            strokeWidth=width)  # Outline width

    # Create a new fill symbol and add the symbol layer to it
    fill_symbol = QgsFillSymbol()
    fill_symbol.changeSymbolLayer(0, symbol_layer)

    # Create a new renderer using the fill symbol
    layer_renderer = QgsSingleSymbolRenderer(fill_symbol)

    # Apply the renderer to the layer
    layer.setRenderer(layer_renderer)

    # Refresh the map canvas
    layer.triggerRepaint()



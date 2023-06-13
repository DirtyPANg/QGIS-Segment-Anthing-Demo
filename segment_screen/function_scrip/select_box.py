
from PyQt5.QtWidgets import QComboBox,QMessageBox
from qgis.core import QgsProject,QgsWkbTypes,QgsVectorLayer
def initLayerComboBox(this):
        this.clear()
        for layerId, layer in QgsProject.instance().mapLayers().items():
               # if layer.wkbType() == QgsWkbTypes.Polygon:
               this.addItem(layer.name(), layerId)      
        
def get_layer(self,box):
        layer_name = box.currentText()
        layer = QgsProject.instance().mapLayersByName(layer_name)
        if not layer:
                QMessageBox.warning(
                  self.dlg,
                  self.tr("Layer selection"),
                  self.tr(f"No layer named {layer_name} found!"),
                  )
                return None
        layer = layer[0]
        if not isinstance(layer, QgsVectorLayer):
                QMessageBox.warning(
                self.dlg,
                self.tr("Layer selection"),
                self.tr(f"The layer {layer_name} is not a vector layer!"),
                )
                return None
        return layer

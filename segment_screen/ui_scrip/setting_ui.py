import torch
from PyQt5 import QtWidgets, QtCore

class Ui_SettingsDialog(object):
    def __init__(self):
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(500, 400)

        self.formLayout = QtWidgets.QFormLayout(SettingsDialog)
        self.formLayout.setObjectName("formLayout")

        self.label_memory = QtWidgets.QLabel(SettingsDialog)
        self.label_memory.setObjectName("label_memory")
        self.spinbox_memory = QtWidgets.QSpinBox()
        self.formLayout.addRow(self.label_memory, self.spinbox_memory)

        self.label_model = QtWidgets.QLabel(SettingsDialog)
        self.label_model.setObjectName("label_model")
        self.lineedit_model = QtWidgets.QLineEdit()
        self.formLayout.addRow(self.label_model, self.lineedit_model)

        # create and add other widgets...

        self.checkbox_gpu = QtWidgets.QCheckBox(SettingsDialog)
        self.checkbox_gpu.setObjectName("checkbox_gpu")
        self.checkbox_gpu.setEnabled(self.device.type == "cuda")
        self.formLayout.addRow(self.checkbox_gpu)

        # buttons to save and load settings
        self.button_save = QtWidgets.QPushButton("Save settings")
        self.button_save.clicked.connect(self.save_settings)
        self.formLayout.addRow(self.button_save)

        self.button_load = QtWidgets.QPushButton("Load settings")
        self.button_load.clicked.connect(self.load_settings)
        self.formLayout.addRow(self.button_load)

        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def save_settings(self):
      with open("settings.txt", "w") as file:
        file.write(f"Memory={self.spinbox_memory.value()}\n")
        file.write(f"Model={self.lineedit_model.text()}\n")
        file.write(f"PointsPerSide={self.spinbox_points_per_side.value()}\n")
        file.write(f"PredIoUThresh={self.spinbox_pred_iou_thresh.value()}\n")
        file.write(f"StabilityScoreThresh={self.spinbox_stability_score_thresh.value()}\n")
        file.write(f"CropNLayers={self.spinbox_crop_n_layers.value()}\n")
        file.write(f"CropNPointsDownscaleFactor={self.spinbox_crop_n_points_downscale_factor.value()}\n")
        file.write(f"MinMaskRegionArea={self.spinbox_min_mask_region_area.value()}\n")
        file.write(f"UseGPU={self.checkbox_gpu.isChecked()}\n")

    def load_settings(self):
      try:
        with open("settings.txt", "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                if key == "Memory":
                    self.spinbox_memory.setValue(int(value))
                elif key == "Model":
                    self.lineedit_model.setText(value)
                elif key == "PointsPerSide":
                    self.spinbox_points_per_side.setValue(int(value))
                elif key == "PredIoUThresh":
                    self.spinbox_pred_iou_thresh.setValue(float(value))
                elif key == "StabilityScoreThresh":
                    self.spinbox_stability_score_thresh.setValue(float(value))
                elif key == "CropNLayers":
                    self.spinbox_crop_n_layers.setValue(int(value))
                elif key == "CropNPointsDownscaleFactor":
                    self.spinbox_crop_n_points_downscale_factor.setValue(int(value))
                elif key == "MinMaskRegionArea":
                    self.spinbox_min_mask_region_area.setValue(int(value))
                elif key == "UseGPU":
                    self.checkbox_gpu.setChecked(value == "True")
      except FileNotFoundError:
        print("Settings file not found. Creating with default settings.")
        self.create_default_settings()
        self.load_settings()

    def create_default_settings(self):
    # set the default values for settings
      self.spinbox_memory.setValue(8)
      self.lineedit_model.setText('sam')
      self.spinbox_points_per_side.setValue(32)
      self.spinbox_pred_iou_thresh.setValue(0.86)
      self.spinbox_stability_score_thresh.setValue(0.92)
      self.spinbox_crop_n_layers.setValue(1)
      self.spinbox_crop_n_points_downscale_factor.setValue(2)
      self.spinbox_min_mask_region_area.setValue(100)
      self.checkbox_gpu.setChecked(False)
    
    # save these as the current settings
      self.save_settings()

from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
import torch
import cv2
import numpy as np
import os
from PyQt5.QtWidgets import QMessageBox
def ready_model(self):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    model_path = os.path.join(current_directory, "sam_vit_h_4b8939.pth")

    sam = sam_model_registry["default"](checkpoint=model_path)

    msg = QMessageBox()
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    if torch.cuda.is_available():
      reply = msg.question(self, 'Use CUDA', 'Would you like to use CUDA for computation?',
                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
      if reply == QMessageBox.Yes:
          msg.setText("You've chosen to use CUDA for computation.")
          # Code to use CUDA for computation
          sam.to(device)
      else:
          msg.setText("You've chosen not to use CUDA for computation.")
          # Code to not use CUDA for computation
    else:
      msg.setText("CUDA is not available.")
      msg.setIcon(QMessageBox.Information)
      msg.setWindowTitle("Title")
      msg.exec_()

    
    mask_generator = SamAutomaticMaskGenerator(model = sam
                                ,pred_iou_thresh=0.70
                                ,stability_score_thresh=0.92)
    return mask_generator
def segmenting(model,image,coordinate_transform,user_ram_gb = 8):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w, _ = image_rgb.shape

    # Memory threshold, if the user inputted amount is less than this, decrease the size of the image
    ram_threshold_gb = 24
    user_ram_gb_for_image = max(0, user_ram_gb - 4)  # at least 0

    # If the user inputted amount of memory is less than the threshold, decrease the max size of the image proportionally
    scale_factor = user_ram_gb_for_image / ram_threshold_gb if user_ram_gb_for_image < ram_threshold_gb else 1

    max_h = int(3000 * scale_factor)
    max_w = int(2500 * scale_factor)

    scale = 1  # default value in case no resize happens

# the part of code where resizing is done
    if h > max_h or w > max_w:
    # Calculate the scale factors
      scale_h = max_h / h
      scale_w = max_w / w

    # Use the smaller scale factor to ensure the resized image fits within the max dimensions
      scale = min(scale_h, scale_w)

    # Resize the image
      new_h = int(h * scale)
      new_w = int(w * scale)
      image = cv2.resize(image_rgb, (new_w, new_h))

    masks = model.generate(image )
    if len(masks) == 0:
        return None
    sorted_anns = sorted(masks, key=(lambda x: x['area']), reverse=True)
    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:,:,3] = 0
    contours = []
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])
        img[m] = color_mask

        # 使用 cv2.findContours 找到掩码的边界
        contour, _ = cv2.findContours(m.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours.append(contour[0])
        

    geo_contours = []
    for contour in contours:
      geo_contour = []
      for point in contour:
          # point[0][0] is x, point[0][1] is y
          # scale the point coordinates back to the original image size
          original_x = point[0][0] / scale
          original_y = point[0][1] / scale
          geo_point = coordinate_transform.toMapCoordinates(original_x, original_y)
          geo_contour.append(geo_point)
      geo_contours.append(geo_contour)
    return geo_contours

        
   
          


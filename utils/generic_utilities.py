import os
import time

import numpy as np

def roi_coordinates(roi_width: int, roi_height: int, frame_width: int, frame_height: int, x: int = 0, y: int = 0):
    """
    This function returns the coordinates of the region of interest for face detection.
        Face detection will be performed on the region of interest only.

    Args:
        roi_width (int): width of the region of interest
        roi_height (int): height of the region of interest
        frame_width (int): width of the frame
        frame_height (int): height of the frame
        x (int): x coordinate of the middle of the region of interest
        y (int): y coordinate of the bottom of the region of interest
    
    Returns:
        tuple(roi_left, roi_top, roi_right, roi_bottom): coordinates of the ROI (region of interest)
    """

    frame_x_center = frame_width // 2
    roi_width_half = roi_width // 2

    roi_left = frame_x_center - roi_width_half + x
    roi_right = frame_x_center + roi_width_half + x

    roi_bottom = frame_height - y
    roi_top = roi_bottom - (roi_height + y)

    return roi_left, roi_top, roi_right, roi_bottom


def create_mask(frame: np.ndarray, left: int, top: int, right: int, bottom: int):
    """
    This function creates a mask for the frame so that face detection is performed only on the region of interest
    
    Args:
        frame (numpy.ndarray): frame on which the mask will be applied
        left (int): left coordinate of the region of interest
        top (int): top coordinate of the region of interest
        right (int): right coordinate of the region of interest
        bottom (int): bottom coordinate of the region of interest

    Returns:
        numpy.ndarray: mask for the frame
    """
    mask = np.zeros_like(frame)
    mask[top:bottom, left:right] = 1
    return mask

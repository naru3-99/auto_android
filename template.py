import cv2
import numpy as np
import time
from PIL import Image
from common.start_scrcpy import start_scrcpy
from common.macro import click_coordinate

# 差分と認識するピクセル数
MIN_AREA_4_DIFF = 100

# クリックしても良い座標の範囲
RANGE_X = (820, 1180)
RANGE_Y = (480, 760)


def detect_enemy_coordinate(last_scrn, curr_scrn):
    # Convert images to grayscale
    last_gray = np.array(last_scrn.convert("L"))
    curr_gray = np.array(curr_scrn.convert("L"))

    # Compute the absolute difference between the two images
    diff = cv2.absdiff(last_gray, curr_gray)

    # Threshold the difference image to get binary image
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours by area
    filtered_contours = [
        cnt for cnt in contours if cv2.contourArea(cnt) > MIN_AREA_4_DIFF
    ]

    # Find the enemy's coordinate
    bounding_boxes = [cv2.boundingRect(cnt) for cnt in filtered_contours]
    enemy_coords = []
    for bbox in bounding_boxes:
        x, y, w, h = bbox
        center_x = x + (w / 2)
        center_y = y + (h / 2)
        # coordinates must be int, int
        enemy_coords.append((int(center_x), int(center_y)))

    return enemy_coords


def click_coordinate_in_range(coord):
    # rangeの中であればクリックする
    x, y = coord
    if not (x > RANGE_X[0] and x < RANGE_X[1]):
        return False
    if not (y > RANGE_Y[0] and y < RANGE_Y[1]):
        return False

    click_coordinate(coord)
    return True


def main():
    click_coordinate_in_range((1000, 600))


if __name__ == "__main__":
    start_scrcpy()
    main()

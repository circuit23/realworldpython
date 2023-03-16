import os
from pathlib import Path
import numpy as np
import cv2 as cv

MIN_NUM_KEYPOINT_MATCHES = 50


def main():
    """Loop through 2 folders with paired images, register & blink images."""
    night1_files = sorted(os.listdir('night_1'))
    night2_files = sorted(os.listdir('night_2'))
    path1 = Path.cwd() / 'night_1'
    path2 = Path.cwd() / 'night_2'
    path3 = Path.cwd() / 'night_1_registered'

    for i, _ in enumerate(night1_files):
        img1 = cv.imread(str(path1 / night1_files[i]), cv.IMREAD_GRAYSCALE)
        img2 = cv.imread(str(path2 / night2_files[i]), cv.IMREAD_GRAYSCALE)
        print("Comparing {} to {}.\n".format(night1_files[i], night2_files[i]))
        kp1, kp2, best_matches = find_best_matches(img1, img2)
        img_match = cv.drawMatches(img1, kp1, img2, kp2, best_matches, outImg=None)
        height, width = img1.shape
        cv.line(img_match, (width, 0), (width, height), (255, 255, 255), 1)
        QC_best_matches(img_match)  # Comment out to ignore.
        img1_registered = register_image(img1, img2, kp1, kp2, best_matches)

        blink(img1, img1_registered, 'Check Registration', num_loops=5)
        out_filename = '{}_registered.png'.format(night1_files[i][:-4])
        cv.imwrite(str(path3 / out_filename), img1_registered)  # Will overwrite!
        cv.destroyAllWindows()
        blink(img1_registered, img2, 'Blink Comparator', num_loops=15)

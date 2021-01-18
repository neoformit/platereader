"""Reads a plate image to assess the area of fungal growth."""

import os
import cv2 as cv
from PIL import Image
from matplotlib import pyplot as plt

# Parameters:
THRESH_LOWER = 200
THRESH_UPPER = 255
INPUT_DIRNAME = 'images'
OUTPUT_DIRNAME = 'output'
OUTPUT_EXTENSION = '.contour.jpg'


def main():
    """Process all jpg files in this directory."""
    assert_dirs()
    areas = {}
    images = [
        os.path.join(INPUT_DIRNAME, x)
        for x in os.listdir(INPUT_DIRNAME) if x.endswith('.jpg')
    ]

    if not images:
        print(
            f'Put some .jpg images in the "{INPUT_DIRNAME}" folder',
            'to analyse'
        )
        return

    for image in images:
        print(f"Processing image {image}...")
        areas[image] = read_plate_area(image)

    with open('areas.csv', 'w') as f:
        f.write('Image,Area (px)\n')
        f.write('\n'.join([
            ','.join([k, str(v)]) for k, v in areas.items()
        ]) + '\n')


def read_plate_area(filename):
    """Read the area of fungal growth on plate.

    Show annotated image of plate with fungal contour outlined.
    """
    img = cv.imread(filename)

    img_th = threshold(
        img,
        blur_factor=15,
        lower=160,
    )

    contours, hierarchy = cv.findContours(
        img_th,
        cv.RETR_TREE,
        cv.CHAIN_APPROX_SIMPLE,
    )

    areas = [cv.contourArea(c) for c in contours]
    max_area = max(areas)
    biggest = areas.index(max_area)

    contour_img_array = cv.drawContours(
        img,
        contours,
        biggest,        # Draw biggest only
        (0, 255, 0),    # Annotation colour BGR
        3               # Line thickness
    )

    contour_img_array = cv.drawContours(
        img,
        contours,
        biggest,        # Draw biggest only
        (0, 255, 0),    # Annotation colour BGR
        3               # Line thickness
    )

    img = Image.fromarray(contour_img_array, 'RGB')
    fig = plt.figure()
    s = fig.add_subplot(111)
    s.imshow(img)
    s.text(850, 900, f"Area: {round(max_area)} px",
           color="white", fontsize=8)
    plt.axis('off')

    fname = os.path.join(
        OUTPUT_DIRNAME,
        filename.replace('.jpg', OUTPUT_EXTENSION),
    )
    print(f"Saving contour image {fname}...")
    plt.savefig(fname, dpi=300)

    return max_area


def threshold(img, blur_factor=None, lower=None, upper=None):
    """Apply threshold to find edges of spots.

    Two parameters affect thresholding of spot outlines. Default values
    are defined in settings.py:

    blur_factor must be an odd number (for some reason?). This smooths the
    spot outlines.

    lower and upper should be from 0-256 and determines the RGB levels on
    which the edge of a spot will be drawn.
    """
    blur_factor = blur_factor or 0
    img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_blur = cv.GaussianBlur(
        img_grey,
        (blur_factor, blur_factor),
        0
    )   # Scale by SF

    # Calibrate thresholding according to k distribution
    threshold_lower = lower or THRESH_LOWER

    ret, img_threshold = cv.threshold(
        img_blur,
        threshold_lower,
        upper or THRESH_UPPER,
        0
    )   # Scale by median K?
    return img_threshold


def assert_dirs():
    """Assert that output dir exists."""
    if not os.path.exists(INPUT_DIRNAME):
        os.mkdir(INPUT_DIRNAME)
    if not os.path.exists(OUTPUT_DIRNAME):
        os.mkdir(OUTPUT_DIRNAME)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(str(exc))
        input('Press enter to quit\n> ')

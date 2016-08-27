
"""  Brief demo of image processing using OpenCV Python bindings.

Author: Nathan Sprague
Version: 3/17/14
"""


import cv2


def camera_loop():
    """
    Capture an image from camera 0, perform some processing,
    and display the result.
    """
    width = 320
    height = 240

    # Tell OpenCV which camera to use:
    capture = cv2.VideoCapture(0)

    # Set up image capture to grab the correct size:
    capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, height)

    # See what size image is REALLY being captured
    # (in case setting failed above.)
    height = capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
    width = capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)


    while(True):
        # Grab the image from the camera.  This  will be a
        # height x width x 3 numpy array
        success, img = capture.read()

        # Separate out the blue, red and green channels.
        blue, green, red = cv2.split(img)

        # Convert the image to grayscale:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Blur the image:
        blur = cv2.blur(gray, (3,3))

        # Perform edge detecion on the blurred image:
        edges = cv2.Canny(blur, 60, 80)

        # Show four versions of the image:
        cv2.imshow("Original Image", img)
        cv2.imshow("Blur", blur)

        cv2.imshow("Mystery Color", img[:,:,2])
        cv2.imshow("Edge Detection", edges)
        # Pause 33 milliseconds before repeating loop.

        c = cv2.waitKey(33)

if __name__ == "__main__":
    camera_loop()

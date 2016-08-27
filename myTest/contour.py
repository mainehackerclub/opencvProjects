# not working right
import cv2
import numpy as np

#
# Mat src; Mat src_gray;

thresh = 50

max_thresh = 255
# RNG;  //random number generator
RNG = np.random(12345)

#
# /// Function header
# void thresh_callback(int, void* );
#
# /** @function main */
# int main( int argc, char** argv ){
#

cap = cv2.VideoCapture(0)
#     if(!cap.open(0))
#         return 0;
#      // Create mat with alpha channel
#     Mat mat(480, 640, CV_8UC4);
scr = cv2.split(cap,[4])
scr_gray = scr[3]

while True:
# 	Mat frame;
#     cap >> frame;
#     src = frame;
        success, frame = cap.read()
        blue, green, red = cv2.split(frame)

#   /// Convert image to gray and blur it
#
gray = cv2.cvtColor(scr_gray, scr_gray, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(scr_gray,  (3,3),0 )

#
#   //createTrackbar( " Canny thresh:", "Source", &thresh, max_thresh, thresh_callback );
#   thresh_callback( 0 , 0 );
#   waitKey(200);
# }

#   return(0);
# }
#
# /** @function thresh_callback */
# void thresh_callback(int, void* ){
#   Mat canny_output;
#   vector<vector<Point> > contours;
#   vector<Vec4i> hierarchy;
#
#   /// Detect edges using canny
#   Canny( src_gray, canny_output, thresh, thresh*2, 3 );

#   /// Find contours
#   findContours( canny_output, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0) );
#
#   /// Draw contours
#   Mat drawing = Mat::zeros( canny_output.size(), CV_8UC3 );
#   for(unsigned int i = 0; i< contours.size(); i++ )
#      {
#        Scalar color = Scalar( rng.uniform(0, 255), rng.uniform(0,255), rng.uniform(0,255) );
#        drawContours( drawing, contours, i, color, 2, 8, hierarchy, 0, Point() );
#      }
#
#   /// Show in a window
#   namedWindow( "Contours", CV_WINDOW_AUTOSIZE );
#   imshow( "Contours", drawing );
# }
#     cv2.imshow("raw",raw)
#     cv2.imshow("mask",mask)
    cv2.imshow("Contours", drawing )
     k = cv2.waitKey(100)
        if k == 32: # spacebar
        break

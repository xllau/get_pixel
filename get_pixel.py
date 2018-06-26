import numpy as np  
import cv2    
print(cv2.__version__)


def show_pixel(event, x, y, flags, param): 
    if event == cv2.EVENT_LBUTTONDOWN:
        print("x:",x," y:",y, img[y,x,:]) 
  
if __name__ == '__main__':
    import argparse

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='pick pixel value in an image!')
    parser.add_argument("imagename",
                        metavar="imagename",
                        help="'path to image and name")
    args = parser.parse_args()
    print("path: ",args.imagename)


    #img = np.zeros((512, 512, 3), np.uint8)
    img = cv2.imread(args.imagename)
    cv2.namedWindow('image')      
    cv2.setMouseCallback('image', show_pixel)    
            
    while (1):
       cv2.imshow('image', img)
       if cv2.waitKey(2) & 0xFF == 27:       
           break  
    cv2.destroyAllWindows()

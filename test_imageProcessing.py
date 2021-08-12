# imorting the module
import cv2

# function to display the coordinates of
# the points clicked on the image
def click_event(event, x, y, flags, params):

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' + 
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        # cv2.imshow('image', img)
        resize()

    # checking for right mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        # cv2.imshow('image', img)
        resize()

    # clean texts on image
    if event == cv2.EVENT_MBUTTONDOWN:
        print('middle mouse button pressed')

def resize():
    scale_percent = 60 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    # dim = (width, height)
    dim = (1200, 1697)

    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow('image', resized)


# # driver function
# if __name__ == "__main__":
#     # reading the image

#     # img = cv2.imread('panzoom executing.png', 1) # for test

#     img = cv2.imread('INBG_01_01.jpg', 1)

#     # displaying the image
#     # cv2.imshow('image', img)
#     resize()

#     # setting mouse handler for the image
#     # and calling the click_event() function
#     cv2.setMouseCallback('image', click_event)

#     # wait for a key to be pressed to exit
#     cv2.waitKey(0)

#     # close the window
#     cv2.destroyAllWindows()

#     cv2.namedWindow('image')
#     cv2.moveWindow('image', 20, 20)
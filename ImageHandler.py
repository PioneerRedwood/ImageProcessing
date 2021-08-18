# imorting the module
from SelectionTracker import SelectionTracker
import cv2
import imutils
from tkinter import *

class ImageHandler:
    windowName = 'ImageProcessing'
    filePath = ''
    tracker = SelectionTracker()

    # root = Tk()
    # root.title('stored position')

    page = 0
    # width: 1200px, height: 1697px
    yPos = [0, 1697]

    dataType = {'N':'None', 'D':'Data', 'C':'Check', 'S':'Signature'}
    currType = 'None'

    def __init__(self, img):
        # click_eve
        params = [img]

        # window setting
        # how is this method works exactly?
        cv2.namedWindow(self.windowName)
        
        # setting mouse handler for the image
        # and calling the click_event() function
        # params like array
        cv2.setMouseCallback(self.windowName, self.click_event, params)

        cv2.imshow(self.windowName, self.resize(img))

        # self.tracker.root.mainloop()

        self.loop()

        self.destroy()

    def loop(self):
        while True:
            keycode = cv2.waitKey(0)
            print(keycode)
            if keycode == ord('q') or keycode == 27 or keycode == -1:
                print('quit..')
                break
            
            # toggle data type
            if keycode == ord('d') or keycode == ord('D'):
                if self.currType != self.dataType['D']:
                    self.currType = self.dataType['D']
                else:
                    self.currType = self.dataType['N']
                continue

            if keycode == ord('n') or keycode == ord('N'):
                if self.currType != self.dataType['N']:
                    self.currType = self.dataType['N']
                continue

            if keycode == ord('c') or keycode == ord('C'):
                if self.currType != self.dataType['C']:
                    self.currType = self.dataType['C']
                else:
                    self.currType = self.dataType['N']
                continue

            if keycode == ord('s') or keycode == ord('S'):
                if self.currType != self.dataType['S']:
                    self.currType = self.dataType['S']
                else:
                    self.currType = self.dataType['N']
                continue

    # returned resized image
    def resize(self, img):
        # scale_percent = 100 # percent of original size
        # width = int(img.shape[1] * scale_percent / 100)
        # height = int(img.shape[0] * scale_percent / 100)
        # dim = (width, height)
        print('width;' , (img.shape[1]), 'height;' , (img.shape[0]))
        dim = (1200, 1697)
        # dim = (1358, 1920)
        
        return cv2.resize(img, dim, interpolation=cv2.INTER_BITS)

    def click_event(self, event, x, y, flags, params):
        # mouse scroll function
        if event == cv2.EVENT_MOUSEWHEEL:
            # print(self.yPos)
            if self.page == 0:
                self.page = 1
                cv2.imshow(self.windowName, self.resize(imutils.translate(params[0], 0, -self.yPos[1])))
            else:
                self.page = 0
                cv2.imshow(self.windowName, self.resize(imutils.translate(params[0], 0, self.yPos[0])))
            return

        # checking for left mouse clicks
        if event == cv2.EVENT_LBUTTONDOWN:
            strClickInfo = self.currType + ' : ' + str(x) + ' ' + str(y)
            print(strClickInfo)

            # extract where do you pick
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(params[0], str(x) + ',' + 
                        str(y), (x,y), font,
                        1, (255, 0, 0), 2)

            # cv2.circle(params[0], (x, y), 1, (255, 0, 0), 3)
            if self.page == 0:
                cv2.imshow(self.windowName, self.resize(imutils.translate(params[0], 0, self.yPos[0])))
            else:
                cv2.imshow(self.windowName, self.resize(imutils.translate(params[0], 0, -self.yPos[1])))                

            self.tracker.add(strClickInfo)
            self.tracker.show()
            self.currType = 'None'

        # checking for right mouse clicks
        elif event == cv2.EVENT_RBUTTONDOWN:
            print(x, ' ', y)

            # extract pixel rgb color
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # b = img[y, x, 0]
            # g = img[y, x, 1]
            # r = img[y, x, 2]
            # cv2.putText(img, str(b) + ',' +
            #             str(g) + ',' + str(r),
            #             (x,y), font, 1,
            #             (255, 255, 0), 2)

        # checking for middle mouse clicks
        elif event == cv2.EVENT_MBUTTONDOWN:
            print('cv2.EVENT_MBUTTONDOWN')

        # track mouse position
        elif event == cv2.EVENT_MOUSEMOVE:
            return

    def destroy(self):
        cv2.destroyAllWindows()

    # update stored position
    def update_tk(self):

        for str in self.tracker.stored:
            # for each stored info, make a functional frame
            #   text, delete button 
            frame = Frame(self.root, relief=SOLID, bd=1)
            frame.pack(side='top', fill='both', expand=True)

            label = Label(frame, text=str, anchor='w')
            rmBtn = Button(frame, text='Del', command=lambda: frame.pack_forget())

            label.pack()
            rmBtn.pack()



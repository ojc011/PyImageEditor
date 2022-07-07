from tkinter import ttk, Tk, PhotoImage, RIDGE, Canvas, GROOVE, Scale, HORIZONTAL, filedialog
import cv2
from PIL import Image, ImageTk
import numpy as np


class FrontEnd:
    def __init__(self, master):
        self.master = master
        
#HEADER#
        self.master.geometry('750x550+250+10') ##Determines Size of Window##
        self.master.title('Image Editor App with Tkinter and OpenCV') ##Title of app, similar to that of an html tab##
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()
        self.logo = PhotoImage(file='pythongif.gif').subsample(5, 5)
        print(self.logo)
        
        ttk.Label(self.frame_header, image=self.logo).grid(
            row=0, column=0, rowspan=2)
        
        ttk.Label(self.frame_header, text='Welcome to the Image Editor App!').grid(
            row=0, column=1)
        
        ttk.Label(self.frame_header, text='Upload, edit and save your images Easily!').grid(
            row=1, column=1)
        
#END HEADER#

## MAIN MENU ##
        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief=RIDGE, padding=(50, 15))
        
        ttk.Button(
            self.frame_menu, text="Upload An Image", command=self.upload_action).grid(row=0, column=0, padx=5, pady=5, sticky='sw')
        
        ttk.Button(
            self.frame_menu, text="Crop Image", command=self.crop_action).grid(row=1, column=0, padx=5, pady=5, sticky='sw')
        
        ttk.Button(
            self.frame_menu, text="Add Text", command=self.text_action_1).grid(row=2, column=0, padx=5, pady=5, sticky='sw')
        
        ttk.Button(
            self.frame_menu, text="Draw Over Image", command=self.draw_action).grid(row=3, column=0, padx=5, pady=5, sticky='sw')
        
        ttk.Button(
            self.frame_menu, text="Apply Filters", command=self.filter_action).grid(row=4, column=0, padx=5, pady=5, sticky='sw')
        
        ttk.Button(
            self.frame_menu, text="Blur/Smoothening", command=self.blur_action).grid(row=5, column=0, padx=5, pady=5, sticky='sw')
        
        ttk.Button(
            self.frame_menu, text="Adjust Levels", command=self.adjust_action).grid(row=6, column=0, padx=5, pady=5, sticky='sw')
        
        ttk.Button(
            self.frame_menu, text="Rotate", command=self.rotate_action).grid(row=7, column=0, padx=5, pady=5, sticky='sw')
        
        ttk.Button(
            self.frame_menu, text="Flip", command=self.flip_action).grid(
                row=8, column=0, padx=5, pady=5, sticky='sw')
            
        ttk.Button(
            self.frame_menu, text="Save As", command=self.save_action).grid(row=9, column=0, padx=5, pady=5, sticky='sw')
## MAIN MENU ##
        
 ##FOOTER MENU##    
        self.apply_and_cancel = ttk.Frame(self.master)
        self.apply_and_cancel.pack()
        
        self.apply = ttk.Button(
            self.apply_and_cancel, text="Apply", command=self.apply_action)
        self.apply.grid(row=0, column=0,
                     padx=5, pady=5, sticky='sw')
    
        ttk.Button(
            self.apply_and_cancel, text="Cancel", command=self.cancel_action).grid(row=0, column=1,
                    padx=5, pady=5, sticky='sw')
    
        ttk.Button(
            self.apply_and_cancel, text="Revert All Changes", command=self.revert_action).grid(row=0, column=2,
                                padx=5, pady=5, sticky='sw')
            
## Canvas for image display ##

        self.canvas = Canvas(self.frame_menu, bg="gray", width=300, height=400)
        self.canvas.grid(row=0, column=1, rowspan=10)
        
## Canvas for image display end##
        
##FOOTER MENU END##

    def refresh_side_frame(self):
        try:
            self.side_frame.grid_forget()
        except:
            pass
        
        #self.canvas.unbind("<ButtonPress>")
        #self.canvas.unbind("<B1-Motion>")
        #self.canvas.unbind("<ButtonRelease>")
        #self.display_image(self.edited_image)
        
        self.side_frame = ttk.Frame(self.frame_menu)
        self.side_frame.grid(row=0, column=2, rowspan=10)
        self.side_frame.config(relief=GROOVE, padding=(50, 15))
        
    def upload_action(self): ## Will open file explorer to upload picture ##
        self.canvas.delete("all")
        
        self.filename = filedialog.askopenfilename()
        
        self.original_image = cv2.imread(self.filename)
        self.edited_image = cv2.imread(self.filename)
        self.filtered_image = cv2.imread(self.filename)
        
        self.display_image(self.edited_image) ##Edited image will be saved here
        
    def text_action_1(self):
        self.refresh_side_frame()
        ttk.Label(self.side_frame, text="Please enter text").grid(row=0,column=0)
        
    def draw_action(self):
        pass
    def crop_action(self):
        pass
    
    ## FILTER MENU OPTIONS ##
    def filter_action(self):
        self.refresh_side_frame()
        ttk.Button(
            self.side_frame, text="Negative", command=self.negative_action).grid(row=0, column=2, padx=5, pady=5, sticky='sw')
        ttk.Button(
            self.side_frame, text="Black and White", command=self.bw_action).grid(row=1, column=2, padx=5, pady=5, sticky='sw')
        ttk.Button(
            self.side_frame, text="Stylisation", command=self.stylisation_action).grid(row=2, column=2, padx=5, pady=5, sticky='sw')
        ttk.Button(
            self.side_frame, text="Sketch Effect", command=self.sketch_action).grid(row=3, column=2, padx=5, pady=5, sticky='sw')
        ttk.Button(
            self.side_frame, text="Emboss", command=self.emb_action).grid(row=4, column=2, padx=5, pady=5, sticky='sw')
        ttk.Button(
            self.side_frame, text="Sepia", command=self.sepia_action).grid(row=5, column=2, padx=5, pady=5, sticky='sw')
        ttk.Button(
            self.side_frame, text="Binary Thresholding", command=self.binary_threshold_action).grid(row=6, column=2, padx=5, pady=5, sticky='sw')
        ttk.Button(
            self.side_frame, text="Erosion", command=self.erosion_action).grid(row=7, column=2, padx=5, pady=5, sticky='sw')
        ttk.Button(
            self.side_frame, text="Dilation", command=self.dilation_action).grid(row=8, column=2, padx=5, pady=5, sticky='sw')
    ## FILTER MENU OPTIONS END ##
    
    ## BLUR MENU OPTIONS ##
    def blur_action(self):
        self.refresh_side_frame()
        
        ttk.Label(
            self.side_frame, text="Averaging Blur").grid(row=0, column=2, padx=5, pady=5, sticky='sw')
        
        self.average_slider = Scale(
            self.side_frame, from_=0, to=50, orient=HORIZONTAL, command=self.averaging_action)
        self.average_slider.grid(row=1, column=2, padx=5, sticky='sw')
        
        ttk.Label(
            self.side_frame, text="Gaussian Blur").grid(row=2, column=2, padx=5, pady=5, sticky='sw')
        
        self.gaussian_slider = Scale(
            self.side_frame, from_=0, to=50, orient=HORIZONTAL, command=self.gaussian_action)
        self.gaussian_slider.grid(row=3, column=2, padx=5, sticky='sw')
        
        ttk.Label(
            self.side_frame, text="Median Blur").grid(row=4, column=2, padx=5, pady=5, sticky='sw')
        
        self.median_slider = Scale(
            self.side_frame, from_=0, to=50, orient=HORIZONTAL, command=self.median_action)
        self.median_slider.grid(row=5, column=2, padx=5, pady=5, sticky='sw')
    ## BLUR MENU OPTIONS END ##
    
    ## ROTATE ACTION ##
    def rotate_action(self):
        self.refresh_side_frame()
        ttk.Button(
            self.side_frame, text="Rotate Left", command=self.rotate_left_action).grid(row=0, column=2, padx=5, pady=5, sticky='sw')
        
        ttk.Button(
            self.side_frame, text="Rotate Right", command=self.rotate_right_action).grid(row=1, column=2, padx=5, pady=5, sticky='sw')
        
    ## ROTATE ACTION END ##
    
    ## FLIP ACTION ##
    def flip_action(self):
        self.refresh_side_frame()
        ttk.Button(
            self.side_frame, text="Vertical Flip", command=self.vertical_action).grid(row=0, column=2, padx=5, pady=5, sticky='sw')
        
        ttk.Button(
            self.side_frame, text="Horizontal Flip", command=self.horizontal_action).grid(row=1, column=2, padx=5, pady=5, sticky='sw')
        
    ##FLIP ACTION END ##
    
    def save_action(self):
        pass
    
    ## ADJUST ACTION ##
    def adjust_action(self):
        self.refresh_side_frame()
        ttk.Label(
            self.side_frame, text="Brightness").grid(row=0, column=2, padx=5, pady=5, sticky='sw')
        
        self.brightness_slider = Scale(
            self.side_frame, from_=0, to_=2, resolution=0.1, orient=HORIZONTAL, command=self.brightness_action)
        self.brightness_slider.grid(row=1, column=2, padx=5, pady=5, sticky='sw')
        self.brightness_slider.set(1)
        
        ttk.Label(
            self.side_frame, text="Saturation").grid(row=2, column=2, padx=5, pady=5, sticky='sw')
        self.saturation_slider = Scale(
            self.side_frame, from_=-200, to=200, resolution=0.5, orient=HORIZONTAL, command=self.saturation_action)
        self.saturation_slider.grid(row=3, column=2, padx=5, sticky='sw')
        self.saturation_slider.set(0)
    ## ADJUST ACTION END ##
    
    def apply_action(self):
        pass
    def cancel_action(self):
        pass
    def revert_action(self):
        pass
    
    ## APPLY FILTER FUNCTIONS TO ADD EFFECTS ##
    def negative_action(self):
        self.filtered_image = cv2.bitwise_not(self.edited_image)
        self.display_image(self.filtered_image)
        
    def bw_action(self):
        self.filtered_image = cv2.cvtColor(
            self.edited_image, cv2.COLOR_BGR2GRAY)
        self.filtered_image = cv2.cvtColor(
            self.filtered_image, cv2.COLOR_GRAY2BGR)
        self.display_image(self.filtered_image)
        
    def sepia_action(self):
        kernel = np.array([[0.272, 0.534, 0.131],
                            [0.349, 0.686, 0.168],
                            [0.393, 0.769, 0.189]])
        
        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)
        self.display_image(self.filtered_image)
    
    def sketch_action(self):
        ret, self.filtered_image = cv2.pencilSketch(
            self.edited_image, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
        self.display_image(self.filtered_image)
    
    def stylisation_action(self):
        self.filtered_image = cv2.stylization(
            self.edited_image, sigma_s=150, sigma_r=0.25)
        self.display_image(self.filtered_image)
        
    def emb_action(self):
        kernel = np.array([[0, -1, -1],
                           [1, 0, -1],
                           [1, 1, 0]])
        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)
        self.display_image(self.filtered_image)
        
    def erosion_action(self):
        kernel = np.ones((5, 5), np.uint8)
        self.filtered_image = cv2.erode(
            self.edited_image, kernel, iterations=1)
        self.display_image(self.filtered_image)
    
    def dilation_action(self):
        kernel = np.ones((5, 5), np.uint8)
        self.filtered_image = cv2.dilate(
            self.edited_image, kernel, iterations=1)
        self.display_image(self.filtered_image)
    
    def binary_threshold_action(self):
        ret, self.filtered_image = cv2.threshold(
            self.edited_image, 127, 255, cv2.THRESH_BINARY)
        self.display_image(self.filtered_image)
    ## APPLY FILTER FUNCTIONS TO ADD EFFECTS ##
    
    ## BLUR/SMOOTHENING ##
    def averaging_action(self, value):
        value = int(value)
        if value % 2 == 0:
            value += 1
        self.filtered_image = cv2.blur(self.edited_image, (value, value))
        self.display_image(self.filtered_image)
        
    def median_action(self, value):
        value = int(value)
        if value % 2 == 0:
            value += 1
            self.filtered_image = cv2.medianBlur(self.edited_image, value)
            self.display_image(self.filtered_image)
            
    def gaussian_action(self, value):
        value = int(value)
        if value % 2 == 0:
            value += 1
        self.filtered_image = cv2.GaussianBlur(
            self.edited_image, (value, value), 0)
        self.display_image(self.filtered_image)
    ## BLUR/SMOOTHENING ##
    
    def rotate_left_action(self):
        pass
    def rotate_right_action(self):
        pass
    def vertical_action(self):
        pass
    def horizontal_action(self):
        pass
    
    def brightness_action(self):
        pass
    def saturation_action(self):
        pass
    
    def display_image(self, image=None):  ## Function will remove old canvas ##
        self.canvas.delete("all")
        
        if image is None: ## Will show previously edited image if image is not passed ##
            image = self.edited_image.copy()
        else:
            image = image 
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) ## coverts BGR color scheme into RGB to render properly ##
        height, width, channels = image.shape
        ratio = height / width
        
        new_width = width
        new_height = height
        
        if height > 400 or width > 300: ## conditional to resize image if it is larger than specified ##
            if ratio < 1:
                new_width = 300
                new_height = int(new_width * ratio)
            else:
                new_height = 400
                new_width = int(new_height * (width / height))
                
        self.ratio = height / new_height
    
        self.new_image = cv2.resize(image, (new_width, new_height))
        
        self.new_image = ImageTk.PhotoImage(
            Image.fromarray(self.new_image))
        
        self.canvas.config(width=new_width, height=new_height)
        self.canvas.create_image(
            new_width / 2, new_height / 2, image=self.new_image)
        
    
    
root = Tk()
FrontEnd(root)
root.mainloop()
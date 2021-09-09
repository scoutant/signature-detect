import numpy as np
import imageio
from craft_text_detector import Craft

craft = Craft(output_dir='output', crop_type="box", cuda=False, export_extra=True) # or cuda=True

def detect(url:str)->bool:
    print(f'Craft detection for {url} ...')
    image: np.ndarray = np.array( imageio.imread(url)) # imread(.) returns a imageio.core.util.Image that IS a Numpy ndarray...

    result = craft.detect_text(image)
    if len(result['boxes'])==0: # image with no text at all
        print("no text here")
        return False
    print("nb of boxes" , result['boxes'].shape[0])
    return is_signature(result)

dw=0.3
dh=0.25
def is_nw(box): # [0.82584153 0.79851147] [0.89945924 0.83282135] [0.8927885  0.91054388] [0.81917073 0.876234  ]
    """ box is in upper left part if pixel # 3 is in upper left part (ensuring the full box is) """
    return box[2][0]<=dw and box[2][1]<= dh

def is_ne(box):
    return box[3][0]>=1-dw and box[3][1]<= dh

def is_se(box):
    return box[0][0]>=1-dw and box[0][1]>= 1-dh

def is_sw(box):
    return box[1][0]<=dw and box[1][1]>= 1-dh

def is_corner(box)->bool:
    """
    true if the box is located in any corner. A box happen to be a 4-pixel list in order
    1 -- 2
    4 -- 3
    """
    return is_nw(box) or is_ne(box) or is_se(box) or is_sw(box)

dhhf=0.2 # dh for header and footer
def is_footer(box)->bool:
    """ true if for the 2 first points, y>0.8 """
    return box[0][1]>=1-dhhf and box[1][1]>=1-dhhf

def is_header(box)->bool:
    """ true if for the 2 last points, y<0.2 """
    return box[2][1]<=dhhf and box[3][1]<=dhhf

def is_signature(prediction_result) -> bool:
    """ true if any of the boxes is at any corner """
    for box in prediction_result['boxes_as_ratios']:
        if is_corner(box) or is_header(box) or is_footer(box):
            print("signature detected")
            return True
    return False

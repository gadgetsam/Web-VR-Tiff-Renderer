from PIL import Image
import os
import numpy as np
import shutil
import math
from scipy import misc, ndimage, io
import ntpath
ntpath.basename("a/b/c")
import json
def readTiff(filepath, onlyOneFile=True, axis=0,updater=None):
    try:
        shutil.rmtree("static/data/test")
    except:
        pass
    filename = "test"
    im = Image.open(filepath)

    try:

        os.mkdir("static/data/"+filename)
    except:
        pass

    h,w = im.width, im.height
    tiffarray = np.zeros((w, h, im.n_frames))

    try:
        os.mkdir("static/data/" + filename + "/" + str(0))
        for i in range(im.n_frames):
            im.seek(im.tell()+1)
            image1 = misc.fromimage(im, flatten=1)
            tiffarray[:, :, i] = np.array(image1)
            # misc.imsave("static/data/test/0/"+str(im.tell())+".png", image1)
    except EOFError:
        pass # end of sequence
    dim = tiffarray.shape
    if onlyOneFile:
        misc.imsave("static/data/"+filename+"/"+str(1)+".png", simple_slice(tiffarray, math.floor(dim[axis]/2), axis))
    else:
        for i in range(1, dim[axis]+1):
            updater.setValue((i/(dim[axis]+1))*100)

            misc.imsave("static/data/"+filename+"/"+str(i)+".png", simple_slice(tiffarray, i-1, axis))

    infoFile = {"numImages":dim[axis]+1, "height":simple_slice(tiffarray, 0, axis).shape[0], "width":simple_slice(tiffarray, 0, axis).shape[1]}
    with open("static/test.js", 'w') as outfile:
        outfile.write("var configuration ="+str(json.dumps(infoFile)))
    # print(tiffarray)
    return filename
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
def simple_slice(arr, inds, axis):
    # this does the same as np.take() except only supports simple slicing, not
    # advanced indexing, and thus is much faster
    sl = [slice(None)] * arr.ndim
    sl[axis] = inds
    return arr[sl]
# readTiff("butterfly_wing_small.tif")



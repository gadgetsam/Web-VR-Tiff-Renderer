from PIL import Image
import os
import numpy as np
import shutil
from scipy import misc, ndimage, io
import ntpath
ntpath.basename("a/b/c")
import json
def readTiff(filepath):
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
    infoFile = {"numImages":im.n_frames, "height":im.height, "width":im.width}
    with open("static/test.js", 'w') as outfile:
        outfile.write("var configuration ="+str(json.dumps(infoFile)))
    h,w = im.width, im.height
    tiffarray = np.zeros((w, h, im.n_frames))

    try:
        for i in range(im.n_frames):
            im.seek(im.tell()+1)
            image1 = misc.fromimage(im, flatten=1)
            tiffarray[:, :, i] = np.array(image1)
            # misc.imsave("static/data/"+filename+"/"+str(im.tell())+".png", image1)
    except EOFError:
        pass # end of sequence
    dim = tiffarray.shape
    for x in range(3):
        os.mkdir("static/data/" + filename + "/" + str(x))
        for i in range(1,dim[x]+1):

            misc.imsave("static/data/"+filename+"/"+str(x)+"/"+str(i)+".png", simple_slice(tiffarray, i-1, x))

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
readTiff("butterfly_wing_small.tif")


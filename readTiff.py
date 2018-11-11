from PIL import Image
import os,glob
import numpy as np
import shutil
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc, ndimage, io
import ntpath
ntpath.basename("a/b/c")
import json
def readTiff(filepath, onlyOneFile=True, axis=0,updater=None, colormap='Greys',invert=False, folder=False):
    try:
        shutil.rmtree("static/data/test")
    except:
        pass
    filename = "test"

    try:

        os.mkdir("static/data")
    except:
        pass
    try:

        os.mkdir("static/data/"+filename)
    except:
        pass

    if folder:
        try:
            list_files = []
            for file in os.listdir(filepath):
                if file.endswith(".tiff") or file.endswith(".tif"):
                    list_files.append(os.path.join(filepath, file))
            im = Image.open(list_files[0])
            h, w = im.width, im.height
            tiffarray = np.zeros((w, h, len(list_files), 4))
            cm_hot = mpl.cm.get_cmap(colormap + ("_r" if invert else ""))
            os.mkdir("static/data/" + filename + "/" + str(0))
            for n,i in enumerate(list_files):
                im = Image.open(i)
                image1 = np.array(im)
                image1 = cm_hot(image1)
                image1 = np.uint8(image1 * 255)
                # image1 = misc.fromimage(im, flatten=1)
                tiffarray[:, :, n] = np.array(image1)
                # misc.imsave("static/data/test/0/"+str(im.tell())+".png", image1)
        except EOFError:
            pass  # end of sequence

    else:

        try:
            im = Image.open(filepath)
            h, w = im.width, im.height
            tiffarray = np.zeros((w, h, im.n_frames, 4))
            cm_hot = mpl.cm.get_cmap(colormap + ("_r" if invert else ""))
            os.mkdir("static/data/" + filename + "/" + str(0))
            for i in range(im.n_frames):
                im.seek(im.tell() + 1)
                image1 = np.array(im)
                image1 = cm_hot(image1)
                image1 = np.uint8(image1 * 255)
                # image1 = misc.fromimage(im, flatten=1)
                tiffarray[:, :, i] = np.array(image1)
                # misc.imsave("static/data/test/0/"+str(im.tell())+".png", image1)
        except EOFError:
            pass  # end of sequence

    dim = tiffarray.shape


    if onlyOneFile:
        slice = simple_slice(tiffarray, math.floor(dim[axis] / 2), axis)


        misc.imsave("static/data/"+filename+"/"+str(1)+".png", slice)
    else:
        for i in range(20, dim[axis]+1):
            updater.setValue((i/(dim[axis]+1))*100)

            misc.imsave("static/data/"+filename+"/"+str(i-20)+".png", simple_slice(tiffarray, i-1, axis))

    infoFile = {"numImages":dim[axis]+1-20, "height":simple_slice(tiffarray, 0, axis).shape[0], "width":simple_slice(tiffarray, 0, axis).shape[1]}
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
filepath = "C:\\Users\\gadge\\Downloads\\als\\New Folder With Items"
colormap="Greys"
filename ="test"
invert =True


from PIL import Image
import os
import shutil
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
    try:
        while False:
            im.seek(im.tell()+1)
            im.save("static/data/"+filename+"/"+str(im.tell())+".png")
    except EOFError:
        pass # end of sequence
    return filename
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

# readTiff("alkaseltzer1_combined_bin2.tif")
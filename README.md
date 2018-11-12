# Web VR Tiff Renderer

Web VR Tiff Renderer allows you to easily view your tiff stacks in VR. It accepts either a folder of single tiff images or a single tiff stack as input. It is compatible with the Vive, Oculus Rift, and Windows Mixed Reality Devices. This program will theoretically work with any size tiff stack but the larger the tiff stack the slower the performance will be. It is recommended that you keep the size below 300MB. 

## Install and Run

Web VR Tiff Renderer is tested on Python 3.7.1.

First download the repo and cd into it:

Then make sure you have all the packages:
> pip install -r requirements.txt

Run the script to open the GUI interface
>python Web-VR-Tiff-Renderer.py  

## Colormaps:

A list of all avaliable colormaps can be found here: https://matplotlib.org/examples/color/colormaps_reference.html

## Rendering Method:

We use a sliced rendering method for ease of computation. This sliced rendering method comes with a few drawbacks. One, when you look at the slices from the side, the model disappears. This is because the slices have no horizontal dimensions. To overcome this you can change the direction of the slices for the model in the GUI for the app. 



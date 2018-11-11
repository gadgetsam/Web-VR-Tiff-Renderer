# Web VR Tiff Renderer

Web VR Tiff Renderer allows you to easily view your tiff stacks in VR. It can take as an input either a folder of single tiff images or a single tiff stack. It is compatible with the Vive, Oculus, and Windows Mixed Reality Devices. This program can theoretically work with any size tiff stack but the larger the tiff stack the worse the performance. It is recommended that you keep the size below 300MB. 

## Install

Web VR Tiff Renderer is tested on Python 3.7.1.

First download the repo and cd into it:

Then make sure you have all the packages:
> pip install -r requirements.txt
 
## Tutorial:

Run the script to open the GUI interface
>python Web-VR-Tiff-Renderer.py  

Once you open the app follow the numbered directions to get the model into VR. Make sure to use the correct browser to insure compatibility with your headset: Chrome for Vive/Oculus and Edge for Windows Mixed Reality. The first thing to do when you enter VR is to bring the model towards you, to do this hold down the trigger and menu button(B button on Oculus Rift) on the right controller at the same time. To move the model around hold the right controller’s trigger and move your right hand in the direction you want to move it. 

## Rendering Method:

We use a sliced rendering method for ease of computation. This sliced rendering method comes with a few drawbacks. One, when you look at the slices from the side it is the model disappears this is because the slices have no horizontal dimensions. To overcome this drawback you can change the orientation in the GUI for the app. 



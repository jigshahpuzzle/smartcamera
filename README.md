# The Smart Camera
![alt tag](https://github.com/jigshahpuzzle/smartcamera/blob/master/product.jpg)

## Goals
There goals of the smart camera project are:   
* Cameras should be hands-free (wearable). We often want to capture fleeting moments with a camera, and a wearable camera saves time that is otherwise spent fumbling to turn on and aim a traditional camera. 
* Cameras should generate descriptive names for images. A picture of a waterfall named 'IMG_0679.jpg' makes it difficult to search for and show friends later; it should be automatically named 'waterfall.jpg'.
* Cameras should store images on our favorite cloud storage providers (OneDrive, Box, etc.). Transferring files from a SD card is slow and risks data loss.
* Cameras should be programmable. It should be easy to connect a camera to an Amazon Echo, for example, to add conversational UI to the camera. 

## Architecture 
There are 3 key components to the application:
* Hardware - This consists of a 3d printed sunglass with a camera mount, a Raspberry Pi Model 3, and a Picamera. The Picamera connects to the Pi with a ribbon, and can be attached to the sunglass with an adhesive.
* Camera Web Server - This is a micro server hosted on the Raspberry Pi that provides an HTTP interface to triggering the camera. On trigger, the camera takes a picture and uploads it to the Image Server.
* Image Web Server - This is a web service hosted on the cloud that generates a descriptive name for images using Microsoft's Computer Vision API and uploads it for cloud storage to a Microsoft OneDrive account.

## Files 
* The 'designs/' directory contains a SCAD and STL design of the sunglass with a camera mount. These files can be sliced and printed on a 3D printer using a softare like CURA. 
* The 'picamserver/' directory contains the lightweight Camera Web Server, and implements the Flask web framework.
* The 'imageserver/' directory conatins the connecting Image Server, and implements the Django web framework.

## Contributions
Simply fork the repository, and make a pull request with contributions. 


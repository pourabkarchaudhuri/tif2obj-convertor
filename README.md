# 3D Mesh Generation from Medical TIF Documents
##### A python based backend scripted pipeline to convert TIF to STL and OBJ
&nbsp;


![MESH](https://raw.githubusercontent.com/pourabkarchaudhuri/tif2obj-convertor/master/documentation_assets/input.gif)![MESH](https://raw.githubusercontent.com/pourabkarchaudhuri/tif2obj-convertor/master/documentation_assets/output.png)

<img src="https://raw.githubusercontent.com/pourabkarchaudhuri/tif2obj-convertor/master/documentation_assets/output.png" width="300" height="600">

## Description
Medical Imaging Techniques export multiple formats, out of which a commonly used medical imaging document format is .TIF documents. These images are of two types, Sequence TIF and single TIF. This code base converts TIFs of any kind under 24bit compression to be converted into data arrays, and generates a 3D mesh out of it to be able to use it in Unity for XR project implementation.

This codebase does the following steps:

  - Reading Medical Image Documents
  - Convert read images into data arrays
  - Create surface meshes based on adjusted threshold value
  - Export generated mesh volume as 3D asset files
  - Clean up buffer once job completes

## Inspiration
This project is greatly inspired multiple available tools in the market viz. Fiji, Amira, etc.

### Technology

This project uses a number of open source projects to work properly:

* [VTK] - A open source medical imaging library by Kitware
* [Python] - awesome language we love

### Environment Setup

##### This was built on `Windows 10` with a `16 GB DDR4 RAM` configuration
This project us very memory intensive so it is recommended to use 16GB RAM or above for edge computation or choosing VMs from any cloud provider.

#### Installation

This project requires the standard [Python](https://www.python.org/) 3.6+ to run

```sh
$ git clone https://github.com/pourabkarchaudhuri/tif2obj-convertor.git
$ cd tif2obj-convertor
$ pip install -r requirements.txt
```
#### To visualize a TIF Stack

```sh
$ python visualize_tif.py --path INPUT_FILE_PATH_HERE.tif
```
#### Run Mesh Generation Job using TIF Stack
```sh
$ python trigger_job.py --path INPUT_FILE_PATH_HERE.tif
```

#### Run TIF Stack creator from folder of multiple TIF images
```sh
$ python convert_image2tif.py --path INPUT_FILE_PATH_HERE.tif
```
#### For help with Command Line Arguements
```sh
$ python trigger_job.py -h
```
Now wait till you get the message "Complete", and the converted builds will be dropped with a generated filename at their respective output folders.


### Todos

 - Create job queues

License
----

Public


   [VTK]: <https://vtk.org/>
   [Python]: <https://www.python.org/>
  

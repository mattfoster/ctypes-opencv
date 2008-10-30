ctypes-opencv
=============

This README was created using text from the [ctypes-opencv ](http://code.google.com/p/ctypes-opencv/ "ctypes-opencv - Google Code") homepage on google code.

`ctypes-opencv` is a Python module which encapsulates the functionality of
Intel's Open Source Computer Vision Library ([OpenCV](http://wwwx.cs.unc.edu/~gb/wp/blog/2007/02/04/python-opencv-wrapper-using-ctypes/ "Python OpenCV wrapper using ctypes &#8212; Gary Bishop")). The Open Computer Vision
Library is a collection of algorithms and sample code for various computer
vision problems. The library is compatible with IPL and utilizes Intel
Integrated Performance Primitives for better performance. The goal of
`ctypes-opencv` is to give one Python access to all documented functionality of OpenCV.

Advantages
----------

Nearly complete access to all documented functionality of OpenCV version 1.0
No installation or compiler required, just import a single module named
'opencv' and run Cross platform, running on Windows, Linux, Mac OS X

Related Python wrappers for OpenCV
----------------------------------

OpenCV has its own swig-based Python wrapper supporting a limited number of
structures and functions. However, it is far from complete.

Another project called CVtypes was pioneered by Michael Otto and is currently
maintained by [Gary Bishop](http://wwwx.cs.unc.edu/~gb/wp/blog/2007/02/04/python-opencv-wrapper-using-ctypes/ "Python OpenCV wrapper using ctypes &#8212; Gary Bishop").
The wrapper is based on ctypes and supports a much larger of set of OpenCV's
functions and structures.

I used to provide some improvements to `CVtypes` here and there. While Prof.
Gary Bishop was a kind man, I felt not so nice to keep asking him to update
his code. Therefore, I decided to branch from his `CVtypes`, and the result is
this project. Though `ctypes-opencv` contains many more OpenCV's structures
and a few more OpenCV's functions compared to `CVtypes`, the main credit
should still go to the first two authors and a number of contributors whose
names can be found in the source code. I intend to eventually merge back to
Gary Bishop's `CVtypes` when the project is mature enough.

Bugs and Commentary
-------------------

Please send information on issues of usage to Minh-Tri Pham
<pmtri80@gmail.com>, or create an issue in the Issues pannel.
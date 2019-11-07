# RaspberryPi
Gravitational Acceleration Calculator using Raspberry Pi and Python OpenCV

This is the project I did as an intern at Extreme Light Infrastructure - Nuclear Physics (ELI-NP) research facility in Bucharest.

It consists of three parts:
  -> the hardware setup
  -> the Computer Vision algorithm
  -> the automation script
  
The aim of this project was to show highschool students that they could do science experiments using accesible software and hardware and some physics and math skills.
It was ultimately used as a reference for the annual students' summer camp, hosted by ELI-NP.

How does it work?
  -> a relay is powered up to generate a strong enough magnetic field to keep a metal ball in place, ready to be released.
  -> the metal ball is released in front of a Raspberry Pi V2 camera.
  -> the camera films the ball at over 990 fps.
  -> the resulting frames are decoded in .ppm format.
  -> a .py program containing the Computer Vision algorithm generates a .txt document containing the XY coordinates of the centre of the ball in all the captured frames. 
  -> a plot is generated based on the .txt document
  -> a .py program analyses the plot and generates the ultimate output - the gravitational acceleration.

This repo contains:
  -> /PICS: a folder containing some test pics
  -> /PROGRAM: contains the bash scripts and .py programs used in the project, as well as some frames and plots:
                -> experiment_setup - the main automated script
                -> relay_on.py - sets on the relay. the relay is now ready to catch the metal ball used for
                -> relay_off.py - releases the ball
                -> raw2ppm - bash script that converts .raw frames in .ppm frames.
                -> image2.py - generates the .txt document
                -> g.py - generates the output
  -> /TESTS: contains some generated .txt test documents for plotting
  -> /VIDS: videos of the ball falling, in .h264 format.
  -> Measuring the Gravitational Acceleration using Raspberry Pi.docx - full extensive documentation.
  
  The documentation contains details of how everything works, motivation, as well as pictures of the setup and outcome.

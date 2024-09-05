# Non-Functional Plant Watering Game

Author: Vishant Raajkumar

Design: The game was intended to be a game in which you have to find an optimal path to water all of your plants before they dry out.
        Unfortunately, my asset pipeline wasn't working so I have transformed it into a commentary on art (I recognize I'm getting no points for this).

Screen Shot:

![Screen Shot](screenshot.png)

How Your Asset Pipeline Works:

I made all of the source art in GIMP. I couldn't finish the rest of the pipeline because I was running into issues exporting from GIMP.
I basically tried to crop images with Microsoft's built-in photo editor in Windows 11, but I kept running into issues with the colors being off until
I realized that no one should ever use the built-in photo editor. 
In the file [link](asset_generation.py), I open each of the files with Python and PIL and parse the files to get the tiles and the palettes.
Unfortunately, I was unable to properly encode the values for the tiles so they're currently stored as tuples of numbers.
The intent was to take the results from the Python script and encode them into static arrays in PlayMode.cpp.

The source files for the art are present in the art folder.

How To Play:

Do nothing, observe the beautiful empty screen, and reflect on the meaning of art and life.

This game was built with [NEST](NEST.md).


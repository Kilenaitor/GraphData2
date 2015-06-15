#GraphData2
GraphData2 is a GDB plugin used for visualizing data structures in image format.
##Inspiration
Normally when debugging or teaching data structures, the developer has to write
a `print` function for the data structure so that they can visualize what the
structure looks like at that current point. This is usually done in some crude,
ASCII art-style, mess of `cout` statements just to get a visual that's only semi-coherent.

With GraphData, all of the visual work is handled by another library called GraphViz that,
when supplied with a `.txt` file containing data pertaining to a graph/chart/tree/etc.,
will draw the diagram to spec and output an image file.
An instructor or developer can simply call the plugin's `visualize` function
and get an image that represents the current state of the data structure! It's pretty cool :D

##Dependencies
GraphData depends on the GraphViz library to be installed on the machine.
A link for which can be found here:

http://www.graphviz.org/Download.php

Also, seeing as GraphData is a plugin for GDB it would probably be a good idea to have gdb installed on your system.

If you're on Mac OS, [here](http://ntraft.com/installing-gdb-on-os-x-mavericks/)'s a tutorial on how to install gdb.

##Usage
This plugin is implemented using GDB.

First, compile your C++ program with debugging by using the `-g` tag for `g++`.
Next, run gdb by calling `gdb -x src/pyviz.py`.
This will set the source of gdb to include the pyviz plugin.
Then load your binary file with `file <filename>`.

Then simply step through your program.
When you've reached a point you wish to visualize, simply call `visualize <structure>` from within gdb.
This will render out a `raw.txt` file that you can build using `dot`.  
Simply call `dot -T<format> -o<name> < raw.txt`  

For example, `dot -Tpng -ofile.png < raw.txt`  
That will generate out the png to see your data structure!  

##Work in Progress
Goal is to finish up the project as soon as possible.
Right now only the nodes will be drawn in the image file without any edges between them.
I'm working as fast as I can to get it finished and will keep this repo updated with progress.

Feel free to open an issue if something isn't working or you just want something add.
My QA department isn't exactly overstaffed.

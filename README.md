#GraphData2
GraphData2 is a GDB plugin used for visualizing data structures in image format.
##Inspiration
Normally when debugging or teaching data structures, the developer has to write
a `print` function for the data structure so that they can visualize what the
structure looks like at that current point. This is usually done in some crude,
ASCII art-style, mess of `cout` statements just to get a structure that's semi-coherent.

With GraphData, all of the work is handled by another library called GraphViz that
when supplied with a txt file containing data pertaining to a graph/chart/tree/etc.
will draw the diagram to spec and output an image file.
An instructor or developer can simply call the library's `print` function
and get an image that represents the current state of the data structure! Awesome :D

##Dependencies
GraphData depends on the GraphViz library to be installed on the machine.
A link for which can be found here:

http://www.graphviz.org/Download.php

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
Feel free to open an issue if something isn't working or you just want something addd.
My QA department isn't exactly overstaffed.

Visual Equalizer
========
Currently waiting for hardware (MSGEQ7 chip). Worked on some basic software to draw the equalizer with Python in this period.

eq_read_file.py reads and outputs to equalizer based on values from a text file.

The plan is:
MSGEQ7 will use send band frequency values to Arduino
Arduino will send data to Python and write to a file (for stage 1)
Equalizer script will read values from the file and output to equalizer.

<img src="https://raw.githubusercontent.com/a3alamgi/Visual_Equalizer/master/images/eq_basic.jpg"/>  
Figure 1: Basic visual equalizer
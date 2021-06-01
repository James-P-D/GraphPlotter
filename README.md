# GraphPlotter
Graph Plotter in Python using Tkinter

![Screenshot](https://github.com/James-P-D/GraphPlotter/blob/master/screenshot.gif)

## Introduction

This project was simply created so I could try using the [TKinter](https://docs.python.org/3/library/tkinter.html) GUI library.

Obviously if you need a real data visualisation tool for Python, you should be using [matplotlib](https://matplotlib.org/).

## Usage

After running the application you will be presented with a small UI. Simply enter the values for `Min X`, `Max X`, `Min Y` and `Max Y` for scaling the x and y axes, then choose whether you want to plot `x =` or `y =` from the drop-down list. Finally, enter a valid equation and press the <kbd>Plot</kbd> button to plot the graph.

Note that the program makes use of `eval()` which is widely considered [dangerous, insecure, slow and hard to debug](https://stackoverflow.com/questions/1832940/why-is-using-eval-a-bad-practice). It will suffice for this toy project, but in general there are few good reasons for `eval()` and should be avoided at all times!
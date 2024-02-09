# eROSITAViz
This repository allows users to explore and analyze eROSITA light curves in three energy bands 0.2-0.6 KeV, 0.2-0.6 KeV, and 2.3-5.0 KeV.
With just the input of the target's name or coordinates, users can access the available light curve in the south hemisphere of eROSITA DR1.

### First step
Download the repository and install dependencies following the next instruction:

```zsh
$ git clone https://github.com/javiserna/eROSITAViz
$ cd eROSITAViz
$ python setup.py install
```
### How to use it?
If you have the target name, run:

```zsh
$ python erositaviz.py "Star_name"
```
Alternatively, if you have the coordinates RA, DEC, run:

```zsh
$ python erositaviz.py "RA" "DEC"
```

The eROSITA Light Curve will be displayed. Enjoy exploring!

© Instituto de Astronomía / UNAM (Ensenada, B.C, Mexico)

Javier Serna (Feb 2024)


# eROSITAViz
This repository allows users to explore and analyze eROSITA light curves using the energy band of 0.2-5.0 KeV.
With just the input of the target's name or coordinates, users can access the available light curve.

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
$ python eROSITAViz.py "Star_name"
```
Alternatively, if you have the coordinates RA, DEC, run:

```zsh
$ python eROSITAViz.py "RA" "DEC"
```

The eROSITA Light Curve will be displayed. Enjoy exploring!

© Instituto de Astronomía / UNAM (Ensenada, B.C, Mexico)

Javier Serna (Feb 2024)


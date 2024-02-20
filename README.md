<img src="https://github.com/javiserna/eROSITAViz/blob/main/eROSITAViz.png?raw=true" width="400"/>

# eROSITAViz
This repository offers a quick and convenient way to visualize light curves and spectra from eROSITA DR1.

eROSITAViz enables users to explore eROSITA light curves and spectra across the energy band: 0.2-10 KeV. With just the input of the target's name or coordinates, users can access available data.

### First step
To get started, follow these steps to download the repository and install the required dependencies:

```zsh
$ git clone https://github.com/javiserna/eROSITAViz
$ cd eROSITAViz
$ python setup.py install
```
### How to use it?
Once you have installed the dependencies, you can use the tool as follows:

If you have the target name, run:

```zsh
$ python erositaviz.py "Star_name"
```
Alternatively, if you have the coordinates RA, DEC, run:

```zsh
$ python erositaviz.py "RA" "DEC"
```

This will display the eROSITA light curve for the specified target. Enjoy exploring!

### Acknowledgements
This project was developed and maintained by Javier Serna, Instituto de Astronomía, UNAM (Ensenada, B.C, Mexico).

© 2024

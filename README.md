<img src="https://github.com/javiserna/eROSITAViz/blob/main/eROSITAViz.png?raw=true" width="400"/>

# eROSITAViz
This repository offers a quick and convenient way to visualize light curves and spectra from eROSITA DR1.

eROSITAViz enables users to explore the available eROSITA data with just the input of the target's name or coordinates.

### First step
To get started, follow these steps to download the repository and install the required dependencies:

```zsh
$ git clone https://github.com/javiserna/eROSITAViz
$ cd eROSITAViz
$ python setup.py install
```
### How to use it?
Once you have installed the dependencies, you can use the tool as follows:

If you have the target name (Only SIMBAD Names), run:

```zsh
$ python erositaviz.py "Star_name"
```
Alternatively, if you have the coordinates RA, DEC, run:

```zsh
$ python erositaviz.py "RA" "DEC"
```
This will display the eROSITA light curve for the specified target. Enjoy exploring!

For instance, the star "AB Dor" is a strong X-ray source, so an active star.
<img src="https://github.com/javiserna/eROSITAViz/blob/main/demo/AB_Dor_eRASS1_LC.png?raw=true" width="400"/> <img src="https://github.com/javiserna/eROSITAViz/blob/main/demo/AB_Dor_eRASS1_spec.png?raw=true" width="400"/>


### Acknowledgements
This project was developed and maintained by Javier Serna, Instituto de Astronomía, UNAM (Ensenada, B.C, Mexico).

© 2024

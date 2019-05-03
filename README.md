# Stable and manipulable Bloch point
Marijan Beg<sup>1,2</sup>, Ryan A. Pepper<sup>2</sup>, David Cortes-Ortuno<sup>2</sup>, Bilal Atie<sup>2</sup>, Marc-Antonio Bisotti<sup>2</sup>, Gary Downing<sup>2</sup>, Thomas Kluyver<sup>1</sup>, Ondrej Hovorka<sup>2</sup>, and Hans Fangohr<sup>1,2</sup>

<sup>1</sup> *European XFEL GmbH, Holzkoppel 4, 22869 Schenefeld, Germany*  
<sup>2</sup> *Faculty of Engineering and Physical Sciences, University of Southampton, Southampton SO17 1BJ, United Kingdom*  

| Description | Badge |
| --- | --- |
| Binder | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/marijanbeg/2019-paper-bloch-point-stability/master?filepath=index.ipynb) |
| License | [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) |

## About

This repository contains simulation and data analysis scripts used to obtain results in [Beg, M. et al. Stable and manipulable Bloch point. arXiv 1808.10772 (2018)](https://arxiv.org/abs/1808.10772).

## Micromagnetic simulations

Simulations scripts used to run micromagneyic simulations using [Finmag](https://github.com/fangohr/finmag) are in `src/` directory. In order to run them, please run

    make all

Micromagnetic simulations will be run inside [Docker](https://www.docker.com/) container, which contains all the necessary software. Therefore, please make sure you have Docker installed on your machine. Installation instructions can be found [here](https://docs.docker.com/install/). Runtime is approximatelly 2 hours.

If you would like only to reproduce the plots from the publication, there is no need to run micromagnetic simulations again, because all the `*.pkl` files required are already a part of this repository. However, VTK files of vector fields are not a part of it due to their size. Acordingly, if you would like to create them, please run micromagnetic simulations again (`make all`).

## Figures

Scripts for creating Figures 2, 3, and 4 from the publication are in Jupyter notebooks which can be found in `figures/` directory. These notebooks can also be run in the cloud via [Binder](https://mybinder.org/v2/gh/marijanbeg/2019-paper-bloch-point-stability/master?filepath=index.ipynb). This does not require you to have anything installed and no files will be created on your machine.

## License

Licensed under the BSD 3-Clause "New" or "Revised" License. For details, please refer to the [LICENSE](LICENSE) file.

## How to cite

1. Beg, M. et al. Stable and manipulable Bloch point. arXiv 1808.10772 (2018).

2. DOI for this repository will be available soon

## Acknowledgements

This work was financially supported by the OpenDreamKit – Horizon 2020 European Research Infrastructure project (676541), EPSRC Centre for Doctoral Training grant EP/L015382/1, and the EPSRC Programme grant on Skyrmionics (EP/N032128/1).

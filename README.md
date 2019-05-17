# Stable and manipulable Bloch point
Marijan Beg<sup>1,2</sup>, Ryan A. Pepper<sup>2</sup>, David Cortes-Ortuno<sup>2</sup>, Bilal Atie<sup>2</sup>, Marc-Antonio Bisotti<sup>2</sup>, Gary Downing<sup>2</sup>, Thomas Kluyver<sup>1</sup>, Ondrej Hovorka<sup>2</sup>, and Hans Fangohr<sup>1,2</sup>

<sup>1</sup> *European XFEL GmbH, Holzkoppel 4, 22869 Schenefeld, Germany*  
<sup>2</sup> *Faculty of Engineering and Physical Sciences, University of Southampton, Southampton SO17 1BJ, United Kingdom*  

| Description | Badge |
| --- | --- |
| Preprint | [![Preprint](https://img.shields.io/badge/arXiv-1808.10772-red.svg)](https://arxiv.org/abs/1808.10772) |
| Binder | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marijanbeg/2019-paper-bloch-point-stability/master?filepath=index.ipynb) |
| Build | [![Build Status](https://travis-ci.org/marijanbeg/2019-paper-bloch-point-stability.svg?branch=master)](https://travis-ci.org/marijanbeg/2019-paper-bloch-point-stability) |
|       | [![Build status](https://ci.appveyor.com/api/projects/status/liuuyc7p7gyexs8m?svg=true)](https://ci.appveyor.com/project/marijanbeg/2019-paper-bloch-point-stability) |
| License | [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) |

## About

This repository contains simulation and data analysis scripts used to obtain results in [Beg, M. et al. Stable and manipulable Bloch point. arXiv 1808.10772 (2018)](https://arxiv.org/abs/1808.10772).

## Micromagnetic simulations

Simulation scripts used to run micromagnetic simulations using [Finmag](https://github.com/fangohr/finmag) are in `src/` directory. In order to run them, please run

    make all

If you would like only to reproduce the plots from the publication, there is no need to run micromagnetic simulations again, because all the `*.txt` files required are already a part of this repository. However, VTK files of vector fields are not a part of it due to their size. Accordingly, if you would like to create them, please run micromagnetic simulations again (`make all`). For the visualisation and the analysis of VTK files, package like [Paraview](https://www.paraview.org/) can be used.

#### Docker

Micromagnetic simulations will be run inside [Docker](https://www.docker.com/) container, which contains all the necessary software. Therefore, please make sure you have Docker installed on your machine. Installation instructions can be found [here](https://docs.docker.com/install/). Runtime is approximatelly 2 hours.

Docker image required to run micromagnetic simulations is `marijanbeg/bloch_point:finmag` and it publicly available in [Docker Cloud](https://cloud.docker.com/repository/docker/marijanbeg/bloch_point). If Docker is installed and `make all` is run, it will be pulled automatically. Alternatively, it can be obtained from the Zenodo record under [10.5281/zenodo.2873744](https://zenodo.org/deposit/2873744) DOI. After downloading the Docker image file, before running `make all`, first run `make load-image`.

## Figures

Scripts for creating plots in Figures 2, 3, and 4 from the publication are in Jupyter notebooks which can be found in `figures/` directory. These notebooks can also be run in the cloud via [Binder](https://mybinder.org/v2/gh/marijanbeg/2019-paper-bloch-point-stability/master?filepath=index.ipynb). This does not require you to have anything installed and no files will be created on your machine.

Alternatively, if you decide to run notebooks on your machine, apart from Python 3, you will need to install the requirements:

    python3 -m pip install -r requirements.txt

## How to cite

1. Beg, M. et al. Stable and manipulable Bloch point. arXiv 1808.10772 (2018).

2. DOI for this repository will be available soon

## License

Licensed under the BSD 3-Clause "New" or "Revised" License. For details, please refer to the [LICENSE](LICENSE) file.

## Acknowledgements

This work was financially supported by the [OpenDreamKit](https://opendreamkit.org/) – Horizon 2020 European Research Infrastructure project (676541), EPSRC Centre for Doctoral Training grant [EP/L015382/1](http://www.ngcm.soton.ac.uk/), and the EPSRC Programme grant on Skyrmionics [EP/N032128/1](https://www.skyrmions.ac.uk/).

# Stable and manipulable Bloch point
Marijan Beg<sup>1,2</sup>, Ryan A. Pepper<sup>2</sup>, David Cortes-Ortuno<sup>2</sup>, Bilal Atie<sup>2</sup>, Marc-Antonio Bisotti<sup>2</sup>, Gary Downing<sup>2</sup>, Thomas Kluyver<sup>1</sup>, Ondrej Hovorka<sup>2</sup>, and Hans Fangohr<sup>1,2</sup>

<sup>1</sup> *European XFEL GmbH, Holzkoppel 4, 22869 Schenefeld, Germany*  
<sup>2</sup> *Faculty of Engineering and Physical Sciences, University of Southampton, Southampton SO17 1BJ, United Kingdom*  

| Description | Badge |
| --- | --- |
| Paper | [![Paper](https://img.shields.io/badge/Scientific%20Reports-9%3A7959%20(2019)-blue.svg)](https://www.nature.com/articles/s41598-019-44462-2) |
| Preprint | [![Preprint](https://img.shields.io/badge/arXiv-1808.10772-green.svg)](https://arxiv.org/abs/1808.10772) |
| Binder | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marijanbeg/2019-paper-bloch-point-stability/HEAD?urlpath=lab/tree/figures%2Findex.ipynb) |
| Tests | [![workflow](https://github.com/marijanbeg/2019-paper-bloch-point-stability/workflows/workflow/badge.svg)](https://github.com/marijanbeg/2019-paper-bloch-point-stability/actions) |
|       | [![docker-image](https://github.com/marijanbeg/2019-paper-bloch-point-stability/workflows/docker-image/badge.svg)](https://github.com/marijanbeg/2019-paper-bloch-point-stability/actions) |
| License | [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) |
| DOI | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2938933.svg)](https://doi.org/10.5281/zenodo.2938933) |

## About

This repository contains simulation, data analysis, and plotting scripts used to obtain results reported in  

- M. Beg *et al.* Stable and manipulable Bloch point. [*Scientific Reports* **9**, 7959](https://www.nature.com/articles/s41598-019-44462-2) (2019).

## Micromagnetic simulations

Simulation scripts for running micromagnetic simulations using [Finmag](https://github.com/fangohr/finmag) are in `src/` directory. In order to run all simulations, run

    $ make all

If you only want to reproduce plots from the publication, there is no need to run micromagnetic simulations again, because all required `*.txt` files containing data are already in this repository. However, VTK and HDF5 files of vector fields are not in the repository due to their size. Therefore, if you would like to create them, you need to run micromagnetic simulations again (`make all`). For the visualisation and the analysis of VTK files, package like [Paraview](https://www.paraview.org/) can be used.

**Docker**

Micromagnetic simulations are run inside [Docker](https://www.docker.com/) container, which contains all the necessary software. Therefore, please make sure you have Docker installed on your machine - installation instructions can be found [here](https://docs.docker.com/install/). Docker image required to run micromagnetic simulations is `marijanbeg/bloch_point:finmag` and it is publicly available on [DockerHub](https://cloud.docker.com/repository/docker/marijanbeg/bloch_point). If Docker is installed and `make all` is run, Docker image will be pulled automatically and simulations will be executed in Docker container (runtime is approximatelly 2 hours). Alternatively, Docker image can be obtained from the Zenodo record with [10.5281/zenodo.2873744](https://zenodo.org/record/2873744) DOI. After downloading Docker image file and before running `make all`, run `make load-image` first.

## Figures

Scripts for making plots in Figures 2, 3, and 4 from the publication are in Jupyter notebooks which can be found in `figures/` directory. These notebooks can also be run in the cloud via [myBinder](https://mybinder.org/v2/gh/marijanbeg/2019-paper-bloch-point-stability/HEAD?urlpath=lab/tree/figures%2Findex.ipynb).

## License

Licensed under the BSD 3-Clause "New" or "Revised" License. For details, please refer to the [LICENSE](LICENSE) file.

## How to cite

1. M. Beg *et al.* Stable and manipulable Bloch point. [*Scientific Reports* **9**, 7959](https://www.nature.com/articles/s41598-019-44462-2) (2019).

2. M. Beg *et al.* Stable and manipulable Bloch point. GitHub: https://github.com/marijanbeg/2019-paper-bloch-point-stability, DOI: [10.5281/zenodo.2938933](http://doi.org/10.5281/zenodo.2938933) (2019).

## Acknowledgements

- [OpenDreamKit](http://opendreamkit.org/) – Horizon 2020 European Research Infrastructure project (676541)

- EPSRC Programme Grant on [Skyrmionics](http://www.skyrmions.ac.uk) (EP/N032128/1)

- EPSRC [Centre for Doctoral Training](http://www.ngcm.soton.ac.uk/) grant (EP/L015382/1)

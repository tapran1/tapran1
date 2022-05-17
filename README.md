INSTALLATION GUIDE

To run the code, you need to have an Anaconda (Jupyter Notebook).

Anaconda is a Python and R programming language distribution aimed for simplifying package management and deployment in scientific computing (data science, machine learning applications, large-scale data processing, predictive analytics, and much more). The distribution includes data-science packages suitable for Windows, Linux, and macOS. 

To download anaconda click the below link 

https://www.anaconda.com/products/distribution#download-section

Then you have to install a library called “Geemap”. 

To use geemap, you must first sign up for a Google Earth Engine account.
geemap is also available on conda-forge. If you have Anaconda or Miniconda installed on your computer, you can create a conda Python environment to install geemap:

conda create -n gee python=3.9

conda activate gee

conda install geopandas

conda install mamba -c conda-forge

mamba install geemap localtileserver -c conda-forge

Optionally, you can install Jupyter notebook extensions, which can improve your productivity in the notebook environment. Some useful extensions include Table of Contents, Gist-it, Autopep8, Variable Inspector, etc. See this post for more information.

conda install jupyter_contrib_nbextensions -c conda-forge

To install the development version from GitHub directly within Jupyter notebook without using Git, run the following code:

import geemap

geemap.update_package()

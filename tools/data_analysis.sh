#!/bin/sh
#Starting Jupyter Notebook

PROJECTDIR=/MyApp

#Starting Jupyter
cd $PROJECTDIR && jupyter notebook --ip 0.0.0.0 --allow-root;
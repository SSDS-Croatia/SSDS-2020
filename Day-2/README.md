# SSDS 2020  - [5<sup>th</sup> Int'l Summer School on Data Science](https://sites.google.com/view/ssdatascience2020)

## Day 2 - Networks, Time, and Higher-Order Models

On the second day of the school you will learn how network methods can be invalidated by sequential patterns in the transitions between nodes, and how higher-order models extend the applicability of networks while accounting for those patters.
In the hands-on session you will learn how to use [pathpy](http://www.pathpy.net/), an Open Source python package providing higher-order network analytics for time series data.

### Lecture materials and outline


#### Networks, Time, and Higher-Order Models ([Ingo Scholtes](https://www.ingoscholtes.net/))

- 08:45 - 10:15

Network-based data mining techniques such as graph mining, (social) network analysis, link prediction and graph clustering are a cornerstone for data science applications in computer science, computational social science, and the life sciences. They help to detect patterns in large data sets that capture \dyadic relations between pairs of genes, species, humans, or documents and have improved our understanding of complex networks. While the potential of analysing graph or network models is undisputed, we increasingly have access to data on networks that contain more than just dyadic relations. Consider, e.g., data on user clickstreams in the Web, timestamped social networks, gene regulatory pathways, or timestamped financial transactions. These are examples for time-resolved or sequential relational data that not only tell us who is related to whom but also when and in which order relations occur. 

Such data pose a important challenges for state-of-the-art graph mining and network analysis techniques. Most of those techniques discard information on the microscopic timing and ordering of links, which is, however, the foundation of so-called time-respecting paths or causal paths. Recent works have exposed that the timing and ordering of relations in such data can introduce higher-order, non-dyadic dependencies that are not captured by state-of-the-art graph representations. Addressing this critical issue when analyzing time-series data, this lecture motivates challenges in the modelling and analysis of temporal networks, and shows how we can address them through higher-order models of causal paths.

#### Hands-on sessions ([Vincenzo Perri](https://www.ifi.uzh.ch/en/dag/people/perri.html))
- 10:30 - 12:00  Data science with python and introduction to pathpy 
- 13:30 - 15:30  Network science and Higher-Order Network Analysis with pathpy 

[pathpy](http://www.pathpy.net/)  is an Open Source python package providing higher-order network analytics for time series data.
pathpy is tailored to analyse time-stamped network data as well as sequential data that capture multiple short paths observed in a graph or network. Examples for data that can be analysed with pathpy include high-resolution time-stamped network data, dynamic social networks, user click streams on the Web, biological pathway data, citation graphs, passenger trajectories in transportation networks, or information propagation in social networks.
Unifying the analysis of time series data on networks, pathpy provides efficient methods to extract causal or time-respecting paths in time-stamped social networks. It facilitates the analysis of higher-order dependencies and uses principled model selection techniques to infer models that capture both topological and temporal characteristics. It allows to answer the question when network models of time series data are justified and when higher-order models are needed.
pathpy is fully integrated with jupyter, providing rich interactive visualisations of networks, temporal networks, higher-, and multi-order models. Visualisations can be exported to HTML5 files that can be shared and published on the Web

##### Hands-on environment setup instructions

The hands-on session is organized as [Jupyter](http://jupyter.org)
notebooks, which you can run on your local computer, 
Preparation for the hands-on session consists of setting up a python
environment, installing pathpy and Jupyter.
Instructions on getting started with pathpy are available at: http://www.pathpy.net/tutorial/

The suggested environment for the hands-on session is [Conda](https://conda.io/). 
After installing Conda on your machine (instructions on linked website), you will need the following additional packages:

- `juypter` - provides an environment for interactive data science projects in your browser. We will extensively use so-called jupyter notebooks, which are interactive computable documents that you can also use to compile reports.
- `pathpy` - provides implementations of common scientific and statistical computing techniques for python.
- `scipy` - provides implementations of common scientific and statistical computing techniques for python.
- `numpy` - provides support for multi-dimensional arrays an matrices as well as high-level mathematical functions. This project originated as a smaller core part of scipy.
- `matplotlib` - provides advanced plotting functions based on the data types introduced in numpy. Visualisations can be directly integrated into jupyter notebooks.
- `pandas` - popular package for the management, analysis, and manipulation of multi-dimensional panel data (thus the name). Provides convenient interfaces for the import and export of data from files or databases.


To install the packages above, except for pathpy,just run the following command in the terminal for each of the packages above:

```
> pip install PACKAGENAME
```
If you see no error messages, you should be all set to continue with the next steps.

Since pathpy is not included in the default Anaconda installation, we first need to install it. We are are currently in the process of finishing 3.0 revised version, which comes with many advantages. It has a cleaner API, is more efficient, and provides advanced plotting functions. 
To benefit from those advantages, we will use the development version of pathpy3 from gitHub. The best way to install it is to 
(1) clone the git repository to a local directory, and 
(2) install an editable version of the pathpy module from this cloned repository. 
This allows you to run git pull to get the latest version. You can do this by opening a command line as administrator and run:

```
> git clone https://github.com/pathpy/pathpy pathpy3
> cd pathpy3
> pip install -e .
```

This will create a new directory pathpy3 on your machine. Changing to this directory and running `pip install -e .` will install pathpy as an editable python module.



##### References


- Martin Rosvall, Alcides V Esquivel, Andrea Lancichinetti, Jevin D West, and Renaud Lambiotte: **Memory in network flows and its effects on spreading dynamics and community detection**. Nature communications (2014)

- Petter Holme. 2015. **Modern temporal network theory: a colloquium**. The European Physical Journal B88, 9 (2015)

- R Lambiotte, M Rosvall, I Scholtes: **From Networks to Optimal Higher-Order Models of Complex Systems**, Nature Physics, March 2019,  [arXiv 1806.05977](https://arxiv.org/abs/1806.05977)

- I Scholtes: **When is a Network a Network? Multi-Order Graphical Model Selection in Pathways and Temporal Networks**, In KDD'17, February 2017, [arXiv 1702.05499](https://arxiv.org/abs/1702.05499)

- I Scholtes, N Wider, R Pfitzner, A Garas, CJ Tessone, F Schweitzer: **Causality-driven slow-down and speed-up of diffusion in non-Markovian temporal networks**, In Nature Communications, September 2014, [arXiv 1307.4030](http://arxiv.org/abs/1307.4030)

- Ingo Scholtes, Nicolas Wider, and Antonios Garas: **Higher-order aggregate networks in the analysis of temporal networks: path structures and centralities**. The European Physical Journal B89, 3 (02 Mar 2016), 61.  

- V Perri, I Scholtes: **HOTVis: Higher-Order Time-Aware Visualisation of Dynamic Graphs**, Graph Drawing 2020, (https://arxiv.org/abs/1908.05976)

- Luka V. Petrović, Ingo Scholtes: **Learning the Markov order of paths in a network**, pre-print (https://arxiv.org/abs/2007.02861)




# SSDS 2020  - [5<sup>th</sup> Int'l Summer School on Data Science](https://sites.google.com/view/ssdatascience2020)

## Day 3 - Intersections between Complexity Science, Network Science and Data Science

On the third day of the school you will learn practical applications of complex networks methodologies to data science related problems. In the hands-on session you will learn how to use [graph-tool](https://graph-tool.skewed.de/), Python library for efficient statistical analysis of graphs.

### Lecture materials and outline


#### Statistical inference of large-scale network structures ([Tiago P. Peixoto](https://skewed.de/tiago))

One of the main computational and scientific challenges in the modern
age is to extract useful information from unstructured texts. Topic
models are one popular machine-learning approach that infers the latent
topical structure of a collection of documents. Despite their
success—particularly of the most widely used variant called latent
Dirichlet allocation (LDA)—and numerous applications in sociology,
history, and linguistics, topic models are known to suffer from severe
conceptual and practical problems, for example, a lack of justification
for the Bayesian priors, discrepancies with statistical properties of
real texts, and the inability to properly choose the number of
topics. 

In this lecture I will present a fresh view of the problem of
identifying topical structures by relating it to the problem of finding
communities in complex networks. This is achieved by representing text
corpora as bipartite networks of documents and words. By adapting
existing community-detection methods (using a stochastic block model
(SBM) with nonparametric priors), we obtain a more versatile and
principled framework for topic modeling (for example, it automatically
detects the number of topics and hierarchically clusters both the words
and documents). I will show how the analysis of artificial and real
corpora demonstrates that the SBM approach leads to better topic models
than LDA in terms of statistical model selection.

##### References

- Martin Gerlach, Tiago P. Peixoto, Eduardo G. Altmann, "A network approach to topic models"
Science Advances 4 eaaq1360 (2018), https://dx.doi.org/10.1126/sciadv.aaq1360, https://arxiv.org/abs/1708.01677


#### Hands-on session: The graph-tool Python module for network analysis ([Tiago P. Peixoto](https://skewed.de/tiago))

[graph-tool](https://graph-tool.skewed.de) is an efficient Python module
for manipulation and statistical analysis of networks.

Contrary to other python modules with similar functionality, the core
data structures and algorithms are implemented in C++, making extensive
use of template metaprogramming, based heavily on the Boost Graph
Library. This confers it a level of performance that is comparable (both
in memory usage and computation time) to that of a pure C/C++ library.

Besides general-purpose algorithms, the library includes implementations
of the [inference
algorithms](https://graph-tool.skewed.de/static/doc/demos/inference/inference.html)
discussed in the previous lectures.

##### Hands-on environment setup instructions

The hands-on session is organized as [Jupyter](http://jupyter.org)
notebooks, which you can run on your local computer, but also using
Google's [colaboratory](https://colab.research.google.com).

Preparation for the hands-on session consists of setting up a python
environment, installing graph-tool and Jupyter.

Installation instructions for graph-tool are available at: https://git.skewed.de/count0/graph-tool/-/wikis/installation-instructions

Many environments are supported, but the easiest one is probably
[Conda](https://conda.io/). After installing Conda on your machine
(following the instructions on the website), you can install graph-tool
and Jupyter with the commands:

```
conda create --name gt -c conda-forge graph-tool
conda activate gt
conda install -n gt -c conda-forge ipython jupyter
```

Pleat take the time to install graph-tool and familiarize yourself with Jupyter before the hands-on session!

Graph-tool works natively only if you are using GNU/Linux or MacOS. If
you are using Windows, as an alternative you can follow the session
using Colaboratory, which does not require graph-tool to be installed
locally. An example of using graph-tool with Colaboratory can be seen
here:
https://colab.research.google.com/github/count0/colab-gt/blob/master/colab-gt.ipynb

---

### The interface of Complexity and Data Science ([Nino Antulov-Fantulin](https://www.ninoaf.com/))

Complexity science studies systems and problems that are composed of many components that may interact with each other in a dynamic and non-linear way. In this talk, I  will address several research directions and problems that are lying on the interface of complexity and data science. 
First, I will address two research problems related to the structure of networks: 
(i) How to select the set of nodes in a network that, when removed or (de)activated, can stop the spread of (dis)information, mitigate an epidemic, or disrupt a malicious system by fragmenting it into small components at the minimum overall cost;
To solve this optimization problem, I will present a method which is based on the spectral properties of a node-weighted Laplacian operator and combine it with a fine-tuning mechanism related to the weighted vertex cover problem.
(ii) What is the connection between directed graphs and geometry of statistical manifolds? 
Here, a novel node embedding method of directed graphs to statistical manifolds is presented, which is based on a global minimization of pairwise relative entropy and graph geodesics in a non-linear way. Each node is encoded with a probability density function over a measurable space.

Afterward, I will present two problems related to the dynamics on the complex networks:
(iii) How graph geodesics can unify continuous and discrete-time stochastic susceptible-infected-recovered processes on networks?
Here, a framework that is able to model continuous, discrete, and hybrid forms of (non-)Markovian susceptible-infected-recovered (SIR) stochastic processes on networks is described.
(iv) Can Neural Networks be used for controlling dynamical processes on complex networks? 
Here, a neural-network control (NNC) framework is introduced, which represents dynamical systems by neural ordinary different equations (neural ODEs). We find that NNC can learn control signals that drive networked dynamical systems into desired target states.

Finally, several Python notebooks (Colaboratory) are given to demonstrate the practical aspects of the discussed topics:

https://colab.research.google.com/drive/1CmSegGOFODjdbMJOcyH69m2tVI9OLWo4?usp=sharing

https://colab.research.google.com/drive/1RI_FuDc76H12BdNc2NEfL51j7cfRXqd7?usp=sharing

**References:**
* https://www.pnas.org/content/116/14/6554
* https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.2.033121
* https://arxiv.org/pdf/1905.10227.pdf
* https://arxiv.org/pdf/2006.09773.pdf

# SSDS 2020  - [5<sup>th</sup> Int'l Summer School on Data Science](https://sites.google.com/view/ssdatascience2020)

## Day 1 - Fundamentals of Network Science

On the first day of the school you will learn about....

### Lecture materials and outline

## Statistical inference of large-scale network structures ([Tiago P. Peixoto](https://skewed.de/tiago))

Networks form the backbone of a wide variety of complex systems, ranging
from food webs, gene regulation, social networks, transportation and the
internet. However, due to the sheer size and complexity of many of
theses systems, it remains an open challenge to formulate general
descriptions of their structures, and to extract such information from
data. Since networks are high-dimensional relational objects, they
cannot be directly inspected using basic tools, and instead require new
methodology. In this lecture, I will describe a principled approach to
this task, based on the elaboration of probabilistic generative models,
and their statistical inference from data.  In particular, I will
present a general class of generative models that describe the
multilevel modular structure of network systems, as well as efficient
algorithms to infer their parameters. I will highlight the common
pitfalls present in more heuristic methods of capturing this type of
structure, and demonstrate the efficacy of more principled methods based
on Bayesian statistics and statistical physics.

Throughout the lecture I will show applications using many empirical networks
such as the internet at the autonomous systems level, the global airport
network, the network of actors and films, social networks, citations among
websites, co-occurrence of disease-causing genes and others.

# References

- Tiago P. Peixoto, "Bayesian stochastic blockmodeling", in Advances in Network Clustering and Blockmodeling, edited by P. Doreian, V. Batagelj, A. Ferligoj (Wiley, New York, 2019]), https://arxiv.org/abs/1705.10225

## Network reconstruction from indirect measurements and dynamics ([Tiago P. Peixoto](https://skewed.de/tiago))

The observed functional behavior of a wide variety large-scale systems
is often the result of a network of pairwise interactions between
individual elements. However, in many cases these interactions are
hidden from us, either because they are impossible to be measured
directly, or because their measurement can be done only at significant
experimental cost. Indeed, even when the interactions can be measured
directly, this can only be done with some certain degree of reliability,
which means that vast majority of network datasets must contain errors
and omissions, although this is rarely incorporated in traditional
network analysis. In such situations, we are required to infer the
underlying network of interactions from the observed functional behavior
or noisy measurement.

In this lecture, I will present how we can employ scalable nonparametric
Bayesian method to perform network reconstruction from indirect
measurements, that at the same time infers the modular structure (or
"communities") present in the network. I will show how the joint
reconstruction with community detection has a synergistic effect, where
the edge correlations used to inform the existence of communities are
also inherently used to improve the accuracy of the reconstruction
which, in turn, can better inform the uncovering of communities. I will
illustrate the use of the method with noisy networks measurements, and
observations arising from epidemic models and the Ising model, both on
synthetic and empirical networks, as well as on data containing only
functional information.

# References

- Tiago P. Peixoto, "Network reconstruction and community detection from dynamics" Phys. Rev. Lett. 123 128301 (2019), https://dx.doi.org/10.1103/PhysRevLett.123.128301, https://arxiv.org/abs/1903.10833
- Tiago P. Peixoto, "Reconstructing networks with unknown and heterogeneous errors", Phys. Rev. X 8 041011 (2018), https://dx.doi.org/10.1103/PhysRevX.8.041011, https://arxiv.org/abs/1806.07956


# SSDS 2020  - [5<sup>th</sup> Int'l Summer School on Data Science](https://sites.google.com/view/ssdatascience2020)

## Day 5 - Graph Representation Learning ([Xavier Bresson](https://www.ntu.edu.sg/home/xbresson/))

On the fifth day of the school you will learn about fundamentals and recent trends in the field of **graph representation learning**
as one of the cornerstones for large-scale machine learning and analysis on network-structured data. 

### Lecture materials and outline

* Graph Convolutional Networks - Spectral Techniques
* Graph Convolutional Networks - Spatial Techniques (w/ a PyTorch hands-on session included)
* Benchmarking Graph Neural Networks

The **Lecture** subfolder contains materials from presentations.

The **Hands-on** session includes practical demonstration using Google Colaboratory notebook:
* [Lab demo : GatedGCNs with DGL](https://drive.google.com/file/d/1WG5t6X12Z70JPtvA2-2PzdK3TMTQMsvm)



### Representing graphs through data: Graph learning and Optimal transport ([Hermina Petric Maretić](https://people.epfl.ch/hermina.petricmaretic/?lang=en))

Graphs offer a simple, yet meaningful representation of relationships between data. This representation is used in numerous machine learning algorithms in order to incorporate additional information about data. However, this representation can also be used in an inverted fashion; instead of modelling data through graphs, we model graphs through data. We will begin by showing how this representation can be used in graph learning in order to infer the unknown structure of the graph. A common drawback of graph inference methods is the assumption that all data belongs to the same graph. We will show how this assumption can be relaxed and use the graph-data representation to automatically cluster data that belong to different graphs and infer multiple graph structures. An interesting application of this method was found in neuroscience, where it enables a simultaneous separation of fMRI signals belonging to different brain networks and the inference of multiple brain network structures. In the second part of the talk we will present the basic notions of optimal transport. Using the representation of graphs through data, we will introduce an optimal transport framework between graphs. This framework defines a structurally meaningful distance between graphs and enables data prediction. We will demonstrate how this distance can be generalised through the definition of graph filters. Finally, a simple approximation of the optimal transport cost gives a highly scalable solution, leading to possible applications in numerous machine learning tasks.

**References:**
* https://ieeexplore.ieee.org/document/9050442 (Open access: https://arxiv.org/pdf/1810.10053.pdf)
* http://papers.nips.cc/paper/9539-got-an-optimal-transport-framework-for-graph-comparison.pdf
* https://arxiv.org/pdf/2003.06048.pdf

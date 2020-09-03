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


---

### Representing graphs through data: Graph learning and Optimal transport ([Hermina Petric Maretić](https://people.epfl.ch/hermina.petricmaretic/?lang=en))

Graphs offer a simple, yet meaningful representation of relationships between data. This representation is used in numerous machine learning algorithms in order to incorporate additional information about data. However, this representation can also be used in an inverted fashion; instead of modelling data through graphs, we model graphs through data. We will begin by showing how this representation can be used in graph learning in order to infer the unknown structure of the graph. A common drawback of graph inference methods is the assumption that all data belongs to the same graph. We will show how this assumption can be relaxed and use the graph-data representation to automatically cluster data that belong to different graphs and infer multiple graph structures. An interesting application of this method was found in neuroscience, where it enables a simultaneous separation of fMRI signals belonging to different brain networks and the inference of multiple brain network structures. In the second part of the talk we will present the basic notions of optimal transport. Using the representation of graphs through data, we will introduce an optimal transport framework between graphs. This framework defines a structurally meaningful distance between graphs and enables data prediction. We will demonstrate how this distance can be generalised through the definition of graph filters. Finally, a simple approximation of the optimal transport cost gives a highly scalable solution, leading to possible applications in numerous machine learning tasks.

**References:**
* https://ieeexplore.ieee.org/document/9050442 (Open access: https://arxiv.org/pdf/1810.10053.pdf)
* http://papers.nips.cc/paper/9539-got-an-optimal-transport-framework-for-graph-comparison.pdf
* https://arxiv.org/pdf/2003.06048.pdf

---

### From brain to epidemics: The power and limitations of graph neural networks ([Nima Dehmamy](http://nimadehmamy.com/))

Graph neural networks (GNN) are quickly replacing traditional methods from network science in a range of problems from link prediction to drug discovery. However, until recently, the focus had been more on designing new GNN layer architectures and much less how to combine such layers to improve expressivity of such models. Additionally, as is common in computer science, the performance of these models was mostly evaluated on benchmark datasets, with unknown generating processes and not on controlled examples with known properties. In these talks, I will review some of the limitations of common GNN designs and our work on how to make them more expressive. I will show how we can use synthetic graph datasets using known generating processes to examine the role played by different hyperparameters and aspects of GNN model design. Another aspect of graph learning, and machine learning in general, is that certain problems may probably not have unique solutions, such as the location of a random walker in a given time. I will discuss this in the specific setting of finding patient zero in an epidemic spreading model. We show that in many settings this question may not be answered uniquely and that our assessment of the accuracy of a GNN model must take this ambiguity into account. We show theoretical bounds on how accurately a learning method can predict patient zero and show experimental results following a similar trend. We also suggest alternative measures of performance may be more robust than the accuracy and which may not be subject to the same theoretical bounds. Lastly, I discuss how GNN may also be used in energy-based modeling for optimization tasks such as modeling the layout of brains and other networks.

**References:**
* http://papers.nips.cc/paper/9675-understanding-the-representation-power-of-graph-neural-networks-in-learning-graph-topology.pdf
* https://arxiv.org/pdf/2006.11913.pdf
* https://www.nature.com/articles/s41586-018-0726-6



# SSDS 2020  - [5<sup>th</sup> Int'l Summer School on Data Science](https://sites.google.com/view/ssdatascience2020)

## Day 4 - Large-scale Graph Mining and Summarization ([Danai Koutra](https://web.eecs.umich.edu/~dkoutra/))

On the fourth day of the school you will learn about data science methodologies for large-scale graph analytics.

### Lecture materials and outline

#### Finding structures in temporal graphs ([Alain Barrat](http://www.cpt.univ-mrs.fr/~barrat/english.html))

Temporal networks are increasingly used to represent a vast diversity of systems, including social interactions, brain activity patterns, interbank transactions or mobility patterns. In many of the corresponding data sets, crucial information on the structure and temporality of the system co-exist with noise and non-essential elements. Moreover, structures of different types can co-exist, from dense subgraphs on a certain time interval to sets of links with correlated dynamics. The temporal network can also exhibit switching behavior between "states" at various timescales. Uncovering the most relevant part of the data, or specific relevant structures and timescales, is a very challenging task. In the lecture, I will present several methods to extract relevant information and structures from temporal networks, along several directions. First, I will present a method to obtain a backbone of significant ties in a temporal network, by defining an adequate temporal null model that allows us to identify pairs of nodes having more interactions than expected given their activities: the significant ties. I will show how the knowledge of the backbone (without knowing the rest of the network) can be exploited to create surrogate data that yield the same outcome than the original data when used for simulating spreading processes. Then, I will discuss the notion of temporal core decomposition and of span-cores: the span-cores decompose a temporal network into subgraphs of controlled duration and increasing connectivity, generalizing the core-decomposition of static graphs. I will present an efficient algorithm to obtain this decomposition and show the relevance of the notion of span-core in analyzing social dynamics and detecting/correcting anomalies in the data. Moreover, I will show that the most stable and cohesive temporal cores play an important role in epidemic processes on temporal networks, and that their nodes are likely to represent influential spreaders. Finally, I will discuss methods introduced recently by several others to extract timescales or important changes in a temporal network and illustrate these methods on the concrete cases of an animal social network and of information sharing brain networks.

Download lecture from [here](https://github.com/SSDS-Croatia/SSDS-2020/raw/master/Day-4/lectures/01_Alain_Barrat_Structures_in_tempnets_SummerSchool_Sep2020.pdf) 

---


#### Large-scale Graph Mining and Summarization ([Danai Koutra](https://web.eecs.umich.edu/~dkoutra/))

* Large-scale graph mining: Network summarization and beyond 
* Hands-on session: Embedding-based multi-network analysis at scale
* Hands-on session: Pattern and anomaly mining in large, evolving graphs

The **Lecture** subfolder contains materials from presentations.

The **Hands-on** subfolder contains materials for hands-on examples.

There are two hands-on examples, 

The folder "MultiNetworkExample" contains a hands-on example of the basics of node similarity, unsupervised network embedding, and multi-network analysis.  You will visualize two different notions of node similarity: one is based on the nodes' proximity to each other, and the other is based on the structural roles that they play in the network.  Preserving either of these node similarities can be an objective for network embedding, an unsupervised method for learning feature representations of nodes in networks.  You will see how these notions of node similarity and the resulting embeddings can be used to compare nodes within a network and across different networks, and how this can be used for cross-network comparison of not only individual nodes, but also entire graphs.  Finally, you will perform a small experiment studying the scalabilitiy of different embedding methods on progressively larger graphs.  
  
### Hands-on environment setup instructions

The hands-on session is organized as Jupyter notebooks, which you can run on your local computer.
For MultiNetworkExample, you only need the basic data science Python toolkit: NumPy, SciPy, Matplotlib, Pandas, as well as the NetworkX graph analysis library.  Source code for specific graph mining examples is included in that folder, and scripts for performing basic visual analysis and calling graph mining tasks are contained in the file analysis.py.  You will run the example.ipynb notebook to walk through all the examples step by step (with explanations of what is happening).     

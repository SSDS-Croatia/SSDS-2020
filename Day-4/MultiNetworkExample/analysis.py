
import numpy as np
from scipy import sparse
import argparse

#Data analysis
import pandas as pd 
import matplotlib.pyplot as plt

#Method-specific code
from REGAL.alignments import *
from RGM.rgm import *
from RGM.main import parse_args

#Basic visualization
def visualize_emb_correlations(emb, emb_method):
    df = pd.DataFrame(data = emb.T)
    plt.matshow(df.corr())
    plt.title("%s similarity" % emb_method)
    plt.colorbar()
    plt.show()

#Network alignment
def embedding_node_alignments(emb1, emb2, true_alignments, emb_method = "xNetMF"):
    alignment_matrix = get_embedding_similarities(emb1, emb2, num_top = 1)
    alignment_accuracy, _ = score_alignment_matrix(alignment_matrix, topk = 1, true_alignments = true_alignments)
    print("Alignment accuracy for %s embeddings: %.3f" % (emb_method, alignment_accuracy))

#Graph comparison
def embedding_graph_comparison(embs, emb_method = "NetMF"):
    rgm_features = run_rgm(embs)
    visualize_emb_correlations(rgm_features.toarray(), emb_method + " graph")

def run_rgm(embs):
	args = parse_args()
	args.dimensionality = embs[0].shape[1]
	features = rgm(embs, args)
	return features
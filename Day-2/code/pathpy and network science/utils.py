#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# =============================================================================
# File      : clustering_example.py
# Author    : Jürgen Hackl <hackl@ifi.uzh.ch>
# Time-stamp: <Sat 2020-09-05 21:41 juergen>
#
# Copyright (c) 2016-2020 Pathpy Developers
# =============================================================================
import pickle
import pathpy as pp



def plot(network):
    style = {
        'width': 900,
        'height': 600,
        'forceCharge': -10,
        'forceRepel': -200,
        'defaultEdgeWeight': 0.01,
        'edge_size': 1,
        'edge_opacity': .3,
        'edge_color': 'gray',
        'curved': True,
    }
    network.plot(filename='cluster_network.html', **style)




# Plot dynamic network
# --------------------


def plot(network):
    style = {
        'width': 900,
        'height': 600,
        'forceCharge': -10,
        'forceRepel': -30,
        'defaultEdgeWeight': 0.6,
        'edge_size': 4,
        'edge_opacity': 1,
        'edge_color': 'red',
        'animation_end': 100,
        'animation_steps': 101,
        'curved': True,
        'directed': False,
    }

    for node in network.nodes.values():
        node.update(color='gray', size=16, t=0)

    for i, (_, edge, begin, end) in enumerate(network.edges.temporal()):
        for node in edge.nodes:
            node.update(color='red', size=20, t=begin)
            node.update(color='gray', size=16, t=end)

        if i == 99:
            break

    network.plot(filename='cluster_temp.html', **style)




# Plot random walk
# ----------------


def plot_walk(network, walk):
    wal = pp.TemporalNetwork(directed=False)

    for node in network.nodes.values():
        wal.add_node(node, color='gray', size=16, t=0)

    for edge in network.edges.values():
        wal.add_edge(edge.v, edge.w, t=0)

    nodes = []
    for t, w in enumerate(walk):
        if nodes:
            n = nodes.pop(0)
            wal.nodes[n].update(color='gray', size=16, t=t)
        wal.nodes[w].update(color='red', size=20, t=t)

        begin = t
        end = t+1
        for edge in wal.edges.values():
            wal._edges._intervals.addi(begin, end, edge)
            wal._edges._interval_map[edge].add((begin, end))
        nodes.append(w)
        if t == 110:
            break

    style = {
        'width': 900,
        'height': 600,
        'forceCharge': -10,
        'forceRepel': -200,
        'defaultEdgeWeight': 0.01,
        'edge_size': 1,
        'edge_opacity': .3,
        'edge_color': 'gray',
        'animation_end': 100,
        'animation_steps': 101,
        'curved': True,
    }

    wal.plot( **style)



# Generate Higher-Order Network
# -----------------------------

#paths = tn.to_paths()



# Plot higher-order network
# -------------------------


def plot_hon(network):

    _net = pp.Network.from_paths(network._subpaths(), frequencies=True)

    forces = pp.Network(directed=False)
    for edge in network.edges:
        v = edge.v.nodes[0]
        w = edge.w.nodes[-1]
        force = edge['frequency']
        if (v, w) not in forces.edges:
            forces.add_edge(v, w, force=force, opacity=0)
        else:
            forces.edges[v, w]['force'] += force

    deg = forces.degrees(weight='force')

    for edge in forces.edges:
        s = min(deg[edge.v.uid], deg[edge.w.uid])
        edge['weight'] = edge['force']/s

    clusters = {str(v): 'red' if len(str(v)) < 2 else (
        'green' if str(v).startswith('1') else 'blue') for v in range(30)}

    style = {
        'width': 900,
        'height': 600,
        'forceCharge': -4000,
        'forceRepel': -800,
        'node_color': clusters,
        'edge_size': 1,
        'edge_color': 'gray',
        'curved': True,
        'restartAlpha': 1,
        'targetAlpha': .0,
        'forceAlpha': .3,
        'repelDistance': 200,
    }

    

    for edge in network.nodes.edges:
        if (edge.v.uid, edge.w.uid) in forces.edges:
            forces.edges[edge.v.uid, edge.w.uid].update(opacity=.3, weight=0)
        else:
            forces.add_edge(edge.v.uid, edge.w.uid, opacity=.3, weight=0)

    # layout_style = {}
    # layout_style["node_size"] = 2
    # layout_style['layout'] = 'Fruchterman-Reingold'
    # layout_style['force'] = 0.2
    # layout_style['iterations'] = 500
    # layout = pp.layout(forces, **layout_style)
    # print(layout)
    
    forces.plot(**style)



def plot_hon_walk(network, walk):
    wal = pp.TemporalNetwork(directed=False)
    net = pp.Network()
    for edge in network.nodes.edges():
        net.add_edge(edge)

    clusters = {str(v): 'red' if len(str(v)) < 2 else (
            'green' if str(v).startswith('1') else 'blue') for v in range(30)}

        
    for node in net.nodes.values():
        #wal.add_node(node, color=clusters[node.uid], size=16, t=0)
        wal.add_node(node, size=16, t=0)

    for edge in network.edges.values():
        wal.add_edge(edge.v, edge.w, t=0)

    nodes = []
    for t, w in enumerate(walk):
        if nodes:
            n = nodes.pop(0)
            wal.nodes[n].update(color=clusters[n], size=16, t=t)
        wal.nodes[w].update(color='gray', size=20, t=t)

        begin = t
        end = t+1
        for edge in wal.edges.values():
            wal._edges._intervals.addi(begin, end, edge)
            wal._edges._interval_map[edge].add((begin, end))
        nodes.append(w)
        if t == 110:
            break

    style = {
        'width': 900,
        'height': 600,
        'forceCharge': -10,
        'forceRepel': -200,
        'defaultEdgeWeight': 0.01,
        'edge_size': 1,
        'edge_opacity': .3,
        'edge_color': 'gray',
        'animation_end': 100,
        'animation_steps': 101,
        'curved': True,
    }

    wal.plot( **style)

# =============================================================================
# eof
#
# Local Variables:
# mode: python
# mode: linum
# mode: auto-fill
# fill-column: 79
# End:

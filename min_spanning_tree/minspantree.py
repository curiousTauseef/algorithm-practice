#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Find minimum spanning tree of a graph represented in dot language
"""

from __future__ import print_function, absolute_import, division


import os
import pydot
from pydot import dot_parser


def load_graph(fpath):
    with open(fpath) as f:
        parsed = dot_parser.parse_dot_data(f.read())
        if parsed:
            return parsed[0]
        else:
            raise ValueError("No graph parsed from %s" % fpath)


def get_weight(edge):
    return edge.get_label()


def get_all_vertices(graph):
    return set(n for e in graph.get_edges() for n in (e.get_source(), e.get_destination()))


def has_cycle(graph):
    vertices = get_all_vertices(graph)
    sets = {v: None for v in vertices}

    def find(v):
        if sets[v] is None:
            return v
        return find(sets[v])

    def union(x, y):
        x_set = find(x)
        y_set = find(y)
        sets[x_set] = y_set

    for e in graph.get_edges():
        src = e.get_source()
        dest = e.get_destination()
        if find(src) == find(dest):
            return True
        union(src, dest)

    return False


def find_min_spanning_tree(graph):
    sorted_edges = sorted(graph.get_edges(), key=get_weight)
    vertices = get_all_vertices(graph)
    i = 0
    min_tree = pydot.Dot()
    for e in sorted_edges:
        if i >= len(vertices):
            print('reached end, stopping', i)
            break
        min_tree.add_edge(e)
        if has_cycle(min_tree):
            print('has cycle, have to remove...')
            min_tree.del_edge(e.get_source(), e.get_destination())
        i += 1
    return min_tree


def run(args):
    graph = load_graph(args.dotgraph)
    min_tree = find_min_spanning_tree(graph)

    output_base, _ = os.path.splitext(args.dotgraph)

    with open(output_base + '-found-mintree.dot', 'wb') as f:
        f.write(min_tree.create_dot())
    with open(output_base + '-found-mintree.png', 'wb') as f:
        f.write(min_tree.create_png())


if '__main__' == __name__:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dotgraph')

    args = parser.parse_args()
    run(args)

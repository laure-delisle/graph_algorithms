#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Graph class

class Graph(object):
    """Graph represented as dict of node:edges"""

    def __init__(self, graph_dict=None,oriented=False):
        """Initialize graph object from dict"""
        if oriented == True:
            print ("Oriented graphs are not implemented yet")
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """returns the vertices of the graph"""
        return list(self.__graph_dict.keys());

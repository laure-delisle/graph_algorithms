#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Manipulating graphs as edges list

import graph as g

def main():
	g_dict = {"a" : ["b","c"],
		 "b" : ["a"],
		 "c" : ["a"],
		 "d" : []}
	graph = g.Graph(g_dict)

	print (graph.vertices())


if __name__ == '__main__':
    main()
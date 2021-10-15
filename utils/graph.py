from py2neo import Graph,Node

from config import gen_graph_conn_params

Graph = Graph(**gen_graph_conn_params())
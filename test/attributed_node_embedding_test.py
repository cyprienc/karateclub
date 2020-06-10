import networkx as nx

import random
import numpy as np
from scipy.sparse import coo_matrix
from karateclub.node_embedding.attributed import BANE, TENE, TADW, FSCNMF, SINE, MUSAE, FeatherNode


def test_feather_node():
    """
    Testing the FEATHER node embedding.
    """
    graph = nx.newman_watts_strogatz_graph(250, 10, 0.2)

    features = np.random.uniform(0, 1, (250, 2000))
    model = FeatherNode()
    model.fit(graph, features)
    embedding = model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert embedding.shape[1] == 2*model.order*model.eval_points*model.reduction_dimensions

    features = np.random.uniform(0, 1, (250, 16))
    model = FeatherNode()
    model.fit(graph, features)
    embedding = model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert embedding.shape[1] == 2*model.order*model.eval_points*features.shape[1]


    features = {i: random.sample(range(150),50) for i in range(250)}

    row = np.array([k for k, v in features.items() for val in v])
    col = np.array([val for k, v in features.items() for val in v])
    data = np.ones(250*50)
    shape = (250, 150)

    features = coo_matrix((data, (row, col)), shape=shape)
    model = FeatherNode()
    model.fit(graph, features)
    embedding = model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert embedding.shape[1] == 2*model.order*model.eval_points*model.reduction_dimensions


def test_bane():
    """
    Testing the BANE node embedding.
    """
    graph = nx.newman_watts_strogatz_graph(250, 10, 0.2)

    features = np.random.uniform(0, 1, (250, 256))
    model = BANE()
    model.fit(graph, features)
    embedding = model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert embedding.shape[1] == model.dimensions


def test_fscnmf():
    """
    Testing the FSCNMF node embedding.
    """
    graph = nx.newman_watts_strogatz_graph(250, 10, 0.2)

    features = np.random.uniform(0, 1, (250, 128))
    model = FSCNMF()
    model.fit(graph, features)
    embedding = model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert embedding.shape[1] == 2*model.dimensions


def test_tene():
    """
    Testing the TENE node embedding.
    """
    graph = nx.newman_watts_strogatz_graph(250, 10, 0.2)

    features = np.random.uniform(0, 1, (250, 128))
    model = TENE()
    model.fit(graph, features)
    embedding = model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert embedding.shape[1] == 2*model.dimensions


def test_tadw():
    """
    Testing the TADW node embedding.
    """
    graph = nx.newman_watts_strogatz_graph(250, 10, 0.2)

    features = np.random.uniform(0, 1, (250, 128))
    model = TADW()
    model.fit(graph, features)
    embedding = model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert embedding.shape[1] == 2*model.dimensions


def test_musae():
    """
    Testing the MUSAE node embedding.
    """
    graph = nx.newman_watts_strogatz_graph(50, 10, 0.2)

    features = {i: random.sample(range(150), 50) for i in range(50)}
    row = np.array([k for k, v in features.items() for val in v])
    col = np.array([val for k, v in features.items() for val in v])
    data = np.ones(50*50)
    shape = (50, 150)
    features = coo_matrix((data, (row, col)), shape=shape)

    model = MUSAE()
    model.fit(graph, X)
    embedding = model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert embedding.shape[1] == model.dimensions


def test_sine():
    """
    Testing the SINE node embedding.
    """
    graph = nx.newman_watts_strogatz_graph(100, 10, 0.2)

    features = {i: random.sample(range(150), 50) for i in range(100)}
    row = np.array([k for k, v in features.items() for val in v])
    col = np.array([val for k, v in features.items() for val in v])
    data = np.ones(100*50)
    shape = (100, 150)

    features = coo_matrix((data, (row, col)), shape=shape)

    model = SINE()
    model.fit(graph, features)
    embedding = model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert embedding.shape[1] == model.dimensions

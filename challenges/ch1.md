# vertex

## Vertex
```python
Vertex(self, key: str)
```

The vertex object that is to be stored within a graph object

properties:
    key - The key or label of the vertex.
    __neighbors - a list of edges between this vertex and another one.

### neighbors

Get the keys of the neighbors of the vertex

### add_neighbor
```python
Vertex.add_neighbor(self, edge: tuple)
```

Add a neighbor to this vertex

Args:
    edge - A tuple containing

Returns:
    True if the edge was successfully added, False if not.

# graph

## Graph
```python
Graph(self)
```

An undirected graph implementation

### add_vertex
```python
Graph.add_vertex(self, vert: vertex.Vertex)
```

Add a vertex to the graph

Args:                * vertex - The vertex object that we would like to be adding.

### get_vertex
```python
Graph.get_vertex(self, vert_key: str)
```

Get a specific vertex from the set of verticies we have.

Args:
    vertKey - the integer of the vert key we're looking for

Returns:
    a vertex object if the vertkey is found

### get_verticies
```python
Graph.get_verticies(self)
```

Return a list of all the vertex keys

Returns:
    a list of all verticies objects within the graph

### add_edge
```python
Graph.add_edge(self, from_vert: str, to_vert: str, weight: float = 1.0)
```

Add an edge to the graph

Args:
    fromVert - The vertex object we're connecting the toVert to
    toVert - The vertex object we're connecting the fromVert to
    weight - (1.0) - The weight of the edge

### get_neighbors
```python
Graph.get_neighbors(self, vert_key: str)
```

Get the neighbors of a vertex stored within the graph.

Args:
    vert: The vertex we're trying to get the neighbors of.

Returns:
    The neighbors of the vertex that we're looking for

### get_edges
```python
Graph.get_edges(self) -> [<class 'tuple'>]
```

Get all of the edges from the graph

Returns:
    A list of the unique edges within the graph.

# digraph

## Digraph
```python
Digraph(self)
```

A directed graph

### add_edge
```python
Digraph.add_edge(self, from_vert: str, to_vert: str, weight: float = 1.0)
```

Add an edge to the digraph

Args:
    fromVert - The vertex object we're connecting the toVert to
    toVert - The vertex object we're connecting the fromVert to
    weight - (1.0) - The weight of the edge

### get_edges
```python
Digraph.get_edges(self) -> [<class 'tuple'>]
```

Get all of the edges from the graph

Returns:
    A list of the unique edges within the graph.


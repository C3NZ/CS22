# vertex

## Vertex
```python
Vertex(self, key: str)
```

The vertex object that is to be stored within a graph object

Properties:
* key - The key or label of the vertex.

### neighbors

Function for getting the keys of the neighbors of the vertex

Returns:
    A list of all neighbors to the current vertex

### add_neighbor
```python
Vertex.add_neighbor(self, edge: tuple)
```

Function for adding a neighbor to this vertex

Args:
* edge - A tuple containing the vertex object and it's
corresponding weight

Returns:
* True if the edge was successfully added, False if not.

# graph

## Graph
```python
Graph(self)
```

Class for representing an undirected graph

### add_vertex
```python
Graph.add_vertex(self, vert: vertex.Vertex)
```

Function for adding a vertex to the graph

Args:
* vertex - The vertex object that we would like to be adding.

### get_vertex
```python
Graph.get_vertex(self, vert_key: str)
```

Function for getting a specific vertex from the set
of verticies we have.

Args:
* vert_key - the integer of the vert key we're looking for

Returns:
* a vertex object if the vertkey is found

### get_verticies
```python
Graph.get_verticies(self)
```

Function for getting a list of all the vertex keys

Returns:
* a list of all verticies objects within the graph

### add_edge
```python
Graph.add_edge(self, from_vert: str, to_vert: str, weight: float = 1.0)
```

Function for adding an edge to the graph

Args:
* from_vert - The vertex object we're connecting the toVert to
* to_vert - The vertex object we're connecting the fromVert to
* weight - (1.0) - The weight of the edge

### get_neighbors
```python
Graph.get_neighbors(self, vert_key: str)
```

Function for getting the neighbors of a vertex
stored within the graph.

Args:
* vert: The vertex we're trying to get the neighbors of.

Returns:
* The neighbors of the vertex that we're looking for

### get_edges
```python
Graph.get_edges(self) -> [<class 'tuple'>]
```

Function for getting all of the edges from the graph

Returns:
* A list of the unique edges within the graph.

# digraph

## Digraph
```python
Digraph(self)
```

Class for representing a directed graph

Inherits properties and functions from the Graph class

### add_edge
```python
Digraph.add_edge(self, from_vert: str, to_vert: str, weight: float = 1.0)
```

Function for adding an edge to the digraph

Args:
* fromVert - The vertex object we're connecting the toVert to
* toVert - The vertex object we're connecting the fromVert to
* weight - (1.0) - The weight of the edge

### get_edges
```python
Digraph.get_edges(self) -> [<class 'tuple'>]
```

Function for getting all of the edges from the graph

Returns:
* A list of the unique edges within the graph.


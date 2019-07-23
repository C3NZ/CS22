# graphs.vertex

Module that handles the Vertex objects to be inserted into any graph type.

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

# graphs.graph

Module that implements an undirected graph class

## Graph
```python
Graph(self)
```

Class for representing an undirected graph

### add_vertex
```python
Graph.add_vertex(self, vert: graphs.vertex.Vertex)
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

### find_shortest_path
```python
Graph.find_shortest_path(self, from_vertex: str, to_vertex: str) -> [<class 'str'>]
```

Finding the shortest path from one vertex to another using breadth first
search. This algorithm attaches a parent property to all vertices that
are neighbors to the vertex that we're traveling from, allowing us to
traverse back up the tree to get the path at the end.

Read more: https://en.wikipedia.org/wiki/Breadth-first_search

Args:
* from_vertex - The key of the vertex we're starting at
* to_vertex - The key of the vertex we're going to

Returns:
* A list of vertex keys and the amount of edges if there is a valid
path within the graph
* An empty list and -1 indicating that there are no paths between the
two vertices within the list

## fill_graph
```python
fill_graph(graph: graphs.graph.Graph, verts: list, edges: list)
```

Fill an undirected graph object with verticies and edges.

Args:
* graph - the graph object that is going to be filled

* verts - A list of vertex objects to add to the graph

* edges - A list of tuples that contain edge keys and weights.


Returns:
A reference to the graph, vertices, and edges.

# graphs.digraph

Module that implements a directed graph class through the extension of the
undirected graph class (from challenges.graphs.graph)

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

# graphs.utils.file_reader

Utils for all of the graph files

## read_graph_file
```python
read_graph_file(filename: str) -> (<class 'graphs.graph.Graph'>, [<class 'graphs.vertex.Vertex'>], [<class 'tuple'>])
```

Read a graph file from the class specified format.

Args:
* filename - Read in the file specified by filename

Returns:
    A tuple that contains a graph object and two lists


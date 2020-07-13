# Maze Craze

## CS 102 Data Structures and Algorithms- Final Project

## Team Members
- Rida Zahid Khan
- Maheen Anees

## Project Description
Python program that generates a maze and traverses it automatically using depth first algorithm.

### Maze Generation
First, the program generates an empty n x n square grid with each node having four boundaries. A random node from the grid is then selected and then a random neighbor of that node, making sure the selected node has not been already explored. Then the wall separating the two nodes is removed. The selected neighbor is then added into the visited node stack and is used as the current node to start off the process again. If all the neighboring nodes of the current node are visited, it pops a node from the stack and use it as the current node. 

### Maze Traversal 
Start from the starting point (source node) and if there are multiple openings, it chooses a node randomly and moves forward. If it reaches a node where there are no openings/ all neighboring nodes are already visited, it will backtrack until it reaches a node which has unvisited neighboring nodes. The program will do this recursively until it reaches the end point. If none of the pathways work, then there is no way out (this situation can occur because the maze is generated randomly). 

### DSA techniques
- Representing maze as a graph 
- Queue for storing visited nodes
- Stack facilitating backtracking
- Depth first search algorithm

### Libraries used
- Pygame

### Acknowledgements 
- https://en.wikipedia.org/wiki/Maze_generation_algorithm
- https://youtu.be/Xthh4SEMA2o

# 15-Puzzle
## Prerequisites
<a href="https://www.python.org/downloads/">Python 3.5+</a>
## How to Run the Program
1. Clone this repository
2. Open command line/terminal
3. Change directory to **src** folder in this repository
4. Run `main.py` on your command line/terminal

## Algorithm Explanation
This program is using A* Search algorithm to solve the 15-puzzle. A* Search algorithm is one of the best and popular technique used in path-finding and graph traversals.

### Why A* Search Algorithm?
Informally speaking, A* Search algorithms, unlike other traversal techniques, it has “brains”. What it means is that it is really a smart algorithm which separates it from the other conventional algorithms. This fact is cleared in detail in below sections. 
And it is also worth mentioning that many games and web-based maps use this algorithm to find the shortest path very efficiently (approximation).

Consider a square grid having many obstacles and we are given a starting cell and a target cell. We want to reach the target cell (if possible) from the starting cell as quickly as possible. Here A* Search Algorithm comes to the rescue.
What A* Search Algorithm does is that at each step it picks the node according to a value-‘f’ which is a parameter equal to the sum of two other parameters – ‘g’ and ‘h’. At each step it picks the node/cell having the lowest ‘f’, and process that node/cell.
We define ‘g’ and ‘h’ as simply as possible below
g = the movement cost to move from the starting point to a given square on the grid, following the path generated to get there. 
h = the estimated movement cost to move from that given square on the grid to the final destination. This is often referred to as the heuristic, which is nothing but a kind of smart guess. We really don’t know the actual distance until we find the path, because all sorts of things can be in the way (walls, water, etc.). There can be many ways to calculate this ‘h’.

## Author
Daffa Ananda Pratama Resyaly -- 13519107

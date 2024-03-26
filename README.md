Performed BFS, DFS, UCS,Astar variations on Pacman developed by UC Berkley 

DFS (Type the following command in terminal)
 python pacman.py -l mediumMaze -p SearchAgent

BFS 
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

UCS 
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

Astar
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

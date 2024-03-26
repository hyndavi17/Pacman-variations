# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    
    "*** YOUR CODE HERE ***"
    reachedNodes = []
    frontierStack = util.Stack()
    startStateNode = (problem.getStartState(), [])
    frontierStack.push(startStateNode)
    while not frontierStack.isEmpty():
        currentStateNode, pathTravelled = frontierStack.pop()
        reachedNodes.append(currentStateNode);
        if not problem.isGoalState(currentStateNode):
            for childStateNode, e, edgeCostTravelled in problem.getSuccessors(currentStateNode):
                if childStateNode not in reachedNodes:
                    childPathTravelled = pathTravelled + [e]
                    childNode = (childStateNode, childPathTravelled)
                    frontierStack.push(childNode)    
        else:
            return pathTravelled
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    startStateNode = (problem.getStartState(), [])  
    frontierQueue = util.Queue()
    reachedNodes = []
    frontierQueue.push(startStateNode)
    while not frontierQueue.isEmpty():
        currentStateNode, pathTravelled = frontierQueue.pop()
        if currentStateNode not in reachedNodes:
            reachedNodes.append(currentStateNode)
            if problem.isGoalState(currentStateNode):
                return pathTravelled
            else:   
                for childStateNode, e, eC in problem.getSuccessors(currentStateNode):
                    childPathTravelled = pathTravelled + [e]
                    childNode = (childStateNode, childPathTravelled)
                    frontierQueue.push(childNode)

def uniformCostSearch(problem):
    "*** YOUR CODE HERE ***"
    
    reachedNodes= {}
    startNode = (problem.getStartState(), []) 
    frontierQueue = util.PriorityQueue()
    frontierQueue.push(startNode, 0)
    while not frontierQueue.isEmpty():
        currentStateNode, pathTravelled = frontierQueue.pop()
        cost = problem.getCostOfActions(pathTravelled)
        if currentStateNode not in reachedNodes or reachedNodes[currentStateNode] > cost:
            reachedNodes[currentStateNode] = cost
            if not problem.isGoalState(currentStateNode):
                for childStateNode, e, eC in problem.getSuccessors(currentStateNode):
                    childPathTravelled = pathTravelled + [e]
                    childCost = cost + eC
                    childNode = (childStateNode, childPathTravelled)
                    frontierQueue.push(childNode, childCost)                
            else:
                return pathTravelled
                
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "*** YOUR CODE HERE ***"
    frontierQueue = util.PriorityQueue()
    reachedNodes = {}
    startNode = (problem.getStartState(), [])     
    frontierQueue.push(startNode, 0)
    while not frontierQueue.isEmpty():
        currentStateNode, pathTravelled = frontierQueue.pop()
        if currentStateNode not in reachedNodes:
            cost = problem.getCostOfActions(pathTravelled)
            reachedNodes[currentStateNode] = cost
            if not problem.isGoalState(currentStateNode):
                for childStateNode, e, eC in problem.getSuccessors(currentStateNode):
                    childPathTravelled = pathTravelled + [e]
                    childNode = (childStateNode, childPathTravelled)
                    childCost = cost + eC + heuristic(childStateNode, problem)
                    frontierQueue.push(childNode, childCost)
            else: 
                return pathTravelled


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch



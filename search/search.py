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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    "*** Q1 ***"

    # Get the starting node of the problem
    startingNode = problem.getStartState()

    # Check if the starting node is the goal state
    if problem.isGoalState(startingNode):
        # If it is, return an empty list (no actions needed)
        return []

    # Initialize a stack to store nodes and their corresponding actions
    myQueue = util.Stack()

    # List to keep track of visited nodes
    visitedNodes = []

    # Push the starting node and an empty list of actions onto the stack
    # (node, actions)
    myQueue.push((startingNode, []))

    # Explore nodes until the stack is empty
    while not myQueue.isEmpty():
        # Pop a node and its corresponding actions from the stack
        currentNode, actions = myQueue.pop()

        # Check if the current node has not been visited
        if currentNode not in visitedNodes:
            # Mark the current node as visited
            visitedNodes.append(currentNode)

            # Check if the current node is the goal state
            if problem.isGoalState(currentNode):
                # If it is, return the list of actions to reach the goal
                return actions

            # Iterate over the successors of the current node
            for nextNode, action, cost in problem.getSuccessors(currentNode):
                # Create a new list of actions by adding the current action
                newAction = actions + [action]

                # Push the next node and the new list of actions onto the stack
                myQueue.push((nextNode, newAction))


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    "*** Q2 ***"

    # Get the starting node of the problem
    startingNode = problem.getStartState()

    # Check if the starting node is the goal state
    if problem.isGoalState(startingNode):
        # If it is, return an empty list (no actions needed)
        return []

    # Initialize a queue to store nodes and their corresponding actions
    myQueue = util.Queue()

    # List to keep track of visited nodes
    visitedNodes = []

    # Push the starting node and an empty list of actions onto the queue
    # (node, actions)
    myQueue.push((startingNode, []))

    # Explore nodes until the queue is empty
    while not myQueue.isEmpty():
        # Pop a node and its corresponding actions from the queue
        currentNode, actions = myQueue.pop()

        # Check if the current node has not been visited
        if currentNode not in visitedNodes:
            # Mark the current node as visited
            visitedNodes.append(currentNode)

            # Check if the current node is the goal state
            if problem.isGoalState(currentNode):
                # If it is, return the list of actions to reach the goal
                return actions

            # Iterate over the successors of the current node
            for nextNode, action, cost in problem.getSuccessors(currentNode):
                # Create a new list of actions by adding the current action
                newAction = actions + [action]

                # Push the next node and the new list of actions onto the queue
                myQueue.push((nextNode, newAction))

    # If no solution is found, raise an exception (this line may need adjustment based on the util module)
    util.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    "*** Q3 ***"
    # Get the starting node of the problem
    startingNode = problem.getStartState()

    # Check if the starting node is the goal state
    if problem.isGoalState(startingNode):
        # If it is, return an empty list (no actions needed)
        return []

    # List to keep track of visited nodes
    visitedNodes = []

    # Initialize a priority queue to store nodes, their corresponding actions, and priorities
    pQueue = util.PriorityQueue()

    # Push the starting node, an empty list of actions, and priority 0 onto the priority queue
    # ((coordinate/node, action to current node, cost to current node), priority)
    pQueue.push((startingNode, [], 0), 0)

    # Explore nodes until the priority queue is empty
    while not pQueue.isEmpty():
        # Pop a node, its corresponding actions, and previous cost from the priority queue
        currentNode, actions, prevCost = pQueue.pop()

        # Check if the current node has not been visited
        if currentNode not in visitedNodes:
            # Mark the current node as visited
            visitedNodes.append(currentNode)

            # Check if the current node is the goal state
            if problem.isGoalState(currentNode):
                # If it is, return the list of actions to reach the goal
                return actions

            # Iterate over the successors of the current node
            for nextNode, action, cost in problem.getSuccessors(currentNode):
                # Create a new list of actions by adding the current action
                newAction = actions + [action]

                # Calculate the priority by adding the previous cost and the cost to the next node
                priority = prevCost + cost

                # Push the next node, the new list of actions, and the priority onto the priority queue
                pQueue.push((nextNode, newAction, priority), priority)

    # If no solution is found, raise an exception (this line may need adjustment based on the util module)
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    "*** Q4 ***"

    # Get the starting node of the problem
    startingNode = problem.getStartState()

    # Check if the starting node is the goal state
    if problem.isGoalState(startingNode):
        # If it is, return an empty list (no actions needed)
        return []

    # List to keep track of visited nodes
    visitedNodes = []

    # Initialize a priority queue to store nodes, their corresponding actions, and costs
    pQueue = util.PriorityQueue()

    # Push the starting node, an empty list of actions, and cost 0 onto the priority queue
    # ((coordinate/node, action to current node, cost to current node), priority)
    pQueue.push((startingNode, [], 0), 0)

    # Explore nodes until the priority queue is empty
    while not pQueue.isEmpty():
        # Pop a node, its corresponding actions, and previous cost from the priority queue
        currentNode, actions, prevCost = pQueue.pop()

        # Check if the current node has not been visited
        if currentNode not in visitedNodes:
            # Mark the current node as visited
            visitedNodes.append(currentNode)

            # Check if the current node is the goal state
            if problem.isGoalState(currentNode):
                # If it is, return the list of actions to reach the goal
                return actions

            # Iterate over the successors of the current node
            for nextNode, action, cost in problem.getSuccessors(currentNode):
                # Create a new list of actions by adding the current action
                newAction = actions + [action]

                # Calculate the cost to the next node by adding the previous cost and the cost to the next node
                newCostToNode = prevCost + cost

                # Calculate the heuristic cost by adding the cost to the next node and the heuristic estimate
                heuristicCost = newCostToNode + heuristic(nextNode, problem)

                # Push the next node, the new list of actions, and the cost to the next node onto the priority queue
                pQueue.push((nextNode, newAction, newCostToNode), heuristicCost)

    # If no solution is found, raise an exception (this line may need adjustment based on the util module)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

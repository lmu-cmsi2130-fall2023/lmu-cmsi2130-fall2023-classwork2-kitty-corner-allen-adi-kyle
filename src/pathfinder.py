'''
CMSI 2130 - Classwork 2
Author: Allen Boyce, Adi Roitburg, Kyle Matton

Modify only this file as part of your submission, as it will contain all of the logic
necessary for implementing the breadth-first tree search that solves the basic maze
pathfinding problem.
'''

from queue import Queue
from maze_problem import *
from dataclasses import *

@dataclass
class SearchTreeNode:
    """
    SearchTreeNodes contain the following attributes to be used in generation of
    the Search tree:

    Attributes:
        player_loc (tuple[int, int]):
            The player's location in this node.
        action (str):
            The action taken to reach this node from its parent (or empty if the root).
        parent (Optional[SearchTreeNode]):
            The parent node from which this node was generated (or None if the root).
    """
    player_loc: tuple[int, int]
    action: str
    parent: Optional["SearchTreeNode"]
    
    
    def __str__(self) -> str:
        return "@: " + str(self.player_loc)

    #Helper method to get the solution as a list of directions to reach the goal state
    def get_path(self) -> list[str]:
        path: list[str] = []
        current_node: SearchTreeNode = self
        
        count: int = 0

        while(current_node.parent):
            path.insert(0, current_node.action)
            current_node = current_node.parent

    
        return path


    
def pathfind(problem: "MazeProblem") -> Optional[list[str]]:
    """
    The main workhorse method of the package that performs A* graph search to find the optimal
    sequence of actions that takes the agent from its initial state and shoots all targets in
    the given MazeProblem's maze, or determines that the problem is unsolvable.

    Parameters:
        problem (MazeProblem):
            The MazeProblem object constructed on the maze that is to be solved or determined
            unsolvable by this method.

    Returns:
        Optional[list[str]]:
            A solution to the problem: a sequence of actions leading from the 
            initial state to the goal (a maze with all targets destroyed). If no such solution is
            possible, returns None.
    """
    # TODO: Implement breadth-first tree search!

    """
        PSEUDOCODE:
        initialize frontier, initial state node
        add initial state node to frontier
        
        while frontier is not empty:
            pop expanding node from frontier
            generate children of expanded node
            for each generated child:
                if child is goal:
                    return solution from child
                add child to frontier
        
        return null (should never reach here for this assignment)
    """

    #---------------------------------------------------------------------------------------------------------------------------------------------------------------

    #Initialize Frontier
    frontier: Queue = Queue()

    #Initialize inital node and puts it in Frontier
    initial_state_node: SearchTreeNode = SearchTreeNode(problem.get_initial_loc(), "", None)
    frontier.put(initial_state_node)    
    test: list[str] = ["hi"]

    #While the Frontier has nodes
    while not frontier.empty():

        #Initializes the node that will eventually generates children, gets that node's location, and uses it to get a dictionary of transitions
        expanding_node: SearchTreeNode = frontier.get()
        location: tuple[int, int] = expanding_node.player_loc
        actions: dict = problem.get_transitions(location)

        #Creates a list of children of the expanding node
        children: list[SearchTreeNode] = []
        for key in actions:
            children.append(SearchTreeNode(actions[key], key, expanding_node))
        
        #Checks if the child reached the goal state. 
        #If yes: Get the path to reach the solution
        #If no: Put that child into the frontier
        for node in children:
            if (node.player_loc[0] == problem.get_goal_loc()[0]) and (node.player_loc[1] == problem.get_goal_loc()[1]):
                return node.get_path()
            else:
                frontier.put(node)
        
    return None

    #---------------------------------------------------------------------------------------------------------------------------------------------------------------
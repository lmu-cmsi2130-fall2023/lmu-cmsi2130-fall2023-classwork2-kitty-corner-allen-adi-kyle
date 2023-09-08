'''
CMSI 2130 - Classwork 2
Author: Allen Boyce, Adi Rottenburg, Kyle Matton

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
    
    #Calls get_path_helper with a new empty list
    #Returns a stack of strings that list the steps taken to reach this SearchTreeNode.
    def get_path(self) -> list[str]:
        return self.get_path_helper([])
    
    #NOTE: UNTESTED:
    #Returns a stack of strings that list the actions taken to reach this SearchTreeNode.
    def get_path_helper(self, actions: list[str]) -> list[str]:
        if type(self.parent) is None:
            return actions
        list.append(self.action)
        self.get_path(self, actions.parent)

def pathfind(problem: MazeProblem) -> Optional[list[str]]:
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
    #initialize frontier
    frontier: list["SearchTreeNode"] = []

    #add initial state node to frontier
    initial_state_node: "SearchTreeNode" = SearchTreeNode()
    initial_state_node.player_loc = MazeProblem.get_initial_loc
    frontier.append(initial_state_node)


    return None


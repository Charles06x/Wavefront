#WAVEFRONT PROGRAM DESCRIPTION

The Wavefront program is designed to “move” a robot through an environment which contains obstacles. In the python program (Wavefront.py) the environment is represented by a multidimensional array and each element is a tile that means a one-step movement; the obstacles are represented by “-1”and the initial coordinate by a single character (“I”), the final destination is set at one (1).
The purpose is to find the shortest way to get from the starting position to the final destination in order to return it to the user.
When it’s done searching all the possible paths the “steps” are labeled with a number and the paths go from one (final destination) to the initial coordinate on a one-and-one sequence, the path with the lowest value will be chosen and if there are two or more paths with the same value, there is not a specific rule to choose one of them so the choice could be random and there are not disadvantages at all.
When a path is chosen, the robot starts the travel through it and the numbers are set to another character (“*”) until it gets to the destination. Below you can see a screenshot of the program after its execution:

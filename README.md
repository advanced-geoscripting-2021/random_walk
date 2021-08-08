# Random Walk Simulation

## Implementation
The application is written in Python3 using Shapely to generate a Playground for multiple Random-Walkers.
Obstacles and borders are implemented as shapely polygons limiting the walking ranges of the walkers.

Organized in 2 Modules:

- random_walker: Contains the default Random-Walker and different extensions, organized in subclasses. Each subclass follows specific rules when walking randomly over the Playground. Most subclasses are chess-inspired and follow the basic movement rules for five of the six stones on the board (sadly there is no Knight...).
- playground: Defining the area, in which the Walker is allowed to "play". A playground is seed-generated s.t. different obstacels can be implemented, while the default map simply spans an quadratic area that can be scaled via initial argument. 

## Application

When running our Random-Walker-Application, a number of randomly chosen walkers will walk a set number of steps following their spefific rules. The resulting paths are drawn and returned as a plot.
For the execution of main.py you can set the following flags (if no flags are set during execution, default parameters are set for a number of 2 walkers on the default playground with scaling factor 4 -> playground size: 1000 x 1000):
- -h : show help message and how to use it
- -w : number of walkers {1...Inf}
- -n : space separated list of walker names to choose from {Rook,King,Bishop,Queen,Pawn}
- -ls: set playground scale factor {1...Inf}
- -ps : set playground/map generation seed (-> currently only one other playground available (seed=1) containing a hole, representing a lake) {0,1}
- -s : number of steps per walkers {1...Inf}
- --save : save the simulation to a file


## Examples Configurations

Simulate three Kings:  
- python main.py -w 3 -n King![img.png](img.png)

Simulate four walkers, choose from Queen and Pawn: 
- python main.py -w 4 -n Queen Pawn

Simulate two random walkers for 10 steps:
- python main.py -w 2 -s 10

Simulate two random walkers on a map with obstacles:
- python main.py -w 2 -ps 1

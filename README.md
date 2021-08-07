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
- -h : help
- -w : number of walkers

- -ls: adjust landscale playground scale
- -ps : set playground/map generation seed
- -s : number of steps per walkers

- --save : save figure

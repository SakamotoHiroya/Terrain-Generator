import numpy as np
import math

# linear completion
def linerCompletion(x, y1, y2):
    return (y2 - y1) * x + y1;

# Method that returns three dimensions slope
def getSlope(location,seed=0,maxSlope=5):
    return np.array([(hash((*location, seed, 0)) % 20000 - 10000) / 10000 * maxSlope,
                     (hash((*location, seed, 1)) % 20000 - 10000) / 10000 * maxSlope,
                     (hash((*location, seed, 2)) % 20000 - 10000) / 10000 * maxSlope])

# Method that returns perlin noise values in three dimensions or less.
def noise(x, y=0, z=0,seed=0,scale=1,maxSlope=5):

    if isinstance(x, np.ndarray):
        if not isinstance(y, np.ndarray) and y == 0:
            y = 0 * x
        if not isinstance(z, np.ndarray) and z == 0:
            z = 0 * x
        
        result = []
        for location in zip(x, y, z):
            result.append(noise(*location, seed=seed, scale=scale, maxSlope=maxSlope))
        return np.array(result)
    else:
        x /= scale
        y /= scale
        z /= scale
        
        targetPoint = np.array([x, y, z])
        
        gridPivot = np.array([math.floor(x),math.floor(y),math.floor(z)]);
        
        relativePoint = targetPoint - gridPivot;
        
        #define grid points enclose target point
        grids = np.array([[0,0,0],
                          [1,0,0],
                          [0,1,0],
                          [1,1,0],
                          [0,0,1],
                          [1,0,1],
                          [0,1,1],
                          [1,1,1]])
        
        for grid in grids:
            grid += gridPivot;
        
        #decide slope vector
        slopes = []
        for grid in grids:
            slopes.append(getSlope(grid,seed=seed,maxSlope=maxSlope))
        slopes = np.array(slopes);
        
        #vectors from grid to target point
        gridVectors = []
        for grid in grids:
            gridVectors.append(targetPoint - grid)
        gridVectors = np.array(gridVectors)
        
        #perlin noise values in grid location
        gridValues = []
        for gridVector, slope in zip(gridVectors, slopes):
            gridValues.append(np.dot(gridVector, slope))
        gridValues = np.array(gridValues)
        
        return linerCompletion(relativePoint[2],
                        linerCompletion(relativePoint[1],
                                        linerCompletion(relativePoint[0], gridValues[0], gridValues[1]),
                                        linerCompletion(relativePoint[0], gridValues[2], gridValues[3])),
                        linerCompletion(relativePoint[1],
                                        linerCompletion(relativePoint[0], gridValues[4], gridValues[5]),
                                        linerCompletion(relativePoint[0], gridValues[6], gridValues[7])))    
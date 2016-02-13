# 8 Queens
# place 8 queens in a chess board so there is no chance of collision

def main():
    numQueens = 8;
    print "Queens:", numQueens
    queensSoFar = [-1] * numQueens
    print placeQueen(numQueens, 0, queensSoFar)
    
def placeQueen(size, currentPosition, queensSoFar):
    if (currentPosition == size):
        return 1   
    choices = getPossibleChoices(size, queensSoFar, currentPosition)
    sum = 0
    for choice in choices:
        queensSoFar[currentPosition] = choice
        sum += placeQueen(size, currentPosition+1, queensSoFar)
        queensSoFar[currentPosition] = -1
    return sum;

def getPossibleChoices(numQueens, queensSoFar, currentPosition):
    allPositions = [0] * numQueens
    for queensPlaced in queensSoFar:
        if (queensPlaced >= 0):
            allPositions[queensPlaced] = 1
    return [i for i, j in enumerate(allPositions) if j == 0]

if __name__ == '__main__':
   main()



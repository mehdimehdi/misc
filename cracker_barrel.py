import copy 

class Hole:
    def __init__(self,index,empty):
        self.index = index
        self.empty = empty


    def __str__(self):
        return "%s" % self.empty

class Board:
    def __init__(self,num_rows):
        self.holes = []
        self.num_rows = num_rows
        n = 0
        while n < num_rows:
            m = 0
            while m <= n:
                empty = False
                if n == 0 and m == 0:
                    empty = True
                self.holes.append(Hole([n,m],empty))
                m =m+1
            n = n+1

    def __str__(self):

        count = 0
        nextBreak = 0
        for h in self.holes:
            if nextBreak == count:
                intro = "\n"
                nextBreak = nextBreak + 1
                count = 0
            else:
                intro = ""
            count = count + 1
            s = "%s%s%s" % (s,intro,h)
        return s

    def getPossibleMove(self):
        possibleMove = []
        for hole in self.holes:
            if not hole.empty:
                for n in self.neighborsIndexes(hole):
                    for nn in self.neighborsIndexesWithDirection(hole,self.getHole(n)):
                        if self.getHole(nn).empty and not self.getHole(n).empty:
                            possibleMove.append([hole,self.getHole(nn),self.getHole(n)])
        return possibleMove

    def move(self):
        if not self.done():
            for source,target,over in self.getPossibleMove():
                self.doMove(source,target,over)
                self.move()
        else:
            print "YAY"
            return



    def getHole(self,index):
        for h in self.holes:
            if index == h.index:
                return h
        return None

    def neighborsIndexesWithDirection(self,jumper,jumped):
        candidates = []
        possibleNeighbor = self.neighborsIndexes(jumped)
        #north-west direction
        nw = [jumped.index[0]-1,jumped.index[1]-1]
        if jumper.index[0]-1 == jumped.index[0] and jumper.index[1]-1 == jumped.index[1] and nw in possibleNeighbor:
            candidates.append(nw)
        #north-east direction
        ne = [jumped.index[0]-1,jumped.index[1]]
        if jumper.index[0]-1 == jumped.index[0] and jumper.index[1] == jumped.index[1] and ne in possibleNeighbor:
            candidates.append(ne)
        #east direction
        e = [jumped.index[0],jumped.index[1]+1]
        if jumper.index[0] == jumped.index[0] and jumper.index[1]+1 == jumped.index[1] and e in possibleNeighbor:
            candidates.append(e)
        #south-east direction
        se = [jumped.index[0]+1,jumped.index[1]+1]
        if jumper.index[0]+1 == jumped.index[0] and jumper.index[1]+1 == jumped.index[1] and se in possibleNeighbor:
            candidates.append(se)
        #south-west direction
        sw = [jumped.index[0]+1,jumped.index[1]]
        if jumper.index[0]+1 == jumped.index[0] and jumper.index[1] == jumped.index[1] and sw in possibleNeighbor:
            candidates.append(sw)
        #west direction
        w = [jumped.index[0],jumped.index[1]-1]
        if jumper.index[0] == jumped.index[0] and jumper.index[1]-1 == jumped.index[1] and w in possibleNeighbor:
            candidates.append(w)
        return candidates

    def neighborsIndexes(self,hole):
        neighbors = []
        #north-west
        if hole.index[0] != 0 and hole.index[1] != 0:#if not at the top or on the left, then has a north-west neighbor
            nw = [hole.index[0]-1,hole.index[1]-1]
            neighbors.append(nw)
        #north-east
        if hole.index[1] != hole.index[0]:#if not on the right, then has a north-east neighbor and east neighbor
            ne = [hole.index[0]-1,hole.index[1]]
            neighbors.append(ne)
            e = [hole.index[0],hole.index[1]+1]
            neighbors.append(e)
        #south-east
        if hole.index[0] != self.num_rows-1:#if not at the bottom , then has a south-east neighbor and south-west neighbor
            se = [hole.index[0]+1,hole.index[1]+1]
            neighbors.append(se)
            sw = [hole.index[0]+1,hole.index[1]]
            neighbors.append(sw)
        #west
        if hole.index[1] != 0:#if not on the left, then has a west neighbor
            w = [hole.index[0],hole.index[1]-1]
            neighbors.append(w)
        return neighbors

    def doMove(self,source,target,over):
        for hole in self.holes:
            if hole == source:
                hole.empty = True
            if hole == target:
                hole.empty = False
            if hole == over:
                hole.empty = True
        return

    def unmove(self,source,target,over):
        self.holes.remove(source)
        self.holes.remove(target)
        self.holes.remove(over)
        source.empty = False
        over.empty = False
        target.empty = True
        self.holes.append(source)
        self.holes.append(over)
        self.holes.append(target)

    def done(self):
        count = 0
        for h in self.holes:
            if not h.empty:
                count = count +1

        if count > 1:
            return False
        else:
            return True


NUM_ROWS = 5

board = Board(NUM_ROWS)

test = board.move()

print test

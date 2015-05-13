import math

class RankMatrix(object):

    def __init__(self, num_docs):
        self.Matrix = [[0.0]*num_docs for i in range(num_docs)] #numpy.zeros((5, 5)) # [[0 for x in range(num_docs)] for y in range(num_docs)]
        self.num_docs = num_docs
        self.alpha = 0.9
        self.epsilon = 0.00000001
        
    def normalize_matrix(self):

        #normalize the rows
        for i in range(self.num_docs):        
            rowSum = 0;
            for j in range(self.num_docs):
                rowSum = rowSum + self.Matrix[i][j];
                
            if rowSum > 0:
                for j in range(self.num_docs):
                    if self.Matrix[i][j] > 0:
                        self.Matrix[i][j] = self.Matrix[i][j] / rowSum;
        
        #pagerank
        if self.num_docs > 0:
            self.inv_n = 1.0 / self.num_docs;
        else:
            self.inv_n = 1.0 / 0.000001;

        """print "$" * 70
        for i in range(self.num_docs):        
            for j in range(self.num_docs):
                print self.Matrix[i][j]
            print "\n"
        print "$" * 70
        """
        self.findVector()
        
        
    def findVector(self):
       
        error = 1.0;

        self.PageRank = [self.inv_n for x in range(self.num_docs)]
        
        tempPR = [0.0 for x in range(self.num_docs)]

        tNodes = (1 - self.alpha) * self.inv_n;

        for i in range(self.num_docs):
            for j in range(self.num_docs):
                self.Matrix[i][j] = self.alpha * self.Matrix[i][j] + tNodes;
        
        while (error >= self.epsilon):
    
            for i in range(self.num_docs):
                tempPR[i] = self.PageRank[i];

            for i in range(self.num_docs):
                temp = 0.0;
                for j in range(self.num_docs):
                    temp += tempPR[j] * self.Matrix[j][i];
                self.PageRank[i] = temp;

            error = self.normalise(self.PageRank, tempPR);

    def normalise(self, a, b):
        norm = 0;
        n = len(a)

        for i in range(n):
            norm += math.fabs(a[i] - b[i]);
        
        return norm;
    
    def get_matrix(self):
        return self.Matrix
        
    def set_matrix(self, i, j, value):
        self.Matrix[i][j] = value
 
    def get_page_rank_matrix(self):
        return self.PageRank
        
    def __repr__(self):
        return "I'm a matrix"
 
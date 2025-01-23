import numpy as np
from collections import Counter 

class KnnMDS:

    def __init__(self,k):
       self.n_neighbours=k
       self.X_train=None
       self.Y_train=None

    def fit(self,X_train,Y_train):
          self.X_train=X_train
          self.Y_train=Y_train

    def predict(self,X_test):

        y_pred = []

        for i in X_test:
            distances=[]
            for j in self.X_train:
                distances.append(self.calculate_distance(i,j))
            n_neighbors = sorted(list(enumerate(distances),key=lambda x:x[1]))
            label=self.majority_count(n_neighbors)
            y_pred.append(label)
        return np.array(y_pred)

    def calculate_distance(self,point_A,point_B):
        np.linalg.norm(point_A-point_B)

    def majority_count(self,neighbors):
        votes=[]
        for i in neighbors:
            votes.append(self.Y_train[i[0]])
        votes=Counter(votes)
        return votes.most_common()[0][0]



#for every testing value calculate the distance with every other node
#and sort the nodes according to that check the nearest k nodes and assign it 
#the majority among them
    

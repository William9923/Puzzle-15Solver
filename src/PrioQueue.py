import copy
class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == 0
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 
  
    # for popping an element based on Priority 
    def delete(self): 
      if self.isEmpty():
        raise IndexError
      min = 0
      for i in range(len(self.queue)):
        if self.queue[i].cost() < self.queue[min].cost():
          min = i
      item = copy.deepcopy(self.queue[min])
      del self.queue[min]
      return item
    
    # delete after reaching goal state 
    def delete_upper_bound(self, cost):
      if self.isEmpty():
        raise IndexError
      i = len(self.queue) - 1
      while (i >= 0) :
        if self.queue[i].cost() > cost:
          del self.queue[i]
        i-=1

      
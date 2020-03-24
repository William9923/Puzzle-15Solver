import copy

def pretty_print(matrix):
  for line in matrix:
    print(line)
    
class Puzzle:
  def __init__(self, matrix,n, path, previous):
    self.matrix = matrix
    self.dimension = n
    self.path = path
    self.previous = previous

  def __str__(self):
    return self.path
  
  def print_matrix(self):
    pretty_print(self.getMatrix())

  def isEqual(self,puzzle):
    found = False
    for i in range(self.dimension):
      for j in range(self.dimension):
        if (self.matrix[i][j] != puzzle.getMatrix()[i][j]):
          found = True
    return not found

  def posisi_blank(self):
    return self.posisi_row_column(0)

  def checkX(self):
    return 1 if (self.posisi_blank()[0] + self.posisi_blank()[1]) % 2 == 1 else 0

  def getMatrix(self):
    return copy.deepcopy(self.matrix)

  def posisi(self, val):
    i, j = self.posisi_row_column(val)
    return i * self.dimension + j

  def posisi_row_column(self, val):
    i = 0; j = 0; found = False
    while(i < self.dimension or not found) :
      j = 0
      while (j < self.dimension and not found):
        if self.matrix[i][j] == val:
          found = True
          break
        else :
          j+=1
      if found: break
      else : i+=1
    return (i,j)

  def cost(self):
    cost = 0
    for i in range(1, 15+1):
      if (self.posisi(i)+1) != i:
        cost += 1
    cost += len(self.path)
    return cost

  def iterate_kurang(self):
    for i in range(1, self.dimension * self.dimension):
      print(i, ':' ,self.kurang(i))
    print(self.dimension * self.dimension, ':', self.kurang_blank())

  def kurang(self, val):  
    """
      For angka 1 - 15
    """
    total = 0
    pos = self.posisi(val)
    for i in range(1, val):
      if (self.posisi(i) > pos):
        total += 1
    return total

  def kurang_blank(self):
    """
      For angka 0 (blank side of the puzzle)
    """
    kurang_awal = self.posisi(0)
    return self.dimension * self.dimension - kurang_awal - 1

  def sum_of_kurang(self):
    total_kurang = self.checkX()
    for i in range(1, self.dimension * self.dimension):
      total_kurang += self.kurang(i)
    total_kurang += self.kurang_blank()
    return total_kurang

  def validate_reachable(self): 
    """
      Checking wether a puzzle can be solved or not via the sum_of_kurang
    """
    return self.sum_of_kurang() % 2 == 0
  
  def validate_movement(self,movement):
    vertical, horizontal = self.posisi_row_column(0)
    if (movement == "U"):
      return True if (vertical != 0 and self.previous != "D")else False 
    elif (movement == "D"):
      return True if (vertical != (self.dimension - 1) and self.previous != "U") else False
    elif (movement == "L"):
      return True if (horizontal != 0 and self.previous != "R") else False
    elif (movement == "R"):
      return True if (horizontal != (self.dimension - 1) and self.previous != "L") else False
    else :
      return False

  def move(self, movement):
    if not self.validate_movement(movement):
      return -1
    arr = self.getMatrix()
    row, column = self.posisi_blank()
    if (movement == "U"):
        arr[row][column], arr[row-1][column] = arr[row-1][column], arr[row][column]
    if (movement == "D"):
      arr[row][column], arr[row+1][column] = arr[row+1][column], arr[row][column]
    if (movement == "L"):
      arr[row][column], arr[row][column-1] = arr[row][column - 1], arr[row][column]
    if (movement == "R"):
      arr[row][column], arr[row][column+1] = arr[row][column + 1], arr[row][column]
    return Puzzle(arr,4,self.path+movement, movement)
  
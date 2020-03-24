import copy
from time import time
from utility import getFileName, preprocessing, pretty_path, print_path_repr
from Puzzle import Puzzle
from PrioQueue import PriorityQueue

if __name__ == '__main__':
  t = time()
  prio_queue = PriorityQueue()
  filename = getFileName()

  print("Reading Files...")
  with open('../test/goal.txt' ,'r') as f:
    lines = f.readlines()
  matrix = preprocessing(lines)
  puzzle_goal = Puzzle(matrix,4,"", "")

  with open(filename, 'r') as f:
    lines = f.readlines()
  matrix = preprocessing(lines)
  puzzle_start = Puzzle(matrix, 4, "", "")

  # Print Matrix Awal:
  print("Initial Puzzle State:")
  puzzle_start.print_matrix()

  # Print letak kosong 
  blank = puzzle_start.posisi_blank()
  print("Blank In : (", blank[0] + 1, ',', blank[1] + 1, ')')

  # Print Kurang
  print("Kurang : ")
  puzzle_start.iterate_kurang()

  # Print nilai dari sum of kurang + X
  print("Sum of Kurang + X :", puzzle_start.sum_of_kurang())

  # Start Algo
  count = 0
  if (puzzle_start.validate_reachable()):
    prio_queue.insert(copy.deepcopy(puzzle_start))
    found = False
    count+=1
    while(not prio_queue.isEmpty()):
      curr_puzzle = prio_queue.delete()
      if curr_puzzle.isEqual(puzzle_goal):
        found = True
        break
      else :
        if (curr_puzzle.validate_movement("U")):
          prio_queue.insert(copy.deepcopy(curr_puzzle.move("U")))
          count+=1
        if (curr_puzzle.validate_movement("D")):
          prio_queue.insert(copy.deepcopy(curr_puzzle.move("D")))
          count+=1
        if (curr_puzzle.validate_movement("L")):
          prio_queue.insert(copy.deepcopy(curr_puzzle.move("L")))
          count+=1
        if (curr_puzzle.validate_movement("R")):
          prio_queue.insert(copy.deepcopy(curr_puzzle.move("R")))
          count+=1
    if found:
      pretty_path(curr_puzzle.path)
      print()
      print_path_repr(curr_puzzle.path, puzzle_start)
      print("Jumlah simpul yang dibangkitkan :", count)
    else :
      print("Solution Not Found")
  else:
    print("Solution is unreachable")

  t = time() - t
  print(f"Done! Time taken to solve the problem {t} seconds")
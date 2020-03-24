import sys
from Puzzle import Puzzle
import copy
# Function to get testcase filename
def getFileName():
  return sys.argv[1]

# Function to preprocess
def preprocessing(lines):
  for i in range(len(lines)):
    lines[i] =  lines[i].strip().replace("\n","").split(" ")
    lines[i] = list(map(int, lines[i]))
  return lines

# Function to pretty print the result


def pretty_path(str_path):
  path = [elem for elem in str_path]
  print("Path : ", end="")
  for i in range(len(path)):
    print(path[i], end="")
    if i != len(path) -1:
      print("→", end="")
  print()

def print_path_repr(str_path, puzzle_start):
  print("Steps:")
  curr_puzzle = copy.deepcopy(puzzle_start)
  curr_puzzle.print_matrix()
  pretty_path(curr_puzzle.path)
  path = [elem for elem in str_path]
  for move in path:
    print("↓")
    curr_puzzle = copy.deepcopy(curr_puzzle.move(move))
    curr_puzzle.print_matrix()
    pretty_path(curr_puzzle.path)
  




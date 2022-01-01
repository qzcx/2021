day = 25
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'


#each step: Left first then south

import numpy as np
def solve(input):
  grid = [ list(line.strip()) for line in open(input).readlines()]
  grid = np.array(grid)
  ret = False
  i = 0
  while not ret:
    if i % 100 == 0:
      print(f"step {i}")
      print(np.array2string(grid, separator='', formatter={'str_kind': lambda x: x}))

    ret = step(grid)
    i+=1

  print(f"Completed after {i} steps")
  print(np.array2string(grid, separator='', formatter={'str_kind': lambda x: x}))


def step(grid):
  ret = True
  height, width = grid.shape
  #Move right if possible
  r_list = np.argwhere(grid=='>')
  for ry,rx in r_list:
    rx_ = (rx+1)%width
    if grid[ry][rx_] == '.':
      grid[ry][rx_] = '>'
      grid[ry][rx] = 'x'
      ret = False
  grid[grid == 'x'] = '.'

  d_list = np.argwhere(grid=='v')
  for ry,rx in d_list:
    ry_ = (ry+1)%height
    if grid[ry_][rx] == '.':
      grid[ry_][rx] = 'v'
      grid[ry][rx] = 'x'
      ret = False

  grid[grid == 'x'] = '.'

  return ret

solve(example_input)
solve(problem_input)
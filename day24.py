day = 24
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'

"""
Solution explanation

I solved this day by trying to construct code which I could read. 

First I removed no-ops and then combined and rewrote instructions to be python

Then I examined the output and figured out that z was being used as a stack
There are a minimum of 7 pushes and 7 pops. 
To have z == 0 at the end, then you need to avoid pushing whenever possible

Each push was gated by an x_offset combined with the y_offset from the last pop

This leads to an equation which can be solved for the max value in the earlier index.
Swap max to min and that solves part 2

"""

def solve(input):
  i_list = [line.strip().split(' ') for line in open(input).readlines()]
  #4 availible registers w,x,y,z
  i_list = list(filter(remove_noop, i_list ))
  i_list = [i_list[0]] + list(map(reduce_two_instr , i_list[:-1], i_list[1:]))

  # open("day24_modified1.txt",'w').write( "\n".join(" ".join(instr) for instr in i_list if len(instr)) )

  inp_list = [i_list[0]]
  final_list = ""
  for inst in i_list[1:]:
    if len(inst) and list(inst)[0] == "inp":  
      final_list += reduce_inp(inp_list)
      inp_list = [inst]
    elif len(inst):
      inp_list.append(inst[0])
  final_list += reduce_inp(inp_list)

  open("day24_modified.txt",'w').write(final_list)

idx = 13
z_stack = []
w = list("00000000000000")
def reduce_inp(ilist):
  global idx,z_stack,w
  s = f"index {idx}\n"
  # print(ilist)
  x_offset = [inst for inst in ilist if str(inst).startswith("x +=")][0].split(" ")[-1]
  y_offset = [inst for inst in ilist if str(inst).startswith("y +=")][-1].split(" ")[-1]
  if any([ (inst == "z /= 26" ) for inst in ilist]):
    zidx, z_offset = z_stack.pop()
    print(f'{idx = }')
    print(f'{z_offset = }')
    print(f'{int(x_offset) = }')
    z_max, w_max = min( (w_max - z_offset - int(x_offset), w_max) for w_max in range(1,10) \
                            if (w_max - z_offset - int(x_offset) ) in range(1,10) )
    w[13-zidx] = str(z_max)
    w[13-idx] = str(w_max)
    print("".join(w))
  else:
    z_stack.append( (idx, int(y_offset))  )

  idx -=1

  #Can't avoid
  # if int(x_offset) >= 10:
  #   s += f"z = z * 26 + w + {y_offset}\n"
  # else:
  s += f"""if (z%26)+{x_offset} != w:
  z = z * 26 + w + {y_offset}
"""
  return s

def remove_noop(instr):
  if instr[0] in ['mul','div'] and instr[2] == '1':
    return False
  return True

def reduce_two_instr(i1,i2):
  # x = y
  if i2[0] == "mul" and i2[2] == '0':
    return []
  if i1[0] == "mul" and i1[2] == '0' and i2[0] == 'add' and i1[1] == i2[1]:
    return [f"{i1[1]} = {i2[2]}"]
  # w != x
  if " ".join(i2) == 'eql x w':
    return []
  if i1[0] == "eql" and i2[2] == '0' and i2[0] == 'eql' and i1[1] == i2[1]:
    return [f"{i1[1]} != {i1[2]}"]

  #mod
  if i2[0] == "mod":
    return [f"{i2[1]} %= {i2[2]}"]
  if i2[0] == "add":
    return [f"{i2[1]} += {i2[2]}"]
  if i2[0] == "mul":
    return [f"{i2[1]} *= {i2[2]}"]
  if i2[0] == "div":
    return [f"{i2[1]} /= {i2[2]}"]

  return i2

# solve(example_input)
solve(problem_input)
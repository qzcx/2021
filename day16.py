day = 16
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'


def solve(input, part2=False):
    hex_input = open(input).read().strip()
    bin_length = len(hex_input)*4
    msg = f"{int(hex_input,16):0{bin_length}b}"
    print(msg)

    packets, _, version_sum = parse_pkt(msg, part2)
    print(packets)
    print(version_sum)
    print(f"part 2 val {packets[2] = }")
    
def parse_pkt(msg, part2):
    if len(msg) < 6:
        print(f"Not enough bits with {msg}")
        return None, None, 0
    version = int(msg[:3],2)
    type = int(msg[3:6],2)
    # print(f"{version = }, {type = }, {msg = }")
    version_sum = 0
    if type == 4:
        literal, after_msg = parse_literal(msg[6:])
        literal = int("".join(literal),2)
        subpackets = []
    else:
        literal = ""
        subpackets, after_msg, version_sum = parse_operator(msg[6:], part2)

        #Handle operators for part 2
        if part2:
            literal = operator(subpackets, type)

    # else: #Hit the end
    #     print(f"hit the end with {msg}")
    #     return None, None
    return (version, type, literal, subpackets), after_msg, version + version_sum

def operator(sub_packets, type):
    if type == 0: #sum
        return sum([s[2] for s in sub_packets])
    elif type == 1: #prod
        prod = 1
        for s in sub_packets:
            prod *= s[2]
        return prod
    elif type == 2: #min
        return min([s[2] for s in sub_packets])
    elif type == 3: #max
        return max([s[2] for s in sub_packets])
    elif type == 5: #greater than
        assert(len(sub_packets) == 2)
        return 1 if sub_packets[0][2] > sub_packets[1][2] else 0
    elif type == 6: #less than
        assert(len(sub_packets) == 2)
        return 1 if sub_packets[0][2] < sub_packets[1][2] else 0
    elif type == 7: #equal to
        assert(len(sub_packets) == 2)
        return 1 if sub_packets[0][2] == sub_packets[1][2] else 0
    print("Bad type no return val")
def parse_literal(msg):
    vals = []
    while(True):
        print(f"Parsing literal value {msg[0] = } {msg[1:5] = }")
        vals.append( msg[1:5] )
        cont = msg[0]
        msg = msg[5:]
        if cont == '0':
            break
    return vals, msg

def parse_operator(msg, part2):
    l_id = msg[0]
    total_version_sum = 0
    if l_id == "0":
        bit_length = int(msg[1:16],2) #next 15
        print(f"Operator {l_id = }, {bit_length = }")
        msg = msg[16:]
        sub_msg = msg[:bit_length]
        subpackets = []
        while(sub_msg is not None):
            subpacket, sub_msg, version_sum = parse_pkt(sub_msg, part2)
            total_version_sum += version_sum
            if subpacket is not None:
                subpackets.append(subpacket)
        after_msg = msg[bit_length:]
    else:
        num_pkts = int(msg[1:12],2) #next 11
        print(f"Operator {l_id = }, {num_pkts = }")
        sub_msg = msg[12:]
        subpackets = []
        for i in range(num_pkts):
            subpacket, sub_msg, version_sum = parse_pkt(sub_msg, part2)
            total_version_sum += version_sum
            subpackets.append(subpacket)
        after_msg = sub_msg
    
    return subpackets, after_msg, total_version_sum


# solve(example_input)
# solve(problem_input)


solve(example_input, True)
solve(problem_input, True)
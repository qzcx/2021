day = 19
example_input = f'day{day}example.txt'
problem_input = f'day{day}input.txt'



#Each scanner detect beacons relative to their position in 3 dimensions
#Each scanner is orientated differently in 3 dimensions


#12 overlapping beacons gives confidence in the overlap

# 1. Select a starting scanner 
# 2. Check each other scanner. 
#       Check each orientation
#       Go over 

import numpy as np
from parse import search,parse 
import math


def solve(input):
    scanners = []
    with open(input) as f:
        # scanner = np.zeros((2000,2000,2000))
        scanner = []
        for line in f:
            if 'scanner' in line:
                if len(scanner) > 0: scanners.append(scanner)
                scanner = []
            elif ',' in line:
                x,y,z = parse("{},{},{}", line).fixed
                scanner.append((int(x),int(y),int(z)))
        scanners.append(scanner)
    #O(n^3)
    dist_lookup = generate_dists(scanners)
    #O(n^4)
    offsets = [0]* len(scanners)

    while(sum([ len(s) == 0 for s in scanners]) != len(scanners)-1 ):
        dist_lookup_copy = dist_lookup.copy()
        for sid1, scanner1 in enumerate(scanners.copy()):
            if len(scanners[sid1]) == 0: continue
            for sid2, scanner2 in enumerate(scanners.copy()):
                if len(scanners[sid2]) == 0 or sid1 == sid2: continue
                bid1, bid2, overlapping_points = compare_scanners(sid1, sid2, dist_lookup_copy)
                if bid1 != None:
                    pitch, roll, yaw, offset = determine_orientation(overlapping_points)
                    for sid,old_offset in enumerate(offsets):
                        #Merging so copy over offset and rotate to new perspective
                        if old_offset != 0 and sid2 == old_offset[1]: 
                            rot_offset = rotate_points([old_offset[0]], pitch, roll, yaw)[0]
                            new_offset = tuple(x+b for b,x in zip(rot_offset,offset))
                            offsets[sid] = (new_offset,sid1)
                            print(f"rotated {sid} from {sid2} to {sid1}")
                    offsets[sid2] = (offset, sid1)

                    #Add new points to scannersid1
                    combine_scanners(scanners[sid1], scanner2, pitch, roll, yaw, offset)
                    #regenerate distances for all points on scannersid1
                    new_dist = generate_dists([scanners[sid1]])
                    dist_lookup[sid1] = new_dist[0]
                    #remove old scanner from equation
                    dist_lookup[sid2] = []
                    scanners[sid2] = []
                    print(f"Combined {sid2} into {sid1} length {len(scanners[sid1])}")

    print(len(scanners[0]))
    print(offsets)
    offsets = [(0,0,0) if o==0 else o[0] for o in offsets]
    print(offsets)
    print(max( sum( [abs(x1-x2) for x1,x2 in zip(o1,o2)]) \
                    for o1 in offsets for o2 in offsets) )

def combine_scanners(scanner1, scanner2, pitch, roll, yaw, offset):
    new_points = rotate_points(scanner2,pitch=pitch, roll=roll, yaw=yaw)
    for beacon2 in new_points:
        new_point = tuple(x+b for b,x in zip(beacon2,offset))
        if (new_point not in scanner1):
            scanner1.append(new_point)

# x = a-b
# a = x+b

def generate_dists(scanners):
    dist_lookup = []
    for sid, scanner in enumerate(scanners):
        beacons = []
        for pid1,point1 in enumerate(scanner):
            beacon_dists = {}
            for pid2,point2 in enumerate(scanner):
                if pid1 == pid2: continue
                beacon_dists[str(point2)] =int(math.dist((point1), (point2)))
            beacons.append(beacon_dists)
        dist_lookup.append(beacons)
    return dist_lookup

def compare_scanners(sid1, sid2, dist_lookup):
    for bid1, beacon1 in enumerate(dist_lookup[sid1]):
        for bid2, beacon2 in enumerate(dist_lookup[sid2]):
            overlap_count = 0
            overlapping_points = []
            for point1,dist1 in beacon1.items():
                for point2,dist2 in beacon2.items():
                    if dist1 == dist2:
                        overlap_count += 1
                        overlapping_points.append((strpoint_to_list(point1),
                                                   strpoint_to_list(point2)))
            if overlap_count >= 12:
                if determine_orientation(overlapping_points) is not False:
                    return bid1, bid2, overlapping_points
    # assert(False), "No overlap found!"
    return None,None,None

def strpoint_to_list(strpoint):
    return parse("({:d}, {:d}, {:d})", strpoint).fixed


"""
rotate around x/y
rotate around y/x
rotate around y/z
rotate around z/x


x,y,z
rotate x,y
-y,x,z
-x,-y,z
y,-x,z

rotate y,z
x,-z,y
x,-y,-z
x,z,-y

x = -y

"""

def determine_orientation(overlapping_points):
    s1_points = [p[0] for p in overlapping_points]
    s2_points = [p[1] for p in overlapping_points]
    rotations = [math.pi/2*i for i in range(4)]
    for pitch in rotations:
        for roll in rotations:
            for yaw in rotations:
                new_points = rotate_points(s2_points, pitch, roll, yaw)
                if(is_aligned(s1_points, new_points,10)):
                    offset = tuple(a-b for a,b in zip(s1_points[0],new_points[0]))
                    return pitch, roll, yaw, offset
    # assert(False), "Could not determine alignment"
    return False

"""
pitch =0.0, roll = 3.141592653589793, yaw =0.0
1  0  0
0 -1  0
0  0 -1
"""


def is_aligned(s1_points, s2_points, minimum=12):
    x,y,z = (a-b for a,b in zip(s1_points[0],s2_points[0]))
    return minimum < sum([ (s1p[0] - s2p[0] == x) and 
                (s1p[1] - s2p[1] == y) and 
                (s1p[2] - s2p[2] == z)   \
                    for s1p,s2p in zip(s1_points, s2_points) ] )

import math
def rotate_points(points, pitch, roll, yaw):
    cosa = math.cos(yaw)
    sina = math.sin(yaw)

    cosb = math.cos(pitch)
    sinb = math.sin(pitch)

    cosc = math.cos(roll)
    sinc = math.sin(roll)

    Axx = round(cosa*cosb)
    Axy = round(cosa*sinb*sinc - sina*cosc)
    Axz = round(cosa*sinb*cosc + sina*sinc)

    Ayx = round(sina*cosb)
    Ayy = round(sina*sinb*sinc + cosa*cosc)
    Ayz = round(sina*sinb*cosc - cosa*sinc)

    Azx = round(-sinb)
    Azy = round(cosb*sinc)
    Azz = round(cosb*cosc)

    # print(f"{pitch =}, {roll = }, {yaw =}")
    # print(f"{int(Axx) :d}, {int(Axy): d}, {int(Axz) :d}")
    # print(f"{int(Ayx) :d}, {int(Ayy): d}, {int(Ayz) :d}")
    # print(f"{int(Azx) :d}, {int(Azy): d}, {int(Azz) :d}")

    new_points = []
    for point in points:
        px = point[0]
        py = point[1]
        pz = point[2]
        new_points.append( (int(Axx*px + Axy*py + Axz*pz),
                            int(Ayx*px + Ayy*py + Ayz*pz),
                            int(Azx*px + Azy*py + Azz*pz) ))
    return new_points

# solve(example_input)
solve(problem_input)
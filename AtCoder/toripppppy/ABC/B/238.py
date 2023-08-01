import itertools
import numpy
print(max(numpy.diff(sorted(map(lambda x:x%360,itertools.accumulate([not input()]+list(map(int,input().split())))))+[360])))
#!/usr/bin/env python3

from scratch_libs import *

print("No. of imported modules:", len(sys.modules))

#print("\nimported modules:")
#for module in sorted(sys.modules):
#    print(module, end=" | ")

array = np.array([1, 2, 3])

print(array)

print(Path(__file__).resolve().parent)

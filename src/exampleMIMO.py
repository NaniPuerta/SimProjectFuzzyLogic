from fuzzy import *
from inference import *
from defuzzyfy import *

#Variables
v1 = FuzzyVariable('x1')
v2 = FuzzyVariable('x2')

v3 = FuzzyVariable('y')
v4 = FuzzyVariable('z')

#Variable Sets
f_set1 = FuzzySet('S', 0, 100)
f_set2 = FuzzySet('M', 0, 100)
f_set3 = FuzzySet('L', 0, 100)

f_set1.set_triangular(0,25,50)
f_set2.set_triangular(25,50,75)
f_set3.set_triangular(50,75,100)

v1.addSet('S',f_set1)
v1.addSet('M',f_set2)
v1.addSet('L',f_set3)

v2.addSet('S',f_set1)
v2.addSet('M',f_set2)
v2.addSet('L',f_set3)

v3.addSet('S',f_set1)
v3.addSet('M',f_set2)
v3.addSet('L',f_set3)

v4.addSet('S',f_set1)
v4.addSet('M',f_set2)
v4.addSet('L',f_set3)

#Rules
r1 = FuzzyRule()
r1.set_rule([(v1,f_set1), (v2,f_set1)], [(v3, f_set1), (v4,f_set3)])

r2 = FuzzyRule()
r2.set_rule([(v1,f_set2), (v2,f_set2)], [(v3, f_set2), (v4,f_set2)])

r3 = FuzzyRule()
r3.set_rule([(v1,f_set3), (v2,f_set3)], [(v3, f_set3), (v4,f_set1)])

r4 = FuzzyRule()
r4.set_rule([(v1,f_set1), (v2,f_set2)], [(v3, f_set1), (v4,f_set3)])

r5 = FuzzyRule()
r5.set_rule([(v1,f_set2), (v2,f_set1)], [(v3, f_set1), (v4,f_set3)])

r6 = FuzzyRule()
r6.set_rule([(v1,f_set3), (v2,f_set2)], [(v3, f_set3), (v4,f_set1)])

r7 = FuzzyRule()
r7.set_rule([(v1,f_set2), (v2,f_set3)], [(v3, f_set3), (v4,f_set1)])

r8 = FuzzyRule()
r8.set_rule([(v1,f_set3), (v2,f_set1)], [(v3, f_set2), (v4,f_set2)])

r9 = FuzzyRule()
r9.set_rule([(v1,f_set1), (v2,f_set3)], [(v3, f_set2), (v4,f_set2)])

rule_base = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

#Example
inpt = {'x1': 35, 'x2': 75}
print(inpt)
print("\nMamdani")
print("Min. of Max.")
res = Mamdani(inpt, rule_base, min_max)
print(res)
print("Medium of Max.")
res = Mamdani(inpt, rule_base, mean_max)
print(res)
print("Max. of Max.")
res = Mamdani(inpt, rule_base, max_max)
print(res)
print("Centroid (discrete)")
res = Mamdani(inpt, rule_base, centroid)
print(res)
print("Area Bisector")
res = Mamdani(inpt, rule_base, bisector)
print(res)

print("\nLarsen")
print("Min. of Max.")
res = Larsen(inpt, rule_base, min_max)
print(res)
print("Medium of Max.")
res = Larsen(inpt, rule_base, mean_max)
print(res)
print("Max. of Max.")
res = Larsen(inpt, rule_base, max_max)
print(res)
print("Centroid (discrete)")
res = Larsen(inpt, rule_base, centroid)
print(res)
print("Area Bisector")
res = Larsen(inpt, rule_base, bisector)
print(res)

print("\nTsukamoto")
print(Tsukamoto(inpt, rule_base))
from fuzzy import *
from inference import *
from defuzzyfy import *

import matplotlib.pyplot as plt
import numpy as np

def lp(i):
    if i < 50:
        return 1
    if i >= 50 and i < 70:
        return((-1/20)*i + 7/2)
    if i >= 70:
       return(0)

def mp(i):
    if i < 60 or i >= 80:
        return(0)
    if i >= 60 and i < 65:
        return(i/5 - 12)
    if i >= 65 and i < 75:
        return(1)
    if i >= 75 and i < 80:
        return((-1/5)*i + 16)

def hp(i):
    if i < 70:
        return(0)
    if i >= 70 and i < 85:
        return(i/15 - 14/3)
    if i >= 85:
        return(1)

def bs(i):
    if i < 40:
        return(-1*i/40 + 1)
    if i >= 40:
        return(0)
    # Regular
def rs(i):
    if i < 30 or i >= 70:
        return(0)
    if i >= 30 and i < 50:
        return(i/20 - 3/2)
    if i >= 50 and i < 70:
        return(-1*i/20 + 7/2)
    # Good
def gs(i):
    if i < 60:
        return(0)
    if i >= 60:
        return(i/40 - 3/2)


def to(i):
    if i >= 60:
        return(0)
    if i < 40:
        return(1)
    if i >= 40 and i < 60:
        return(-1*i/20 + 3)
    # Maintain
def m(i):
    if i < 40:
        return(0)
    if i >= 40 and i < 60:
        return(i/20 - 2)
    if i >= 60:
        return(1)   

low = FuzzySet('LP', 0, 100)
med = FuzzySet('MP', 0, 100)
hi = FuzzySet('HP', 0, 100)
bad = FuzzySet('BS', 0, 100)
reg = FuzzySet('RS', 0, 100)
goo = FuzzySet('GS', 0, 100)
take = FuzzySet('TO', 0, 100)
maint = FuzzySet('M', 0, 100)

low.set_custom(lp)
med.set_custom(mp)
hi.set_custom(hp)
bad.set_custom(bs)
reg.set_custom(rs)
goo.set_custom(gs)
take.set_custom(to)
maint.set_custom(m)

cold = FuzzySet('C', 10, 40)
medi = FuzzySet('M', 10, 40)
hot = FuzzySet('H', 10, 40)
cold.set_triangular(10, 10, 25)
medi.set_triangular(15,25,35)
hot.set_triangular(25,40,40)

dom_temp = np.linspace(0, 50, 100)
y1 = [cold.miu(x) for x in dom_temp]
y2 = [medi.miu(x) for x in dom_temp]
y3 = [hot.miu(x) for x in dom_temp]
plt.plot(dom_temp, y1)
plt.plot(dom_temp, y2)
plt.plot(dom_temp, y3)
plt.title('Temperatura')
plt.show()

wet = FuzzySet('W', 20, 100)
nor = FuzzySet('N', 20, 100)
dry = FuzzySet('D', 20, 100)
wet.set_triangular(20,20,60)
nor.set_trapezoidal(30,50,70,90)
dry.set_triangular(60,100,100)


dom_hum = np.linspace(10, 110, 200)
y1 = [wet.miu(x) for x in dom_hum]
y2 = [nor.miu(x) for x in dom_hum]
y3 = [dry.miu(x) for x in dom_hum]
plt.plot(dom_hum, y1)
plt.plot(dom_hum, y2)
plt.plot(dom_hum, y3)
plt.title('Humedad')
plt.show()

slow = FuzzySet('S', 0, 100)
mode = FuzzySet('Mo', 0, 100)
fast = FuzzySet('F', 0, 100)
slow.set_triangular(0,0,50)
mode.set_triangular(10,50,90)
fast.set_triangular(50,100,100)

dom_speed = np.linspace(0, 110, 200)
y1 = [slow.miu(x) for x in dom_speed]
y2 = [mode.miu(x) for x in dom_speed]
y3 = [fast.miu(x) for x in dom_speed]
plt.plot(dom_speed, y1)
plt.plot(dom_speed, y2)
plt.plot(dom_speed, y3)
plt.title('Velocidad')
plt.show()

v1 = FuzzyVariable('Temperatura')
v1.addSet('Frio', cold)
v1.addSet('Medio', medi)
v1.addSet('Caliente', hot)

v2 = FuzzyVariable('Humedad')
v2.addSet('Humedo', wet)
v2.addSet('Normal', nor)
v2.addSet('Seco', dry)

v3 = FuzzyVariable('Velocidad')
v3.addSet('Lenta', slow)
v3.addSet('Moderada', mode)
v3.addSet('Rapida', fast)

r1 = FuzzyRule()
r1.add_ante_clause(v1, cold)
r1.add_ante_clause(v2, wet)
r1.add_conseq_clause(v3, slow)

r2 = FuzzyRule()
r2.add_ante_clause(v1, cold)
r2.add_ante_clause(v2, nor)
r2.add_conseq_clause(v3, slow)

r3 = FuzzyRule()
r3.add_ante_clause(v1, medi)
r3.add_ante_clause(v2, wet)
r3.add_conseq_clause(v3, slow)

r4 = FuzzyRule()
r4.add_ante_clause(v1, medi)
r4.add_ante_clause(v2, nor)
r4.add_conseq_clause(v3, mode)

r5 = FuzzyRule()
r5.add_ante_clause(v1, cold)
r5.add_ante_clause(v2, dry)
r5.add_conseq_clause(v3, mode)

r6 = FuzzyRule()
r6.add_ante_clause(v1, hot)
r6.add_ante_clause(v2, wet)
r6.add_conseq_clause(v3, mode)

r7 = FuzzyRule()
r7.add_ante_clause(v1, hot)
r7.add_ante_clause(v2, nor)
r7.add_conseq_clause(v3, fast)

r8 = FuzzyRule()
r8.add_ante_clause(v1, hot)
r8.add_ante_clause(v2, dry)
r8.add_conseq_clause(v3, fast)

r9 = FuzzyRule()
r9.add_ante_clause(v1, medi)
r9.add_ante_clause(v2, dry)
r9.add_conseq_clause(v3, fast)

rule_base = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

p1 = int(input("Temperature: "))
s1 = int(input("Humidity: "))
inpt = {'Temperatura': p1, 'Humedad': s1}
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

import numpy as np
import matplotlib.pyplot as plt
import copy

#Fuzzy Numbers
def triangular(a1, a2, a3):
    def mem(x):
        if x < a1 or x > a3:
            return 0
        if x >= a1 and x < a2:
            return (x - a1)/(a2 - a1)
        if x == a2: return 1
        if x > a2 and x <= a3:
            return (a3 - x)/(a3 - a2)
    return mem

def trapezoidal(a1, a2, a3, a4):
    def mem(x):
        if x < a1 or x > a4:
            return 0
        if x >= a1 and x < a2:
            return (x - a1)/(a2 - a1)
        if x >= a2 and x <= a3:
            return 1
        if x > a3 and x <= a4:
            return (a4 - x)/(a4 - a3)
    return mem


class FuzzySet:
    def __init__(self, name, min_val, max_val):
        self._name = name
        self._empty = True
        self._type = None
        self._vars = {}
        self._min_val = min_val
        self._max_val = max_val        

    def __getitem__(self, item):
        return self._vars[item]

    @property 
    def name(self):        
        return self._name

    @property
    def empty(self):
        return self._empty

    @property
    def vars(self):
        return self._vars

    def set_triangular(self, a1, a2, a3):
        self._membership = triangular(a1,a2,a3)

    def set_trapezoidal(self, a1, a2, a3, a4):
        self._membership = trapezoidal(a1,a2,a3,a4)

    def set_custom(self, func):
        self._membership = func

    def miu(self, var_value):
        val = self._membership(var_value)
        if self._empty: self._empty = False
        return val        

    def _triang(self, x):
        if x < self._a1 or x > self._a3:
            return 0
        if x >= self._a1 and x < self._a2:
            return (x-self._a1)/(self._a2 - self._a1)
        if x >= self._a2 and x < self._a3:
            return (self._a3 - x)/(self._a3 - self._a2)

    def _trapez(self, x):
        if x < self._a1 or x > self._a4:
            return 0
        if x >= self._a1 and x < self._a2:
            return (x-self._a1)/(self._a2 - self._a1)
        if x >= self._a2 and x < self._a3:
            return 1
        if x >= self._a3 and x < self._a4:
            return (self._a4 - x)/(self._a4) 

class FuzzyVariable:
    def __init__(self, name):
        self._name = name
        self._sets = {}

    @property
    def name(self):
        return self._name

    def addSet(self, name, fuzzy_set):
        self._sets[name] = fuzzy_set
    
    def getSet(self, name):
        return self._sets[name]


class FuzzyClause:
    def __init__(self, variable, fuzzy_set):
        self._variable = variable
        self._set = fuzzy_set

    def __str__(self):
        return f'{self._variable.name} is {self._set.name}'

    @property
    def var_name(self):
        return self._variable.name

    @property
    def fuzzy_set_name(self):
        return self._set.name

    def evaluate_as_antecedent(self, var_value):
        # try:
        #     result = self._set.vars[self._variable.name]
        # except Exception as e:
        result = self._set.miu(var_value)
        return result

    def evaluate_as_consequent(self):
        return [self._set.miu(x) for x in np.arange(self._set._min_val, self._set._max_val + 1)]

class FuzzyRule:
    def __init__(self):
        self._antecedents = []
        self._consequents = []

    def __str__(self):
        antecedent = ' and '.join(map(str, self._antecedents))
        consquent = ' and '.join(map(str, self._consequents))
        return f'If {antecedent} then {consquent}'

    def add_ante_clause(self, variable, fuzzy_set):    
        self._antecedents.append(FuzzyClause(variable, fuzzy_set))

    def add_conseq_clause(self, variable, fuzzy_set):
        self._consequents.append(FuzzyClause(variable, fuzzy_set))

    def set_rule(self, antes, conses):
        for (var, f_set) in antes:
            self.add_ante_clause(var, f_set)
        for (var, f_set) in conses:
            self.add_conseq_clause(var, f_set)

    
    class FuzzyInputVariable(FuzzyVariable):
        def __init__(self, name):
            super().__init__(self, name)
            self._value_in_sets = {}

        def fuzzify(self, value):
            for set_name, fuzzy_set in self._sets.items():
                self._value_in_sets[set_name] = fuzzy_set.miu(value)

        def get_fuzzyfied(self):
            return self._value_in_sets

    class FuzzyOutputVariable(FuzzyVariable):
        def __init__(self, name):
            super().__init__(self, name)
            self._value_in_sets = {}
from fuzzy import *

import numpy as np
import math


#input es un diccionario {var_name: var_value} para todos los métodos
def Mamdani(input, rule_base, defuzzify_func):  
    cons = {} 
    varss = {}
    for rule in rule_base:
        min_val = 1
        for antec in rule._antecedents:
            min_val = min(antec.evaluate_as_antecedent(input[antec._variable.name]), min_val)
        for conseq in rule._consequents:
            key = conseq._variable.name
            set_n = conseq._set
            evaluation = conseq.evaluate_as_consequent()
            result = [min(min_val, x) for x in evaluation]
            try:
                max_v = list(np.fmax(cons[key][1], result))
                if max_v == result:
                    cons[key][0] = set_n
                cons[key][1] = max_v
            except KeyError as e:
                cons[key] = [set_n, result]   
    return {x: [cons[x][0].name, defuzzify_func(cons[x][1], cons[x][0]._min_val, cons[x][0]._max_val)] for x in cons}


def Larsen(input, rule_base, defuzzify_func):
    cons = {} 
    varss = {}
    for rule in rule_base:
        min_val = 1
        for antec in rule._antecedents:
            min_val = min(antec.evaluate_as_antecedent(input[antec._variable.name]), min_val)
        for conseq in rule._consequents:
            key = conseq._variable.name
            set_n = conseq._set
            evaluation = conseq.evaluate_as_consequent()
            result = [min_val*x for x in evaluation]
            try:
                max_v = list(np.fmax(cons[key][1], result))
                if max_v == result:
                    cons[key][0] = set_n
                cons[key][1] = max_v
            except KeyError as e:
                cons[key] = [set_n, result]
    return {x:[cons[x][0].name, defuzzify_func(cons[x][1], cons[x][0]._min_val, cons[x][0]._max_val)] for x in cons}


def Tsukamoto(input, rule_base):
    cons = {} 
    alphas = []
    for rule in rule_base:
        min_val = 1
        for antec in rule._antecedents:
            min_val = min(antec.evaluate_as_antecedent(input[antec._variable.name]), min_val)
        alphas.append(min_val)
        for conseq in rule._consequents:
            key = conseq._variable.name
            w = _get_w(min_val, conseq._set)
            try:
                cons[key].append(w)
            except Exception as e:
                cons[key] = [w]
    output = {}
    for var in cons:
        temp = [x for x in map(lambda x,y: x*y, cons[var], alphas)]
        output[var] = (sum(temp)/sum(alphas))
    return output   


def _get_w(alpha, fuzzy_set):
    i = 0
    min_diff = math.inf
    result = fuzzy_set._max_val + 1
    for w in np.arange(fuzzy_set._min_val, fuzzy_set._max_val + 1):
        temp_diff = abs(fuzzy_set.miu(i) - alpha)
        if temp_diff < min_diff:
            min_diff = temp_diff
            result = w
        i += 1
    return result
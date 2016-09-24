# -*- coding: utf-8 -*-
"""
This is a question which randomly generates two d-digit numbers
and asks for their GCD (greatest common divisor).

Created on Sat Sep 24 11:17:52 2016

@author: martinweissman
"""

from quiz_generator import question
import jinja2

def input_function(param_values, input_values):
    """
    Function that randomly creates two numbers with a given number of digits.
    The resulting numbers are stored under the keys 'a' and 'b'.    
    """
    from random import randint
    d = param_values['digits']
    if (d < 1) or (d > 10):    
        raise IndexError("Between 1 and 10 digits only")
    minnumber = 10**(d-1)  # If d = 3, minimum is 100.
    maxnumber = (10 * minnumber) - 1 # If d = 3, maximum is 999.
    a,b = 0,0
    while a == b:    
        a = randint(minnumber,maxnumber)
        b = randint(minnumber,maxnumber)
        a,b = max(a,b), min(a,b)
    return {"a":a, "b":b}
    
def answer_function(input_values):
    """
    Function that computes the GCD of two numbers.  These are stored in the 
    input values dictionary under the keys 'a' and 'b'.
    Note the return value is a dictionary because this is required for 
    rendering the answer.
    """
    a = input_values['a']
    b = input_values['b']
    while b!= 0:
        a,b = b,a%b
    return {"answer":a}

params = {"digits":2}

q_template = jinja2.Template("""
                            What is the greatest common divisor of ${{a}}$ and ${{b}}$?
                            """)

a_template = jinja2.Template("""
                            The greatest common divisor is ${{answer}}$.
                            """)

# Below, this creates the question.
GCD_question = Question( 
    question_template = q_template,
    answer_template = a_template,
    params=params,
    input_generation_function=input_function,
    answer_generation_function=answer_function    
    )

# Tests things out!
print GCD_question.question_to_latex()
print GCD_question.answer_to_latex()

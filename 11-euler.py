#!/usr/bin/env python3

__author__ = "Jeremy Brown"
__copyright__ = "2014 Jeremy Brown"
__license__ = "MIT"

"""

Improved Eurler's Method solver

Inspired by my math homework, which showed me that Euler's Method is a very 
repetitive process.  I couldn't find a tool that would easily let me solve 
using this method and I didn't want to enter a few very similar forumlas 10 
times with different values, so I wrote one myself. I also prefer coding to 
doing my math homework so this is a compromise.

-----------------------------------------------------------------------------

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

-----------------------------------------------------------------------------

Uses the simpleeval library by Daniel Fairhead for parsing equations.
https://github.com/danthedeckie/simpleeval
Distributed under the MIT License

-----------------------------------------------------------------------------

Usage:

The script prompts for:
- the ODE
- initial value of x
- initial value of y
- value to calculate up to (last value of the table)
- step value (h), the increment of x for each result

and outputs a quick 2-column table of results.


Supported functions:
- Floor
- Ceiling
- Exponential
- Logarithm (natural, base 10, any base)
- Power
- Square root
- Sin, cos, tan
- asin, acos, atan
- sinh, cosh, tanh
- asinh, acosh, atanh

"""

"""
no y' = xy^2 - y/x
"""

from simpleeval.simpleeval import SimpleEval
import math

def function(x, y, formula_string):
	"""Evaluate the passed formula using passed variables."""
	return evaluator.eval(formula_string)

def func_y_star(x, y, h, formula_string):
	"""Calculates the y*(n+1) using the formula and passed variables."""
	return y + h * function(x, y, formula_string)

def func_y(x, y, h, formula_string):
	"""Calculates the y(n+1) using the formula and passed variables."""
	return y + h * (function(x, y, formula_string) + function(x + h, func_y_star(x, y, h, formula_string), formula_string)) / 2

def print_table(results):
	"""Prints the presults to the console."""
	print("\n---RESULTS---\n")
	for r in results:
		print(r[0], "\t", r[1])
	print()

def prompt_value(message):
	"""Prompts the user for a value and converts it to a float"""
	val = input(message)
	while not val or not (val.isdigit() or is_float(val)):
		if not (val.isdigit() or is_float(val)):
			print("Invalid input, please enter a valid number")
		val = input(message)

	return float(val)

def is_float(value):
	"""Checks if the specified value is a float"""
	try:
		float(value)
		return True
	except ValueError:
		return False


supported_functions = {"ceil": math.ceil,
					"floor": math.floor,
					"factorial": math.factorial,
					"exp": math.exp,
					"ln": math.log,
					"log": math.log,
					"log10": math.log10,
					"pow": math.pow,
					"sqrt": math.sqrt,
					"sin": math.sin,
					"cos": math.cos,
					"tan": math.tan,
					"asin": math.asin,
					"acos": math.acos,
					"atan": math.atan,
					"sinh": math.sinh,
					"cosh": math.cosh,
					"tanh": math.tanh,
					"asinh": math.asinh,
					"acosh": math.acosh,
					"atanh": math.atanh}


print("\nImproved Euler's Method ODE solver\nCopyright 2014 Jeremy Brown")
formula_string = str(input("\nEnter an ODE (with all operators, incl. *) to be solved: "))

x = prompt_value("Enter an initial x: ")
y = prompt_value("Enter an initial y: ")
MAX = prompt_value("Enter the value to calculate up to: ")
h = prompt_value("Enter the step value (h) to use for the calculation: ")

results = []
results.append([x, y])

evaluator = SimpleEval(names={"x": x, "y": y, "pi": math.pi, "e": math.e}, functions=supported_functions)
while x <= MAX:
	y = func_y(x, y, h, formula_string)
	x += h

	vals = [float("{0:.4f}".format(x)), float("{0:.4f}".format(y))]
	results.append(vals)

print_table(results)

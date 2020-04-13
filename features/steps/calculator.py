import sys
import os
from behave import given, when, then
from hamcrest import assert_that, equal_to

sys.path.insert(0, os.path.abspath('../calc_module'))
from mathcalc import MathCalc

@given(u'I have entered {number} into the calculator')
def step_impl(context, number):
    context.calc = MathCalc()
    context.calc.first = number

@given(u'I have also entered {number} into the calculator')
def step_impl(context, number):
    context.calc.second = number

@when(u'I press add')
def step_impl(context):
    context.result = context.calc.add()

@then(u'the result should be {expectedResult} on the screen')
def step_impl(context, expectedResult):
    assert_that(context.result, equal_to(int(expectedResult)))



import pytest
import sys
import os 
sys.path.insert(0, os.path.abspath('../emp_module'))
from employee import Employee

@pytest.fixture     #Marks input for a test case which is utilized in the below test 
def input_email():
   input = Employee('Corey', 'Schafer', 50000)
   return input

@pytest.fixture     #Marks input for a test case which is utilized in the below test
def input_fullname():
   input = Employee('John', 'Smith', 60000)
   return input

@pytest.mark.basictest  #Marks a set of tests into a group, you can run tests for a group using pytest command
def test_email(input_email):
    assert input_email.email == 'Corey.Schafer@email.com'   #assertion to check if the test returns required output

    input_email.first = 'John'

    assert input_email.email == 'John.Schafer@email.com'

@pytest.mark.basictest  #Marks a set of tests into a group, you can run tests for a group using pytest command
def test_fullname(input_fullname):
    assert input_fullname.fullname == 'John Smith'

    input_fullname.first = 'Sue'

    assert input_fullname.fullname == 'Sue Smith'

@pytest.mark.salarytest     #Marks a set of tests under a group, you can run tests for a group using pytest command
@pytest.mark.parametrize("emp, output",[(Employee('Corey', 'Schafer', 50000), 52500), (Employee('John', 'Smith', 60000), 63000)])
# Above line used to run the test with multiple set of inputs defined in the array, defines the argument names and values to be passed
# Value is an array with first parameter being the input value and second parameter to be the value to be compared with (expected result)
# This way test is executed with many sets of values easily
def test_apply_raise(emp, output):
    emp.apply_raise()
    assert emp.pay == output

@pytest.mark.skip   #Marks to skip a test, doesn't run the test just ignore
def test_future():
   assert 5 == 6
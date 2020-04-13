# This is required to suppress some warnings generated by pytest when you use the test group feature
# This may not be required in future releases, When grouping tests it generates a big warning message in the output, but tests are still run
# This is the programmatic way to suppress that warning, you can also suppress it by creating pytest.ini in the same folder
def pytest_configure(config):
    config.addinivalue_line(
        'markers', 'basictest: workaround for https://bitbucket.org/pytest-dev/pytest-pep8/issues/23/'
    )
    config.addinivalue_line(
        'markers', 'salarytest'
    )
# PythonRestAPITesting
![Python Testing Logo](/images/pythonTestingBanner.webp)

Example code for testing a REST API using Python Requests and Pytest.

Run from the command line with: pytest tests\01_basic_tests.py --html=pytest_report.html

or run the runMe.bat file

Report file is created as : pytest_report.html

## Goal:
* 3(4) tests for rest service available here: http://ec2-3-123-145-12.eu-central-1.compute.amazonaws.com/api

## Roles:
* Admin - superuser which has access to admin system via token
* User - client which can only query publicly opened endpoints (the ones without need of token)

## Tests
1. Smoke Test
    * Check that the API is up and healthy. If this fails, all other tests are skipped.

1. Wrong Token Test
    * Admin provides incorrect token while trying to get logs from environment

1. Admin updates fund id field
    * User can see some fund id in ‘api/v0/fund’ endpoint
    * Admin updates fund id it to different value
    * User can now see new fund id in ‘api/v0/fund’ endpoint

1. Admin clears log
    * Make sure that there is at least one log entry in logs endpoint (you can generate logs entry by querrying v0/fund or v0/challenges)
    * Admin clears log
    * Admin validates logs are cleared

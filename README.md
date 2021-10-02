# PythonRestAPITesting
Example code for testing a REST APi using Python Requests and Pytest

Setup:
pip3 install -U requests Flask pytest pytest-html

Goal:
3 tests for rest service available here: http://ec2-3-123-145-12.eu-central-1.compute.amazonaws.com/api

Roles:
Admin - superuser which has access to admin system via token
User - client which can only query publicly opened endpoints (the ones without need of token)
Steps
I Wrong Token Test
Admin provides incorrect token while trying to get logs from environment

II Admin updates fund id field
Steps:

User can see some fund id in ‘api/v0/fund’ endpoint
Admin updates fund id it to different value
User can now see new fund id in ‘api/v0/fund’ endpoint
III Admin clears log

Make sure that there is at least one log entry in logs endpoint (you can generate logs entry by querrying v0/fund or v0/challenges)
Admin clears log
Admin validates logs are cleared

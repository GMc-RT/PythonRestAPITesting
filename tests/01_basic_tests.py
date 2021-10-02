#!/usr/bin/env python
import settings
import requests
import json
import pytest
import logging

LOGGER = logging.getLogger(__name__)
# run with --html=pytest_report.html to generate the report

@pytest.mark.dependency() #skip all other tests if this fails
def test_smoke_test():
    LOGGER.info('Test 1: Check that the api is up')
    response = requests.get(settings.url + settings.health)
    status_code = response.status_code 
    if status_code == 200:
        LOGGER.info('Test 1: The API is up and healthy')
    else:
        LOGGER.critical('Test 1: Error, API seems to be down')
    assert status_code == 200

@pytest.mark.dependency(depends=["test_smoke_test"])
def test_admin_read_logs_with_incorrect_token():
    LOGGER.info('Test 2: Admin tries to read logs with incorrect auth key')  
    # try to read log using incorrect key
    response = requests.get(settings.url + settings.get_logs, headers=settings.incorrect_access_header)
    status_code = response.status_code 
    if status_code == 500:
        LOGGER.info('Test 2: The correct response (500) is given')
    else:
        LOGGER.error(f'Test 2: Error, An unexpected response occured: {status_code}')
    # Result: 500 error
    assert status_code == 500

@pytest.mark.dependency(depends=["test_smoke_test"])
def test_admin_clear_the_logs():
    LOGGER.info('Test 3: Admin clears log')
    # Make sure that there is at least one log entry in logs endpoint (you can generate logs entry by querrying v0/fund or v0/challenges)
    requests.get(settings.url + settings.get_fund)
    response = requests.get(settings.url + settings.get_logs, headers=settings.access_header)
    num_logs = len(response.content)
    if num_logs > 0:
        LOGGER.info('Test 3: There is at least one log found')
    else:
        LOGGER.error(f'Test 3: Error, Logs not created')
    assert num_logs> 0
    # Admin clears log
    response = requests.post(settings.url + settings.post_clear_logs, headers=settings.access_header)
    num_logs = len(response.content)
    # Admin validates logs are cleared
    if num_logs == 0:
        LOGGER.info('Test 3: The logs have been cleared as expected')
    else:
        LOGGER.error(f'Test 3: Error, logs are not fully cleared, there are still {num_logs} logs')
    assert num_logs == 0      

@pytest.mark.dependency(depends=["test_smoke_test"])
def test_admin_updates_fund_id_field():
    LOGGER.info('Test 4: Admin updates fund id field')

    #reset the fund_id to 3
    requests.post(settings.url + settings.fund_reset, headers=settings.access_header, json=settings.reset_body)
    # User can see some fund id in ‘api/v0/fund’ endpoint
    response = requests.get(settings.url + settings.get_fund)
    body_json = response.json()
    fund_id = body_json['id']
    if fund_id == 3:
        LOGGER.info('Test 4: The fund_id is 3 as expected')
    else:
        LOGGER.error(f'Test 4: Error, fund_id is {fund_id}, expected 3')
    assert fund_id == 3

    # Admin updates fund id it to different value
    requests.post(settings.url + settings.fund_reset, headers=settings.access_header, json=settings.update_body)
    # User can now see new fund id in ‘api/v0/fund’ endpoint
    response = requests.get(settings.url + settings.get_fund)
    body_json = response.json()
    fund_id = body_json['id']
    if fund_id == 100:
        LOGGER.info('Test 4: The fund_id is now 100 as expected')
    else:
        LOGGER.error(f'Test 4: Error, fund_id is {fund_id}, expected 100')
    assert fund_id == 100

    #reset the fund_id to 3, good practice to leave states as you found them, but disabled for speed
    #requests.post(settings.url + settings.fund_reset, headers=settings.access_header, json=settings.reset_body)








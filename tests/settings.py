url = 'http://ec2-3-123-145-12.eu-central-1.compute.amazonaws.com/'  
health = "api/health"
access_token = "Oy3hfPoH45ze7Q"
get_logs = "api/control/logs/get"
post_clear_logs = "api/control/logs/clear"
get_fund = "api/v0/fund"
fund_reset = "api/control/command/reset"
access_header = {"API-Token": access_token}
incorrect_access_header = {"API-Token": "password1234"}
update_body = {
            "initials": [
                {
                "above_threshold": 10,
                "pin": "1234"
                },
                {
                "name": "darek",
                "funds": 8000,
                "pin": "1111"
                },
                {
                "name": "german",
                "funds": 8000,
                "pin": "9999"
                },
                {
                "name": "florencia",
                "funds": 8000,
                "pin": "9999"
                },
                {
                "name": "juan",
                "funds": 8000,
                "pin": "2222"
                }
            ],
            "vote_start": 1,
            "vote_tally": 5,
            "tally_end": 6,
            "next_vote_start_time": "2021-05-31T20:00:00",
            "proposals": 150,
            "challenges": 3,
            "slot_duration": 20,
            "slots_per_epoch": 30,
            "voting_power": 2950,
            "fund_name": "Fund3",
            "private": False,
            "version": "2.0",
            "fund_id": 100, #update the Fund ID
            "reviews": 1, #missing from docs
            "block_content_max_size": 1, #missing from docs
            "linear_fees": {
                "constant": 0,
                "coefficient": 0,
                "certificate": 0
            }
            }
reset_body = {
            "initials": [
                {
                "above_threshold": 10,
                "pin": "1234"
                },
                {
                "name": "darek",
                "funds": 8000,
                "pin": "1111"
                },
                {
                "name": "german",
                "funds": 8000,
                "pin": "9999"
                },
                {
                "name": "florencia",
                "funds": 8000,
                "pin": "9999"
                },
                {
                "name": "juan",
                "funds": 8000,
                "pin": "2222"
                }
            ],
            "vote_start": 1,
            "vote_tally": 5,
            "tally_end": 6,
            "next_vote_start_time": "2021-05-31T20:00:00",
            "proposals": 150,
            "challenges": 3,
            "slot_duration": 20,
            "slots_per_epoch": 30,
            "voting_power": 2950,
            "fund_name": "Fund3",
            "private": False,
            "version": "2.0",
            "fund_id": 3, #reset the Fund ID
            "reviews": 1, #missing from docs
            "block_content_max_size": 1, #missing from docs
            "linear_fees": {
                "constant": 0,
                "coefficient": 0,
                "certificate": 0
            }
            }
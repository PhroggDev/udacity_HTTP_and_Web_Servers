#!/usr/bin/env python3
#
# Client for the UINames.com service.
#
# 1. Decode the JSON data returned by the UINames.com API.
# 2. Print the fields in the specified format.
#
# Example output:
# My name is Tyler Hudson and the PIN on my card is 4840.

import requests


def SampleRecord():
    r = requests.get("http://randomuser.me/api/?inc=name,id&nat=us",
                     timeout=2.0)
    # 1. Add a line of code here to decode JSON from the response.
    firstName = f"{r.json()['results'][0]['name']['first']}"
    lastName = f"{r.json()['results'][0]['name']['last']}"
    pinEntry = f"{r.json()['results'][0]['id']['value'][-4:]}"

    # 2. Add the correct fields from the JSON data structure.

    return f"My name is {firstName} {lastName} and the PIN on my card is {pinEntry}."

if __name__ == '__main__':
    print(SampleRecord())

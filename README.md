# API-testing

a) Test function and create input/output data sets

b) API testing
Create test-cases covering CRUD operations of booking. API description can be
found here:

[https://restful-booker.herokuapp.com/apidoc/index.html](https://restful-booker.herokuapp.com/apidoc/index.html)


a) For the method lengthOfLongestSubstring I wrote a test which checks if the function value is consistent with the expected value.
The whole thing was written in Python and with the help of Pytest.

Tests cases for random characters and the empty string.
It would be possible to add a case-insensitive search method and then use str.lower() before using lengthOfLongestSubstring.

To run test:
```
pytest longest_substring_test.py
```

Result:
![Screenshot from 2022-04-24 16-41-40](https://user-images.githubusercontent.com/81774440/164981914-b096ca5d-32d5-4203-a248-f5e5063f7288.png)


b) The purpose of these tests was to validate the API.

API passed all tests except for the one PACH test, so it appears that the API is not working properly and requires a fix for PartialUpdateBooking

The tests were written in python with the help of unittest and the functions executing the API rules with the help of requests, pycurl, io, json.

To run test:
```
nose2 --verbose
```

Result:
[
![Screenshot from 2022-04-24 16-39-15](https://user-images.githubusercontent.com/81774440/164981852-ab993c04-5fd6-46a9-9ca7-5cfdaf95c0f3.png)
](url)

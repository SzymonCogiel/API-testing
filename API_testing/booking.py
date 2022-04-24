import requests
import pycurl
from io import BytesIO
import json

BOOK_URL = 'https://restful-booker.herokuapp.com/booking'


def get_books():
    """Get list of book"""
    response = requests.get(BOOK_URL)
    if response.ok:
        return response
    else:
        return None


def get_dict_len():
    all_books = get_books().json()
    return len(all_books)


def get_info_book(n: int):
    # Creating a buffer as the cURL is not allocating a buffer for the network response
    buffer = BytesIO()
    c = pycurl.Curl()
    # initializing the request URL
    c.setopt(c.URL, '{0}/{1}'.format(BOOK_URL, n))
    # setting options for cURL transfer
    c.setopt(c.WRITEDATA, buffer)
    # perform file transfer
    c.perform()
    # Ending the session and freeing the resources
    c.close()
    # retrieve the content BytesIO
    body = buffer.getvalue()
    pop = json.loads(body.decode('utf-8'))
    return pop


def create_booking():
    data = {
        "firstname": "Zu",
        "lastname": "Zu",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.post(BOOK_URL, json=data, headers=headers)
    print(r.status_code, r.reason)
    return r.status_code, r.reason

    """ALTERNATIVE"""
    # c = pycurl.Curl()
    # # initializing the request URL
    # c.setopt(c.URL, 'https://restful-booker.herokuapp.com/booking')
    # # the data that we need to Post
    # post_data = {
    #     "firstname" : "Jacu",
    #     "lastname" : "Placu",
    #     "totalprice" : 999,
    #     "depositpaid" : True,
    #     "bookingdates" : {
    #         "checkin" : "2018-01-01",
    #         "checkout" : "2019-01-01"
    #     },
    #     "additionalneeds" : "Breakfast"
    # }
    # # encoding the string to be used as a query
    # postfields = urlencode(post_data)
    # # setting the cURL for POST operation
    # c.setopt(c.POSTFIELDS, postfields)
    # # perform file transfer
    # c.perform()
    # # Ending the session and freeing the resources
    # c.close()


def update_booking(n: int):
    # Making a PUT request
    _, _, token = create_token()
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': 'token={0}'.format(token["token"])}
    r = requests.put('https://restful-booker.herokuapp.com/booking/{0}'.format(n), json={
        "firstname": "Zu",
        "lastname": "Zu",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }, headers=headers)

    # check status code for response received
    # success code - 200
    print(r)

    # print content of request
    print(r.content)
    return r.status_code, r.content


def part_update_booking(n: int):
    _, _, token = create_token()
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': 'token={0}'.format(token["token"])}

    # Making a PUT request
    r = requests.put('{0}/{1}'.format(BOOK_URL, n), data={
        "firstname": "Zu",
        "lastname": "La"
    }, headers=headers)

    # check status code for response received
    # success code - 200
    print(r)

    # print content of request
    print(r.content)
    return r, r.content


def delete_booking(n: int):
    _, _, token = create_token()
    headers = {'Content-Type': 'application/json', 'Cookie': 'token={0}'.format(token["token"])}
    r = requests.delete('https://restful-booker.herokuapp.com/booking/{0}'.format(n), headers=headers)
    return r.status_code, r.text


def get_ping():
    response = requests.get("https://restful-booker.herokuapp.com/ping")
    # if 201 Created
    if response.ok:
        return response.status_code
    else:
        return None


def create_token():
    url_post = 'https://restful-booker.herokuapp.com/auth'
    data = {
        "username": "admin",
        "password": "password123"
    }
    r = requests.post(url_post, data=data)
    token = json.loads(r.content.decode('utf-8'))
    return r.status_code, r.reason, token


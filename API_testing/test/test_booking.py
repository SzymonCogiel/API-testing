import unittest
from booking import get_books, get_info_book, get_dict_len, create_booking, update_booking, part_update_booking, delete_booking, get_ping, create_token
from unittest.mock import patch

class TestAPI(unittest.TestCase):

    # CHECKING GetBookingIds response
    @patch('booking.requests.get') # Mock 'requests' module 'get' method.
    def test_book_response_code(self, mock_get):
        """Mocking using a decorator"""
        mock_get.return_value.status_code = 200  # Mock status code of response.
        response = get_books()

        # Assert that the request-response cycle completed successfully with status code 200.
        self.assertEqual(response.status_code, 200)  # add assertion here


    # CHECKING GetBooking
    def test_book_response_value(self):
        foo = {
            "firstname": True,
            "lastname": True,
            "totalprice": True,
            "depositpaid": True,
            "bookingdates": {
                "checkin": True,
                "checkout": True
            },
            "additionalneeds": True}
        cos = get_info_book(get_dict_len())
        assert cos.keys() == foo.keys()


    # CHECKING CreateBooking
    def test_create_book(self):
        r, mess = create_booking()
        assert r == 200, mess


    # CHECKING CreateBooking
    def test_update_book(self):
        r, mess = update_booking(1)
        assert r == 200, mess


    # CHECKING PartialUpdateBooking
    def test_part_update_book(self):
        r, mess = part_update_booking(1)
        assert r == 200, mess


    # CHECKING DeleteBooking
    def test_delete_booking(self):
        create_booking()
        id = get_dict_len()
        r, mess = delete_booking(id)
        assert r == 201, mess
        x, _ = delete_booking(id)
        assert x == 405, "No existet"


    # CHECKING Ping
    def test_get_ping(self):
        r = get_ping()
        assert r == 201, r

    # CHECKING CreateToken
    def test_create_token(self):
        r, t, _ = create_token()
        assert r == 200, t


if __name__ == '__main__':
    unittest.main()

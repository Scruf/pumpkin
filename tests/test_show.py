import sys, os
import pytest
sys.path.append(os.getcwd())

from show import handler
from db.consts import get_response_object


def test_show_handler():
    assert handler(None, None) == get_response_object(400, {"error":"Missing path parameter"}, {})

    assert handler({"pathParameters":{}}, None) ==  get_response_object(400, {"error":"Id Cannot be left empty"}, {})

    assert handler({"pathParameters":{"id":"asd"}}, None) ==  get_response_object(400, {"error":f"Could not fetch pet information for pet id asd"}, {})

    assert(handler({"pathParameters":{"id":"48122b1504e0460ead3a11f32af11a26"}}, None)) == get_response_object(200, {}, {"result":181.8})

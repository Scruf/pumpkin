import sys, os, json
import pytest
sys.path.append(os.getcwd())

from db.consts import get_response_object

def test_get_response_object():
	assert get_response_object(123, None, None) == {"statusCode": 123,
													    "headers": {
													        "Access-Control-Allow-Origin": "*",
													        "Access-Control-Allow-Credentials": True,
													        "Access-Control-Expose-Headers": "WWW-Authenticate, Server-Authorization, Content-Range",
													        "Content-Type":"application/json"
													    },
													    "body":json.dumps({
													        "error":None,
													        "body": None
													    })
													}
													    
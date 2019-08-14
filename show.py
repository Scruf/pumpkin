import logging
from db.driver import Connection
from db.query import get_quote
from db.consts import get_response_object

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def handler(event, context):
    conn = Connection()

    if not event:
        return get_response_object(
                    400,
                    {"error": "Missing path parameter"}, {})

    path_parameters = event.get("pathParameters")
    id = path_parameters.get("id")
    if not id:
        return get_response_object(
                    400,
                    {"error": "Id Cannot be left empty"}, {})

    quote, err = get_quote(id, conn.get_connection())

    if err:
        return get_response_object(
                    400,
                    {"error":
                        f"Could not fetch pet information for pet id {id}"},
                    {})

    return get_response_object(200, {}, {"result": quote})

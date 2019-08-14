import json

AGE_FACTORS = {
    '<1': 1.01,
    '1': 1.015,
    '2': 1.019,
    '3': 1.024,
    '4': 1.028,
    '5': 1.03,
    '6': 1.034,
    '7': 1.038,
    '8': 1.044,
    '>8': 1.055
}

ZIPCODE_FACTORS = {
    '90210': 1.01,
    '10001': 1.015,
    '02481': 1.019,
    '11217': 1.024,
    'DEFAULT': 1.013
}

DOG_BREED_FACTORS = {
    'golden_retriever': 1.01,
    'dachshund': 1.015,
    'chesapeake_bay_retriever': 1.002,
    'DEFAULT': 1.005
}

CAT_BREED_FACTORS = {
    'siamese': 1.01,
    'maine_coon': 1.015,
    'ragdoll': 1.002,
    'DEFAULT': 1.005
}

SPECIES_FACTORS = {
    'dog': 1,
    'cat': 0.99
}


def get_response_object(response_code, error_value, payload):
    return {
        "statusCode": response_code,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
            "Access-Control-Expose-Headers": "WWW-Authenticate, Server-Authorization, Content-Range",
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "error": error_value,
            "body": payload
        })
    }

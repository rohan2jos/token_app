def check_data_payload_validity(data):
    """
    :param data:        The data payload that we got in the request
    Return:             True: The data payload is valid
                        False: The data payload is not valid
    """
    if data.get('name') is None or data.get('phone') is None or data.get('email') is None:
        return False
    return True


def generate_response(message, status):
    """
    :param message:     The message that is being added to the response
                        dict
    :param status:      The status that has to be added to the response
                        dict
    return:             A dict containing the message and the response
                        status

    example:
    {
        "error": "payload validation failed",
        "status": "400"
    }
    """
    response_obj = {
        "message": message,
        "status": status
    }
    return response_obj

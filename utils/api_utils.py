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

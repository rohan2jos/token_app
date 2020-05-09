import re

def check_data_payload_validity(data):
    """
    :param data:        The data payload that we got in the request
    Return:             True: The data payload is valid
                        False: The data payload is not valid
    """

    # regular expressions for the payload check
    pat_name = r'^([a-z]+)( [a-z]+)*( [a-z]+)*$'
    pat_phone = r'^[7-9][0-9]{9}$'
    pat_email = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    # check if we have the appropriate payload data
    if data.get('name') is not None and data.get('phone') is not None and data.get('email') is not None:    
        
        # validate each element of the payload
        if re.match(pat_phone, data.get('phone')) and re.match(pat_name, data.get('name'), re.IGNORECASE) and re.match(pat_email, data.get('email')):
            return True 
        return False
    return False


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

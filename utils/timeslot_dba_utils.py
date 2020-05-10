def generate_timeslot_doc(timeslot):
    """
    :param timeslot:        The timeslot for which the document has to be created
                            The timeslot is in string
    :return                 The document dict that is created with the timeslot
    """
    timeslot_dict = {
        "timeslot": timeslot,
        "assigned": False,
        "user": ""
    }
    return timeslot_dict



def filter_dict(orig_dict: dict, filter_keys: list) -> dict:
    """

    :param orig_dict:
    :param filter_keys:
    :return:
    """
    filtered_dict = {}
    for key, value in orig_dict.items():
        if key in filter_keys:
            filtered_dict[key] = value

    return filtered_dict


def filter_list_of_dict(orig_list: list, filter_keys: list) -> list:
    """

    :param orig_list:
    :param filter_keys:
    :return:
    """
    filtered_list = []

    for orig_dict in orig_list:
        filtered_dict = {}
        for key, value in orig_dict.items():
            if key in filter_keys:
                filtered_dict[key] = value

        filtered_list.append(filtered_dict)

    return filtered_list

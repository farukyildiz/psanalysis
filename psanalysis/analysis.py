from operator import itemgetter

from .process import *
from .helpers import *


def connections(pid: int, filter_keys: list = None, sort_key: str = None, reverse: bool = False) -> list:
    """

    :param pid: process id
    :param filter_keys: ['fd', 'family', 'type', 'laddr', 'raddr', 'status']
    :param sort_key: ['fd']
    :param reverse:
    :return:
    """
    if filter_keys is None:
        filter_keys = []

    _process = get_process_as_dict_by_pid(pid)
    _connections = _process.get("connections")

    connections_list = [item._asdict() for item in _connections]
    filtered_list = filter_list_of_dict(connections_list, filter_keys) if filter_keys else connections_list
    sorted_list = sorted(filtered_list, key=itemgetter(sort_key), reverse=reverse) if sort_key else filtered_list

    return sorted_list

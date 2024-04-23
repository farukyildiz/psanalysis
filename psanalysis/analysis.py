from operator import itemgetter

from .process import *
from .helpers import *


def connections(pid: int, filter_keys: list = [], sort_key: str = None, reverse: bool = False) -> list:
    """
    filter_key = ['fd', 'family', 'type', 'laddr', 'raddr', 'status']
    sort_key = ['fd']
    """
    _process = get_process_as_dict_by_pid(pid)
    connections = _process.get("connections")
    
    connections_list = [item._asdict() for item in connections]
    filtered_list = filter_list_of_dict(connections_list, filter_keys) if filter_keys else connections_list
    sorted_list = sorted(filtered_list, key=itemgetter(sort_key), reverse=reverse) if sort_key else filtered_list
    
    return sorted_list

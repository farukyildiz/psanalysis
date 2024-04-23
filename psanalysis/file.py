from operator import itemgetter

from .process import *
from .helpers import *


def open_files(pid: int, filter_keys: list = [], sort_key: str = None, reverse: bool = False) -> list:
    """
    filter_key = ['path', 'fd', 'position', 'mode', 'flags']
    sort_key = ['fd', 'position', 'flags']
    """
    _process = get_process_as_dict_by_pid(pid)
    open_files = _process.get("open_files")
    
    open_files_list = [item._asdict() for item in open_files]
    filtered_list = filter_list_of_dict(open_files_list, filter_keys) if filter_keys else open_files_list
    sorted_list = sorted(filtered_list, key=itemgetter(sort_key), reverse=reverse) if sort_key else filtered_list
    
    return sorted_list


def file_of_descriptors_number(pid: int) -> int:
    """
    """
    _process = get_process_as_dict_by_pid(pid)
    return _process.get("num_fds")

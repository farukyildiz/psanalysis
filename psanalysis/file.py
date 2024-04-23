from operator import itemgetter

from .process import *
from .helpers import *


def open_files(pid: int, filter_keys: list = None, sort_key: str = None, reverse: bool = False) -> list:
    """
    :param pid: process id
    :param filter_keys: ['path', 'fd', 'position', 'mode', 'flags']
    :param sort_key: ['fd', 'position', 'flags']
    :param reverse:
    :return:
    """
    if filter_keys is None:
        filter_keys = []

    _process = get_process_as_dict_by_pid(pid)
    _open_files = _process.get("open_files")

    open_files_list = [item._asdict() for item in _open_files]
    filtered_list = filter_list_of_dict(open_files_list, filter_keys) if filter_keys else open_files_list
    sorted_list = sorted(filtered_list, key=itemgetter(sort_key), reverse=reverse) if sort_key else filtered_list

    return sorted_list


def file_of_descriptors_number(pid: int) -> int:
    """

    :param pid:
    :return:
    """
    _process = get_process_as_dict_by_pid(pid)
    return _process.get("num_fds")

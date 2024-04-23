from operator import itemgetter

from .process import *
from .helpers import *


def process_memory_info(pid: int) -> dict:
    """
    Get memory information of process with pid and return as dict.
    {
         'rss': 11714560,
         'vms': 69586944,
         'shared': 3796992,
         'text': 5025792,
         'lib': 0,
         'data': 10055680,
         'dirty': 0,
         'uss': 7917568,
         'pss': 8339456,
         'swap': 0
    }

    - rss: Resident Set Size
    - vms: Virtual Memory Size
    - shared: This data matches top command output's SHR column
    - text: text resident set, This data matches top command output's CODE column
    - lib: used by shared libraries
    - data: data resident set, This data matches top command output's DATA column
    - dirty: dirty pages number
    - uss: Unique Set Size
    - pss: Proportional Set Size
    - swap

    :param pid: process pid
    :return: memory information of process as dict
    """
    _process = get_process_as_dict_by_pid(pid)
    _process.get("memory_full_info")._asdict()

    return _process.get("memory_full_info")._asdict()


def memory_maps(pid: int, filter_keys: list = None, sort_key: str = None, reverse: bool = False) -> list:
    """
    Get memory maps of process with pid and return as list.
    [
        {
            'path': '/usr/sbin/...',
            'rss': 872448,
            'size': 8159232,
            'pss': 485376,
            'shared_clean': 692224,
            'shared_dirty': 0,
            'private_clean': 0,
            'private_dirty': 180224,
            'referenced': 622592,
            'anonymous': 180224,
            'swap': 0
        }
    ]

    :param pid: process pid
    :param filter_keys: ['path', 'rss', 'size', 'pss', 'shared_clean', 'shared_dirty', 'private_clean', 'private_dirty',
    'referenced', 'anonymous', 'swap']
    :param sort_key: ['rss', 'size', 'pss', 'shared_clean', 'shared_dirty', 'private_clean', 'private_dirty', 'referenced',
    'anonymous', 'swap']
    :param reverse: reverse list
    :return: filtered and sorted list of memory maps
    """
    if filter_keys is None:
        filter_keys = []

    _process = get_process_as_dict_by_pid(pid)
    _memory_maps = _process.get("memory_maps")

    memory_map_list = [item._asdict() for item in _memory_maps]
    filtered_list = filter_list_of_dict(memory_map_list, filter_keys) if filter_keys else memory_map_list
    sorted_list = sorted(filtered_list, key=itemgetter(sort_key), reverse=reverse) if sort_key else filtered_list

    return sorted_list

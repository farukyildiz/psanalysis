from operator import itemgetter

from .process import *
from .helpers import *


def process_memory_info(pid: int) -> dict:
    """
    """
    _process = get_process_as_dict_by_pid(pid)
    _process.get("memory_full_info")._asdict()
    
    return _process.get("memory_full_info")._asdict()
    

def memory_maps(pid: int, filter_keys: list = [], sort_key: str = None, reverse: bool = False) -> list:
    """
    filter_key = ['path', 'rss', 'size', 'pss', 'shared_clean', 'shared_dirty', 'private_clean', 'private_dirty', 'referenced', 'anonymous', 'swap']
    sort_key = ['rss', 'size', 'pss', 'shared_clean', 'shared_dirty', 'private_clean', 'private_dirty', 'referenced', 'anonymous', 'swap']
    """
    _process = get_process_as_dict_by_pid(pid)
    memory_maps = _process.get("memory_maps")
    
    memory_map_list = [item._asdict() for item in memory_maps]
    filtered_list = filter_list_of_dict(memory_map_list, filter_keys) if filter_keys else memory_map_list
    sorted_list = sorted(filtered_list, key=itemgetter(sort_key), reverse=reverse) if sort_key else filtered_list
    
    return sorted_list
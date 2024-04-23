from psutil import process_iter, Process, pid_exists


def get_process_as_dict_by_pid(pid: int) -> dict:
    """

    :param pid:
    :return:
    """
    try:
        if not pid_exists(pid):
            print(f"Cannot find process by pid: {pid}")
            return {}

        _process = Process(pid)
        return _process.as_dict()
    except Exception as exception:
        print(f"Err in get_process_as_dict_by_pid: {exception}")
        return {}


def get_process_as_dict_by_name(name: str) -> dict:
    """

    :param name:
    :return:
    """
    try:
        for _process in process_iter():
            if _process.name() == name:
                return _process.as_dict()

        print(f"Cannot find process by name: {name}")
        return {}
    except Exception as exception:
        print(f"Err in get_process_as_dict_by_pid: {exception}")
        return {}

def x():
    print("test-0001")
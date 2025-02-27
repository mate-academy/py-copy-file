from itertools import zip_longest


def copy_file(command: str) -> None:
    command_dict = {"cp": None, "src_name": None, "dst_name": None}
    command_dict = dict(zip_longest(command_dict, command.split()))
    if (command_dict["cp"] != "cp"
            or command_dict["src_name"] is None
            or command_dict["dst_name"] is None):
        return

    try:
        with (open(command_dict["src_name"], "r") as src_file,
              open(command_dict["dst_name"], "w") as dst_file):
            dst_file.write(src_file.read())
    except FileNotFoundError:
        return

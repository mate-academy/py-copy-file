from contextlib import ExitStack


def copy_file(cmd: str) -> None:
    cmd_list = cmd.split()

    if len(cmd_list) == 3 and cmd_list[0] == "cp":
        _, existing_file, new_file = cmd_list

        if existing_file != new_file:
            with ExitStack() as stack:
                file_in = stack.enter_context(open(existing_file, "r"))
                file_out = stack.enter_context(open(new_file, "w"))
                file_out.write(file_in.read())

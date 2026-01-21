import os


def copy_file(command: str) -> None:
    command_kv = command.split()

    if (len(command_kv) == 3 and command_kv[0] == "cp"
            and command_kv[1] != command_kv[2]
            and os.path.exists(command_kv[1])
            and not os.path.exists(command_kv[2])):
        with (open(command_kv[1], "r") as file_in,
              open(command_kv[2], "w") as file_out):
            file_out.write(file_in.read())

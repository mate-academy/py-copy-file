from pathlib import Path


def copy_file(command: str) -> None:
    command_list = command.split(" ")

    if len(command_list) != 3:
        return

    if command_list[1] == command_list[2]:
        return

    if command_list[0] == "cp":

        if not Path(command_list[1]).is_file():
            return

        with (open(command_list[1], "r") as file_in,
              open(command_list[2], "w") as file_out):
            file_out.write(file_in.read())


# if __name__ == "__main__":
#    copy_file("cp test3.txt test2.txt")

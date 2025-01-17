def copy_file(command: str) -> None:
    separate = command.split()
    with open(separate[1], "r") as copy, open(separate[2], "w") as new_file:
        if separate[1] == separate[2]:
            pass
        else:
            for item in copy:
                new_file.write(item)

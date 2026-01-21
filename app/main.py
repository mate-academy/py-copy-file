def copy_file(command: str) -> None:
    try:
        cmd, firs_file, second_file = command.split()
    except ValueError:
        print("Value cmd must be 3")
        return

    if cmd != "cp":
        print("CMD must start at cp")
        return

    if firs_file == second_file:
        return

    try:
        with (open(firs_file, "r") as file_in,
              open(second_file, "w") as file_out):
            file_out.write(file_in.read()
                           )

    except FileNotFoundError:
        pass

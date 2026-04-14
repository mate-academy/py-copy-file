def copy_file(command: str) -> None:
    try:
        cmd, file_in, file_out = command.split()

        if file_in == file_out or cmd != "cp":
            return

        with open(file_in) as f_in, open(file_out, "w") as f_out:
            f_out.write(f_in.read())
    except ValueError:
        print("Command must be not empty.")
    except FileNotFoundError:
        print("No such file.")

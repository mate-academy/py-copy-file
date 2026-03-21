def copy_file(command: str) -> None:
    try:
        operation, file_in, file_out = command.split(" ")

        if operation != "cp":
            return

        if file_in != file_out:
            with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
                f_out.writelines(f_in.readlines())
    except Exception:
        pass

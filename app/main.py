def copy_file(command: str) -> None:
    try:
        cp, f1_name, f2_mame = command.split()
    except Exception:
        return

    if f1_name == f2_mame or cp != "cp":
        return

    try:
        with open(f1_name, "r") as file_in, open(f2_mame, "w") as file_out:
            file_out.write(file_in.read())
    except Exception:
        return

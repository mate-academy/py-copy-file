def copy_file(command: str) -> None:
    cmd_mapped = command.split()
    if len(cmd_mapped) != 3:
        return
    if cmd_mapped[1] == cmd_mapped[2]:
        return
    if cmd_mapped[0] != "cp":
        return
    try:
        with (open(cmd_mapped[1], "r") as file_in,
              open(cmd_mapped[2], "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"file {cmd_mapped[1]} not found")
    except Exception:
        print(f"failed to copy file {cmd_mapped[1]}")

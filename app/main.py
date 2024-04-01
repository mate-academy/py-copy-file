def copy_file(command: str) -> None:
    try:
        command, file_in, file_out = command.split()
        if file_in != file_out and command == "cp":
            with (open(file_in, "r") as file_in,
                  open(file_out, "w") as file_out):
                file_out.write(file_in.read())
    except Exception:
        print("You have to write 'cp file_in_name file_out_name' "
              "separated with space for copying some file")

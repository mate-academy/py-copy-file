from os import path


def copy_file(command: str) -> None:
    com, filename_in, filename_out = command.split()
    if (com == "cp" and filename_in != filename_out
            and path.exists(filename_in)):
        with (open(filename_in, "r") as file_in,
              open(filename_out, "w") as file_out):
            file_out.write(file_in.read())

def copy_file(command: str) -> None:
    try:
        cp, name_out, name_in = command.split()
        if cp == "cp" and name_out != name_in:
            with (open(name_out, "r") as file_out,
                  open(name_in, "w") as file_in):
                for line in file_out:
                    file_in.write(line)
    except ValueError:
        print("Something missed in command")
    except FileNotFoundError:
        print("File not found")

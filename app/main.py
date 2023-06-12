def copy_file(command: str) -> None:
    try:
        cmd, old_file, new_file = command.split()
    except ValueError:
        print("You put incorrect data")
    else:
        try:
            if old_file == new_file:
                raise ValueError(f"You can't copy {old_file}"
                                 f" with the same name!")
            if cmd != "cp":
                raise ValueError(f"This command {cmd} unavailable."
                                 f" You can just copy file!")
            if not (old_file.endswith(".txt") and new_file.endswith(".txt")):
                raise ValueError("File's format is wrong."
                                 " It must be just '.txt'")

            with (open(old_file, "r") as file_in,
                  open(new_file, "w") as file_out):
                file_out.write(file_in.read())
        except ValueError as ve:
            print(f"{ve}")
        except FileNotFoundError:
            print(f"File {file_in} doesn't exist"
                  f" or situated in another directory")

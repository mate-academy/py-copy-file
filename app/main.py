def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        try:
            copy, old_file, new_file = command.split()

            if old_file != new_file or copy == "cp":
                with (
                    open(old_file, "r") as file_int,
                    open(new_file, "w") as file_out
                ):
                    file_out.write(file_int.read())
        except ValueError:
            print(
                "Invalid command, must be like:"
                "cp file_name.txt new_file_name.txt"
            )
        except FileNotFoundError:
            print("Your file that needs to copied can not be found")

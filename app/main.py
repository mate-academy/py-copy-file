def copy_file(command: str) -> None:
    try:
        cp, current_file, new_file = command.split(" ")
        if cp != "cp":
            raise ValueError("Command should start with 'cp'")
        if current_file == new_file:
            print(
                f"Source and destination files are the same: "
                f"'{current_file}'. No action taken."
            )
            return

        with (
            open(current_file, "r") as file_in,
            open(new_file, "w") as file_out
        ):
            data_in = file_in.read()
            file_out.write(data_in)
            print(
                f"File '{current_file}' was successfully "
                f"copied to '{new_file}'."
            )

    except FileNotFoundError:
        print(f"Error: File '{current_file}' does not exist.")

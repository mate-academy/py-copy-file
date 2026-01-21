def copy_file(command: str) -> None:
    command_name, source, destination, *_ = command.split()
    if command_name != "cp" or source == destination:
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
        print(f"File {source} has been copied to {destination}")
    except FileNotFoundError:
        print(f"File {source} does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

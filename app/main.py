def copy_file(command: str) -> None:
    if not command:
        print("Error: Command empty")
        return
    if len(command.split()) != 3:
        print("Incorrect command format")
        return

    perform_copy, source_file, destination_file = command.split()

    if source_file == destination_file:
        return
    if perform_copy != "cp":
        print("Error: Invalid command. Only 'cp' is allowed.")
        return

    try:
        with (open(source_file, "r") as main_file,
              open(destination_file, "w") as copy_file):
            for line in main_file:
                copy_file.write(line)

    except FileNotFoundError:
        print(f"Error {source_file} not found")

    except Exception as e:
        print(e)

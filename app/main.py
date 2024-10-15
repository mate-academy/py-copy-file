import os


def copy_file(command: str) -> str:
    parts = command.split()

    if not all([len(parts) == 3, parts[0] == "copy"]):
        return (
            f"Invalid command format. "
            f"Use: copy '{parts[1]}' '{parts[2]}'."
        ) if len(parts) > 2 else "Invalid command format."

    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        return (
            f"Source and destination files are the same ('{source_file}'). "
            f"No action taken."
        )

    if not os.path.isfile(source_file):
        return f"Error: Source file '{source_file}' not found."

    try:
        with (
            open(source_file, "r") as file_in,
            open(destination_file, "w") as file_out
        ):
            file_out.write(file_in.read())
        return (
            f"Successfully copied '{source_file}' to '{destination_file}'."
        )
    except IOError as error:
        return (
            f"An I/O error occurred while copying '{source_file}' to "
            f"'{destination_file}': {error}"
        )
    except Exception as error:
        return f"An unexpected error occurred: {error}"


def main() -> None:
    source_file = input("Enter the path of the source file: ")
    destination_file = input("Enter the name/path for the destination file: ")
    command = f"copy {source_file} {destination_file}"
    result = copy_file(command)
    print(result)


if __name__ == "__main__":
    main()

from pathlib import Path


def copy_file(command: str) -> None:
    try:
        _command, input_file, output_file = command.split()
        input_file = Path(input_file)
        if input_file.exists():
            if input_file != output_file and _command == "cp":
                with open(input_file, "r") as file_in, open(output_file, "w") as file_out:
                    file_out.write(file_in.read())
    except ValueError as error:
        print(error)

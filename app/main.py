import os


def copy_file(command: str) -> None:
    elements = command.split()
    try:
        if not command.startswith("cp"):
            raise ValueError
        os.path.exists(elements[1])
        if elements[1] != elements[2]:
            with open(elements[1], "r") as file_out, open(
                elements[2], "w"
            ) as file_in:
                text = file_out.read()
                file_in.write(text)
                print(f"File {elements[1]} copied to file {elements[2]}")
    except FileNotFoundError:
        print(f"File {elements[1]} does not exist")
    except ValueError:
        print(f"Incorrect command name: {elements[0]}")

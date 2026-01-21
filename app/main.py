from pathlib import Path


def copy_file(command: str) -> None:
    if isinstance(command, str):
        list_of_files = command.split(" ")
        if "cp" in list_of_files:
            if len(list_of_files) == 3:
                filee = list_of_files[1]
                new_file = list_of_files[2]
                if filee == new_file:
                    return
                elif Path(filee).is_file():
                    with open(f"{filee}", "r") as file_in:
                        reader = file_in.read()

                    with open(f"{new_file}", "w") as file_out:
                        file_out.write(f"{reader}")

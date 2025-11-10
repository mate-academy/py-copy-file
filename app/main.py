from typing import TextIO


class ReadingManager:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path

    def __enter__(self) -> TextIO:
        self.file = open(self.source_path, "r")
        return self.file

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        self.file.close()


class WritingManager:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path

    def __enter__(self) -> TextIO:
        self.file = open(self.source_path, "w")
        return self.file

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        self.file.close()


def copy_file(command: str) -> None:
    command_files_list = command.split()
    if len(command_files_list) != 3 or command_files_list[0] != "cp":
        return

    source_file_name = command_files_list[1]
    distribution_file_name = command_files_list[2]
    if source_file_name == distribution_file_name:
        return
    try:
        with (ReadingManager(source_file_name) as src_obj,
              WritingManager(distribution_file_name) as dst_obj):
            for line in src_obj:
                dst_obj.write(line)
    except FileNotFoundError:
        return

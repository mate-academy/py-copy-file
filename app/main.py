class ReadingManager:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path

    def __enter__(self) -> str:
        self.file = open(self.source_path, "r")
        return self.file

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        self.file.close()


class WritingManager:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path

    def __enter__(self) -> str:
        self.file = open(self.source_path, "w")
        return self.file

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        self.file.close()


def copy_file(command: str) -> None:
    command_files_list = command.split()
    if len(command_files_list) != 3 or command_files_list[0] != "cp":
        return

    src_file = command_files_list[1]
    dst_file = command_files_list[2]
    if src_file == dst_file:
        return
    try:
        with (ReadingManager(src_file) as src_obj,
              WritingManager(dst_file) as dst_obj):
            for line in src_obj:
                dst_obj.write(line)
    except FileNotFoundError:
        return "No such file or directory"

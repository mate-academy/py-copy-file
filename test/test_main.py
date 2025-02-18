import pytest
import os
from app.main import copy_file

@pytest.fixture
def setup_files():
    # Создание тестовых файлов
    with open("file.txt", "w") as f:
        f.write("Test content")
    assert os.path.exists("file.txt")  # Убедимся, что файл создан

    yield  # Возвращаем управление тестам

    # Удаление созданных файлов после тестов
    if os.path.exists("file.txt"):
        os.remove("file.txt")
    if os.path.exists("copy.txt"):
        os.remove("copy.txt")


def test_copy_same_file(setup_files):
    # Тест: копирование в тот же файл должно ничего не делать
    copy_file("cp file.txt file.txt")
    with open("file.txt", "r") as f:
        assert f.read() == "Test content"


def test_copy_new_file(setup_files):
    # Тест: копирование в новый файл
    copy_file("cp file.txt copy.txt")
    assert os.path.exists("copy.txt")
    with open("copy.txt", "r") as f1, open("file.txt", "r") as f2:
        assert f1.read() == f2.read()


def test_file_not_found():
    # Тест: ошибка, если исходный файл отсутствует
    with pytest.raises(FileNotFoundError):
        copy_file("cp missing.txt copy.txt")


def test_invalid_command():
    # Тест: ошибка, если неверный формат команды
    with pytest.raises(ValueError):
        copy_file("invalid_command")
from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date

mock_context_no_file = {
    "base_path": "/home/trybe/????"
}


def test_show_details(capsys, tmp_path):
    file = tmp_path / "durandal.py"
    file.touch()
    mock_context = {
        "base_path": str(file)
    }
    show_details(mock_context)
    captured = capsys.readouterr()
    time = date.today()
    assert captured.out == f"File name: durandal.py\n\
File size in bytes: 0\nFile type: file\nFile extension: .py\n\
Last modified date: {time}\n"


def test_show_details_no_extension(capsys, tmp_path):
    file = tmp_path / "durandal"
    file.touch()
    mock_context_no_extension = {
        "base_path": str(file)
    }
    show_details(mock_context_no_extension)
    captured = capsys.readouterr()
    time = date.today()
    assert captured.out == f"File name: durandal\n\
File size in bytes: 0\nFile type: file\nFile extension: [no extension]\n\
Last modified date: {time}\n"


def test_show_details_no_file(capsys):
    show_details(mock_context_no_file)
    captured = capsys.readouterr()
    assert captured.out == "File '????' does not exist\n"

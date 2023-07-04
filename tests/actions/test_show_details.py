from pro_filer.actions.main_actions import show_details  # NOQA

mock_context = {
    "base_path": "pro_filer/actions/alpha_actions.py"
}

mock_context_no_file = {
    "base_path": "/home/trybe/????"
}


def test_show_details(capsys):
    show_details(mock_context)
    captured = capsys.readouterr()
    assert captured.out == "File name: alpha_actions.py\n\
File size in bytes: 2346\nFile type: file\nFile extension: .py\n\
Last modified date: 2023-07-04\n"


def test_show_details_no_file(capsys):
    show_details(mock_context_no_file)
    captured = capsys.readouterr()
    assert captured.out == "File '????' does not exist\n"

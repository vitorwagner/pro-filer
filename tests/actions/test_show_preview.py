from pro_filer.actions.main_actions import show_preview  # NOQA

mock_context = {
    "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
    "all_dirs": ["src", "src/utils"]
}

mock_empty_context = {
    "all_files": [],
    "all_dirs": []
}


def test_show_preview(capsys):
    show_preview(mock_context)
    captured = capsys.readouterr()
    assert captured.out == "Found 3 files and 2 directories\n\
First 5 files: ['src/__init__.py', 'src/app.py', \
'src/utils/__init__.py']\n\
First 5 directories: ['src', 'src/utils']\n"


def test_show_preview_empty(capsys):
    show_preview(mock_empty_context)
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"

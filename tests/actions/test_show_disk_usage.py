from pro_filer.actions.main_actions import show_disk_usage  # NOQA

mock_context = {
        "all_files": ["pro_filer/actions/alpha_actions.py"]
}

mock_context_no_files = {
        "all_files": []
}


def test_show_disk_usage(capsys):
    show_disk_usage(mock_context)
    captured = capsys.readouterr()
    assert captured.out == "'pro_filer/actions/alpha_actions.py':\
                                  \
2346 (100%)\nTotal size: 2346\n"


def test_show_disk_usage_no_files(capsys):
    show_disk_usage(mock_context_no_files)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"

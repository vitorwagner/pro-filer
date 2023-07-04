from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from pro_filer.cli_helpers import _get_printable_file_path  # NOQA


mock_context_no_files = {
        "all_files": []
}


def test_show_disk_usage(capsys, tmp_path):
    file = tmp_path / "durandal.py"
    file.touch()
    file.write_text("test")
    path = str(file)

    empty_file = tmp_path / "empty.py"
    empty_file.touch()
    path_empty = str(empty_file)

    mock_context = {
        "all_files": [path, path_empty],
    }

    show_disk_usage(mock_context)
    captured = capsys.readouterr()
    output_path = f"'{_get_printable_file_path(path)}':".ljust(70)
    empty_output_path = f"'{_get_printable_file_path(path_empty)}':".ljust(70)
    assert captured.out == f"{output_path} 4 (100%)\n\
{empty_output_path} 0 (0%)\nTotal size: 4\n"


def test_show_disk_usage_no_files(capsys):
    show_disk_usage(mock_context_no_files)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"

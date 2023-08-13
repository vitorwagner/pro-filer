from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_files(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.touch()
    file1.write_text("file1")

    file2 = tmp_path / "file2.txt"
    file2.touch()
    file2.write_text("file2")

    file1_duplicate = tmp_path / "file3.txt"
    file1_duplicate.touch()
    file1_duplicate.write_text("file1")

    context = {
        "all_files": [str(file1), str(file2), str(file1_duplicate)],
    }

    expected = [(str(file1), str(file1_duplicate))]
    actual = find_duplicate_files(context)

    assert expected == actual


def test_find_duplicate_files_no_duplicates(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.touch()
    file1.write_text("file1")

    file2 = tmp_path / "file2.txt"
    file2.touch()
    file2.write_text("file2")

    context = {
        "all_files": [str(file1), str(file2)],
    }

    expected = list()
    actual = find_duplicate_files(context)

    assert expected == actual


def test_find_duplicate_files_no_files(tmp_path):
    context = {
        "all_files": [
            "file1.txt",
            "file2.txt",
        ],
    }

    with pytest.raises(ValueError):
        find_duplicate_files(context)

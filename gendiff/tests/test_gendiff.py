"""Test gendiff module."""

from gendiff.scripts import gendiff

CONTENT = 'something content'


def test_is_file(tmpdir):
    """
    Test for checking file in path.

    Parameters:
        tmpdir: temporary /path/to/file
    """
    # TODO: will fix S101 before production
    file_with_extension = tmpdir.join('file.json')
    file_with_extension.write(CONTENT)
    file_without_extension = tmpdir.join('file')
    file_without_extension.write(CONTENT)
    # real path/file with extension
    assert gendiff.is_file(  # noqa: S101
        str(file_with_extension),
    ) is True
    # real path/file without extension
    assert gendiff.is_file(  # noqa: S101
        str(file_without_extension),
    ) is True
    # real path but file not exist
    assert gendiff.is_file(  # noqa: S101
        str(tmpdir.join('file2.json')),
    ) is False
    # empty path
    assert gendiff.is_file(  # noqa: S101
        str(tmpdir.join('')),
    ) is False
    # assert 0


def test_check_extension(tmpdir):
    """
    Test for checking extension file.

    Parameters:
        tmpdir: temporary /path/to/file
    """
    # TODO: will fix S101 before production
    json_file = tmpdir.join('file.json')
    json_file.write(CONTENT)
    yaml_file = tmpdir.join('file.yaml')
    yaml_file.write(CONTENT)
    # check json ext
    assert gendiff.check_extension(str(json_file)) == 'json'  # noqa: S101
    # check yaml ext
    assert gendiff.check_extension(str(yaml_file)) == 'yaml'  # noqa: S101
    # check empty path
    assert gendiff.check_extension('') is None  # noqa: S101


def test_data_reception(tmpdir):
    """
    Test for checking structure.

    Parameters:
        tmpdir: temporary /path/to/file
    """
    # TODO: will fix WPS421 before production
    json_load = './gendiff/tests/fixtures/load.json'
    json_expected = {
        'verbose': True,
        'host': 'hexlet.io',
        'smtp': 25,
        'starttls': True,
        'timeout': 20,
    }
    try:
        with open(json_load, 'r') as json_read:
            json_file = tmpdir.join('file.json')
            json_file.write(json_read.readline())
    except TypeError:
        print('File {0} is not json'.format(tmpdir))  # noqa: WPS421
    assert gendiff.data_reception(json_load) == json_expected  # noqa: S101

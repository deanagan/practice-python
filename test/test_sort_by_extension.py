import pytest
from src.sort_by_extension import sort_by_ext


@pytest.mark.parametrize(('filenames, expected'), [
    (['1.cad', '1.bat', '1.aa'],  ['1.aa', '1.bat', '1.cad']),
    (['1.cad', '1.bat', '1.aa', '2.bat'],  ['1.aa', '1.bat', '2.bat', '1.cad']),
    (['1.cad', '1.bat', '1.aa', '.bat'],  ['.bat', '1.aa', '1.bat', '1.cad']),
    (['1.cad', '1.bat', '.aa', '.bat'],  ['.aa', '.bat', '1.bat', '1.cad']),
    (['1.cad', '1.', '1.aa'],  ['1.', '1.aa', '1.cad']),
    (['1.cad', '1.bat', '1.aa', '1.aa.doc'],  ['1.aa', '1.bat', '1.cad', '1.aa.doc']),
    (['1.cad', '1.bat', '1.aa', '.aa.doc'],  ['1.aa', '1.bat', '1.cad', '.aa.doc']),
    ([".config","my.doc","1.exe","345.bin","green.bat","format.c","no.name.","best.test.exe"], [".config","no.name.","green.bat","345.bin","format.c","my.doc","1.exe","best.test.exe"])

])
def test_sort_by_extension(filenames, expected):
    assert sort_by_ext(filenames) == expected

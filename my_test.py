from functions_2 import *
def test_function():
    assert isinstance(decoder(prepare_text(remove_punctuation('33'))), list)
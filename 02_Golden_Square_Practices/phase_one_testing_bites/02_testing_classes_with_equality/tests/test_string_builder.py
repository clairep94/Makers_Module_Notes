from lib.string_builder import StringBuilder

def test_string_size():
    builder = StringBuilder()
    builder.add("test string")
    assert builder.size() == 11
    assert builder.output() == "test string"
    builder.add("extra")
    assert builder.size() == 16
    assert builder.output() == "test stringextra"

def test_adding():
    builder = StringBuilder()
    builder.add("Initial string")
    builder.add(" another test")
    assert builder.size() == 27
    assert builder.output() == "Initial string another test"

from streamxml2json import stream_xml2json

# The example XML used is derived from https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms762271(v=vs.85)
def test_matches_to_expected():
    with open("./tests/data/books.xml", "rb") as xml_file:
        stream_xml2json(xml_file, "./tests/data/generated_books.json", 2)

    generated = None
    with open("./tests/data/generated_books.json", "r") as generated_file:
        generated = generated_file.readlines()

    expected = None
    with open("./tests/data/expected_books.json", "r") as expected_file:
        expected = expected_file.readlines()

    assert generated == expected

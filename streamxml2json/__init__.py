import jsonstreams
import xmltodict
from tqdm import tqdm


def stream_xml2json(
    xml_input,
    json_output_filename,
    item_depth,
    pretty=True,
    indent=2,
    display_progress_bar=True,
    tqdm_kwargs={},
):
    """
    `xml_input` can either be an XML `string` or a file-like object opened in binary mode
    - using `open(file, "rb")` for example.
    If your xml is gzipped, for example, you might pass a GzipFile(filename) instance

    `json_output_filename` must be a `string` with the relative/absolute path
    to where the json should be written to.

    `item_depth` is required because of the streaming nature of the process. You must tell
    at which depth of the XML we want to iterate on to generate the output JSON array.

    By default, we pretty-print the JSON file with `2` spaces. You can disable this pretty-printing
    by setting `pretty` to False, or customize the indentation depth by changing `indent` value.

    We automatically display a progress bar. You can disable it by passing False to `display_progress_bar`.
    We use [`tqdm`](https://github.com/tqdm/tqdm) to display this progress bar. You can pass additional
    customization parameters as a dictionary to `tqdm_kwargs`. Please check their documentation to better
    understand the available options.
    One interesting option is `total`, which will make tqdm be able to show how much longer it expects
    the process to take.
    """

    try:
        if display_progress_bar:
            tqdm_handler = tqdm(desc="XML Parsing", **tqdm_kwargs)

        output_stream = jsonstreams.Stream(
            jsonstreams.Type.ARRAY,
            filename=json_output_filename,
            pretty=pretty,
            indent=indent,
        )

        def handle_entry(_, entry):
            output_stream.write(entry)

            if display_progress_bar:
                tqdm_handler.update()

            return True

        xmltodict.parse(xml_input, item_depth=item_depth, item_callback=handle_entry)
    finally:
        # Always close the open fd-like instances at the end of the execution
        output_stream.close()
        tqdm_handler.close()

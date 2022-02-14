# Changelog

## v1.0.0

Initial release of the library

The library can be used like so:

```python
import stream_xml2json from streamxml2json

with open("input.xml", "rb") as input_file:
   stream_xml2json(input_file, "output.json", 2)
```

`xml_input` can either be an XML `string` or a file-like object opened in binary mode - using `open(file, "rb")` for example. If your xml is gzipped, for example, you might pass a `GzipFile(filename)` instance

`json_output_filename` must be a `string` with the relative/absolute path to where the json should be written to.

`item_depth` is required because of the streaming nature of the process. You must tell at which depth of the XML we want to iterate on to generate the output JSON array.

By default, we pretty-print the JSON file with `2` spaces. You can disable this pretty-printing by setting `pretty` to False, or customize the indentation depth by changing `indent` value.

We automatically display a progress bar. You can disable it by passing False to `display_progress_bar`. We use [`tqdm`](https://github.com/tqdm/tqdm) to display this progress bar. You can pass additional customization parameters as a dictionary to `tqdm_kwargs`. One interesting option is `total`, which will make tqdm be able to show how much longer it expects the process to take. Please check their documentation to better understand the available options.

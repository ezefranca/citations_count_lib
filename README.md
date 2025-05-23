# citations_count_lib ![PyPI - Version](https://img.shields.io/pypi/v/citations-count) [![DOI](https://zenodo.org/badge/954234210.svg)](https://doi.org/10.5281/zenodo.15079437)

## Overview
`citations-count` is a Python library designed to fetch citation counts for academic publications from multiple sources, including [CrossRef](https://www.crossref.org), [OpenCitations](https://opencitations.net), and [Google Scholar](https://scholar.google.com). 

This library provides a unified interface to retrieve citation counts using DOIs (Digital Object Identifiers).

Check the [example on Google Colab](https://colab.research.google.com/drive/17T7tj6Dd5WN4pjOrX-lls0WWfV9f_vNd?usp=sharing).

## Features
- Fetch citation counts from CrossRef, OpenCitations, and Google Scholar.
- Support for verbose logging to aid in debugging.
- Handles rate limiting by introducing delays between API calls.

## Installation
To install the library, clone the repository and install the dependencies:

```bash
git clone https://github.com/ezefranca/citations_count_lib.git
cd citations_count_lib
pip install -r requirements.txt
```

## Usage

```python
from citations_count.core import fetch_multiple_citations

dois = [
    "10.1109/SeGAH.2017.7939283",
    "10.1109/SeGAH.2011.6165447",
    "10.3390/info16030246",
    "10.1038/s41586-020-2649-2"
]
results = fetch_multiple_citations(dois, delay=1.0, verbose=True)
for result in results:
    print(result)
```

### Example output:

```json
[
    {
        "doi": "10.1109/SeGAH.2017.7939283",
        "citations_crossref": 62,
        "citations_opencitations": 64,
        "citations_google_scholar": 160
    },
    {
        "doi": "10.1109/SeGAH.2011.6165447",
        "citations_crossref": 48,
        "citations_opencitations": 48,
        "citations_google_scholar": 116
    },
    {
        "doi": "10.3390/info16030246",
        "citations_crossref": 0,
        "citations_opencitations": 0,
        "citations_google_scholar": 0
    },
    {
        "doi": "10.1038/s41586-020-2649-2",
        "citations_crossref": 14710,
        "citations_opencitations": None,
        "citations_google_scholar": 22393
    }
]
```

## Logging
Verbose logging can be enabled by setting the verbose parameter to `True`. This will print detailed logs for debugging purposes.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Citation

```bibtex
@software{Santos_citations_count_is_a_2025,
	title        = {{citations\_count is a Python library designed to fetch citation counts for academic publications from multiple sources, including CrossRef, OpenCitations, and Google Scholar.}},
	author       = {Santos, Ezequiel},
	year         = 2025,
	month        = {mar},
	doi          = {10.5281/zenodo.15079456},
	url          = {https://github.com/ezefranca/citations_count_lib},
	license      = {MIT},
	version      = {1.0.0}
}
```


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

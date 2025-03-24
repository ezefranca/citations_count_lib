import requests
from urllib.parse import quote
from citations_count.config import DEFAULT_HEADERS
from citations_count.logging_utils import log_message

def get_citation_count_opencitations(doi: str, verbose: bool = False) -> int | None:
    """
    Fetch citation count from OpenCitations COCI API for a given DOI.

    Parameters:
    doi (str): The DOI (Digital Object Identifier) of the publication.
    verbose (bool): If True, print detailed logs for debugging.

    Returns:
    int: The number of citations if the request is successful.
    None: If the request fails or the response status code is not 200.
    """
    base_url = "https://opencitations.net/index/coci/api/v1/citations/"
    encoded_doi = quote(doi)
    url = base_url + encoded_doi

    log_message(f"\n🔍 [OpenCitations] Fetching citation count for DOI: {doi}", verbose)
    log_message(f"🌐 URL: {url}", verbose)
    log_message(f"📦 Headers: {DEFAULT_HEADERS}\n", verbose)

    try:
        response = requests.get(url, headers=DEFAULT_HEADERS, timeout=10)
        response.raise_for_status()

        data = response.json()
        count = len(data)

        log_message(f"✅ Status: {response.status_code}", verbose)
        log_message(f"📊 Raw count: {count} ({type(count)})", verbose)
        
        return int(count)

    except requests.exceptions.RequestException as e:
        log_message(f"[OpenCitations Error] DOI {doi}: {e}", verbose)
        return None
import requests
from citations_count.config import DEFAULT_HEADERS
from citations_count.logging_utils import log_message

def get_crossref_citations(doi: str, verbose: bool = False) -> int | None:
    """
    Fetch citation count from CrossRef API for a given DOI.

    Parameters:
    doi (str): The DOI (Digital Object Identifier) of the publication.
    verbose (bool): If True, print detailed logs for debugging.

    Returns:
    int: The number of citations if the request is successful.
    None: If the request fails or the response status code is not 200.
    """
    url = f"https://api.crossref.org/works/{doi}"

    log_message(f"\n🔍 [CrossRef] Fetching citation count for DOI: {doi}", verbose)
    log_message(f"🌐 URL: {url}", verbose)

    try:
        response = requests.get(url, headers=DEFAULT_HEADERS, timeout=10)
        response.raise_for_status()

        log_message(f"✅ Status: {response.status_code}", verbose)
        log_message(f"📊 Response JSON: {response.json()}", verbose)

        return response.json()["message"].get("is-referenced-by-count", 0)
    except requests.RequestException as e:
        log_message(f"[CrossRef Error] DOI {doi}: {e}", verbose)
        return None
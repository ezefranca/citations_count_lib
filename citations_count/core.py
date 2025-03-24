import time
from .sources.crossref import get_crossref_citations
from .sources.opencitations import get_citation_count_opencitations
from .sources.googlescholar import get_google_scholar_count
from citations_count.logging_utils import log_message

def fetch_citations(doi: str, delay: float = 1.0, verbose: bool = False) -> dict:
    """
    Fetch citation counts from multiple sources for a given DOI.

    Parameters:
    doi (str): The DOI (Digital Object Identifier) of the publication.
    delay (float): Delay in seconds between API calls to avoid rate limiting.
    verbose (bool): If True, print detailed logs for debugging.

    Returns:
    dict: A dictionary containing the DOI and citation counts from various sources.
    """
    log_message(f"\n🔍 Fetching citations for DOI: {doi}", verbose)

    result = {
        "doi": doi,
        "citations_crossref": get_crossref_citations(doi, verbose),
        "citations_opencitations": get_citation_count_opencitations(doi, verbose),
        "citations_google_scholar": get_google_scholar_count(doi, verbose)
    }

    time.sleep(delay)

    log_message(f"✅ Citation results for DOI {doi}: {result}", verbose)

    return result

def fetch_multiple_citations(dois: list, delay: float = 1.0, verbose: bool = False) -> list:
    """
    Fetch citation counts from multiple sources for a list of DOIs.

    Parameters:
    dois (list): A list of DOIs (Digital Object Identifiers) of the publications.
    delay (float): Delay in seconds between API calls to avoid rate limiting.
    verbose (bool): If True, print detailed logs for debugging.

    Returns:
    list: A list of dictionaries, each containing a DOI and citation counts from various sources.
    """
    results = []

    for doi in dois:
        log_message(f"\n🔍 Processing DOI: {doi}", verbose)
        result = fetch_citations(doi, delay, verbose)
        results.append(result)
        time.sleep(delay)

    log_message(f"✅ All citation results: {results}", verbose)

    return results
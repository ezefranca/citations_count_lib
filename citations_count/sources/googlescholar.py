import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import quote
from citations_count.config import DEFAULT_HEADERS
from citations_count.logging_utils import log_message

def get_google_scholar_count(doi: str, verbose: bool = False) -> int | None:
    """
    Search Google Scholar using a DOI and parse the 'Cited by' count from the HTML.

    Parameters:
    doi (str): The DOI (Digital Object Identifier) of the publication.
    verbose (bool): If True, print detailed logs for debugging.

    Returns:
    int: The number of citations if the request is successful.
    None: If the request fails or the response status code is not 200.
    """
    try:
        query = quote(doi)
        url = f"https://scholar.google.com/scholar?q={query}&hl=en"

        log_message(f"\n🔍 [Google Scholar] Searching for DOI: {doi}", verbose)
        log_message(f"🌐 URL: {url}", verbose)
        log_message(f"📦 Headers: {DEFAULT_HEADERS}\n", verbose)

        response = requests.get(url, headers=DEFAULT_HEADERS, timeout=10)

        log_message(f"✅ Status: {response.status_code}", verbose)
        if response.status_code != 200:
            log_message("❌ Response content:", verbose)
            log_message(response.text[:1000], verbose)  # Print first 1000 chars to inspect block messages

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        cited_by = 0

        for a_tag in soup.find_all("a", href=True):
            if "Cited by" in a_tag.text:
                log_message(f"🔗 Found citation link: {a_tag.text}", verbose)
                match = re.search(r"Cited by (\d+)", a_tag.text)
                if match:
                    cited_by = int(match.group(1))
                    break

        log_message(f"📊 Citation count: {cited_by}", verbose)

        return cited_by or 0

    except Exception as e:
        log_message(f"[Google Scholar Error] DOI {doi}: {e}", verbose)
        return None
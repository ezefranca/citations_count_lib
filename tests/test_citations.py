import unittest
from citations_count.core import fetch_multiple_citations
import sys
import requests

class TestCitationFetching(unittest.TestCase):
    def setUp(self):
        self.test_dois = [
            "10.1109/SeGAH.2017.7939283",
            "10.1109/SeGAH.2011.6165447",
            "10.3390/info16030246",
            "10.1038/s41586-020-2649-2"
        ]
        self.delay = 0.1

    def test_environment(self):
        print(f"🐍 Python version: {sys.version}")
        print(f"📦 requests version: {requests.__version__}")

    def test_fetch_multiple_citations(self):
        results = fetch_multiple_citations(self.test_dois, delay=self.delay, verbose=True)
        for result in results:
            print(result)
            self.assertIn("doi", result)
            self.assertIn("citations_crossref", result)
            self.assertIn("citations_opencitations", result)
            self.assertIn("citations_google_scholar", result)
            self.assertIsInstance(result["citations_crossref"], (int, type(None)))
            self.assertIsInstance(result["citations_opencitations"], (int, type(None)))
            self.assertIsInstance(result["citations_google_scholar"], (int, type(None)))

if __name__ == "__main__":
    unittest.main()
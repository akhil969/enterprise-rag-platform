from pypdf import PdfReader
from typing import List, Tuple


def extract_text_by_page(file_path: str) -> List[Tuple[int, str]]:
    """
    Returns a list of (page_number, page_text) tuples.
    Page numbers start at 1, matching what a human would cite.
    """
    reader = PdfReader(file_path)
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if text.strip():
            pages.append((i, text))
    return pages
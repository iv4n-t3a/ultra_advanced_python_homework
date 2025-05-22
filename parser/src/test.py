import pytest
from unittest.mock import patch, MagicMock
from main import WebScraper, WebScraperError


def test_webscraper_initialization():
    url = "https://example.com"
    scraper = WebScraper(url)
    assert scraper.url == url
    assert scraper._headers == WebScraper.DEFAULT_HEADERS
    assert scraper._html_content is None
    assert scraper._company_data == []
    assert not scraper._has_data


def test_print_data_no_data():
    scraper = WebScraper("https://example.com")
    with pytest.raises(WebScraperError):
        scraper.print_data()


def test_get_data_no_data():
    scraper = WebScraper("https://example.com")
    with pytest.raises(WebScraperError):
        scraper.get_data()


@patch("main.requests.get")
def test_fetch_html_success(mock_get):
    mock_response = MagicMock()
    mock_response.text = "<html></html>"
    mock_get.return_value = mock_response

    scraper = WebScraper("https://example.com")
    scraper._fetch_html()
    assert scraper._html_content == "<html></html>"


@patch("main.requests.get")
def test_fetch_html_failure(mock_get):
    mock_get.side_effect = Exception("Request failed")
    scraper = WebScraper("https://example.com")
    with pytest.raises(WebScraperError):
        scraper._fetch_html()


def test_parse_html_no_content():
    scraper = WebScraper("https://example.com")
    with pytest.raises(WebScraperError):
        scraper._parse_html()


@patch("main.requests.get")
def test_extract_company_data(mock_get):
    html_content = """
    <div class="company-index" data-hour="12" data-day="Monday">
        <h5>Company A</h5>
        <a href="https://example.com/company-a">Link</a>
    </div>
    <div class="company-index" data-hour="14" data-day="Tuesday">
        <h5>Company B</h5>
        <a href="https://example.com/company-b">Link</a>
    </div>
    """
    mock_response = MagicMock()
    mock_response.text = html_content
    mock_get.return_value = mock_response

    scraper = WebScraper("https://example.com")
    scraper._fetch_html()
    soup = scraper._parse_html()
    scraper._extract_company_data(soup)

    assert len(scraper._company_data) == 2
    assert scraper._company_data[0] == {
        "name": "Company A",
        "link": "https://example.com/company-a",
        "data_hour": "12",
        "data_day": "Monday",
    }
    assert scraper._company_data[1] == {
        "name": "Company B",
        "link": "https://example.com/company-b",
        "data_hour": "14",
        "data_day": "Tuesday",
    }


@patch("main.requests.get")
def test_parse_integration(mock_get):
    html_content = """
    <div class="company-index" data-hour="12" data-day="Monday">
        <h5>Company A</h5>
        <a href="https://example.com/company-a">Link</a>
    </div>
    """
    mock_response = MagicMock()
    mock_response.text = html_content
    mock_get.return_value = mock_response

    scraper = WebScraper("https://example.com")
    scraper.parse()

    assert scraper._has_data
    assert len(scraper._company_data) == 1
    assert scraper._company_data[0] == {
        "name": "Company A",
        "link": "https://example.com/company-a",
        "data_hour": "12",
        "data_day": "Monday",
    }

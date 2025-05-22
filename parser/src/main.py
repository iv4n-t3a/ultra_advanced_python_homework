import requests
from bs4 import BeautifulSoup
import sys


class WebScraperError(Exception):
    pass


class WebScraper:
    DEFAULT_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    def __init__(self, url, headers=DEFAULT_HEADERS):
        self.url = url
        self._headers = headers
        self._html_content = None
        self._company_data = []
        self._has_data = False

    def print_data(self):
        if not self._has_data:
            raise WebScraperError("No data, run parse() first")

        for company in self._company_data:
            print(f"Name: {company['name']}, Link: {company['link']}, "
                  f"Data Hour: {company['data_hour']}, Data Day: {company['data_day']}")

    def get_data(self):
        if not self._has_data:
            raise WebScraperError("No data, run parse() first")

        return self._company_data

    def parse(self):
        self._fetch_html()
        soup = self._parse_html()
        self._extract_company_data(soup)
        self._has_data = True

    def _fetch_html(self):
        try:
            response = requests.get(self.url, headers=self._headers)
            response.raise_for_status()
            self._html_content = response.text
        except requests.exceptions.RequestException as e:
            raise WebScraperError(f"Failed to fetch HTML content: {e}")
        except:
            raise WebScraperError(f"Unknown requests error")

    def _parse_html(self):
        if not self._html_content:
            raise WebScraperError("No HTML content to parse.")

        return BeautifulSoup(self._html_content, 'html.parser')

    def _extract_company_data(self, soup):
        company_cards = soup.find_all('div', class_='company-index')
        for card in company_cards:
            name_tag = card.find('h5')
            name = name_tag.text.strip() if name_tag else None

            link_tag = card.find('a', href=True)
            link = link_tag['href'] if link_tag else None

            data_hour = card.get('data-hour')
            data_day = card.get('data-day')

            if name and link:
                self._company_data.append({
                    'name': name,
                    'link': link,
                    'data_hour': data_hour,
                    'data_day': data_day
                })

def main():
    url = "https://downdetector.co.uk"
    scraper = WebScraper(url)
    try:
        scraper.parse()
        scraper.print_data()
    except WebScraperError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

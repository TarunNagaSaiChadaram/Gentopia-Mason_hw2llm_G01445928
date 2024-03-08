### Define your custom tool here. Check prebuilts in gentopia.tool (:###
from typing import AnyStr
from Gentopia.gentopia.tools.basetool import BaseTool
import requests
from bs4 import BeautifulSoup
class WebScraper(BaseTool):
    """Tool for web scraping."""

    name = "web_scraper"
    description = "A tool for extracting data from websites using web scraping techniques."

    def _run(self, url: AnyStr) -> str:
        try:
            # Send a GET request to the specified URL
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the HTML content of the page
                soup = BeautifulSoup(response.content, 'html.parser')

                # Extract specific elements from the page
                # For example, find all <a> tags with class="link"
                links = soup.find_all('a', class_='link')

                # Return the text content of the extracted links
                return '\n'.join(link.text for link in links)
            else:
                return f"Failed to retrieve content from {url}. Status code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            # Handle request errors
            return f"Error accessing {url}: {e}"
        except Exception as e:
            # Handle other exceptions
            return f"Error occurred: {e}"
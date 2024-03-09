### Define your custom tool here. Check prebuilts in gentopia.tool (:###
from Gentopia.gentopia.tools import *
from googlesearch import search
from Gentopia.gentopia.tools.basetool import *
import PyPDF2
from pydantic import BaseModel, Field
from typing import AnyStr, Optional, Type

class GoogleSearchArgs(BaseModel):
    query: str = Field(..., description="a search query")


class GoogleSearch(BaseTool):
    """Tool that adds the capability to query the Google search API."""

    name = "google_search"
    description = ("A search engine retrieving top search results as snippets from Google."
                   "Input should be a search query.")

    args_schema: Optional[Type[BaseModel]] = GoogleSearchArgs

    def _run(self, query: AnyStr) -> str:
        return '\n\n'.join([str(item) for item in search(query, advanced=True)])

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

class PDFReadingArgs(BaseModel):
    file_path: str = Field(..., description="Path to the PDF file to be read")


class PDFReading(BaseTool):
    """Tool that reads text content from a PDF file."""

    name = "pdf_reading"
    description = "A tool for extracting text content from a PDF file."

    args_schema: Optional[Type[BaseModel]] = PDFReadingArgs

    def _run(self, file_path: AnyStr) -> str:
        try:
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                text = ""
                for page_num in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_num)
                    text += page.extractText()
                return text
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

if __name__ == "__main__":
    ans = GoogleSearch()._run("Attention for transformer")
    print(ans)

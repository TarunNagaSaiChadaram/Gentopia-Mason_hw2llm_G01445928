import os
from typing import AnyStr

import PyPDF2
from gentopia.tools.basetool import *


class CustomPDFReaderTool:
    def __init__(self):
        pass

    def run(self, file_path: str) -> str:
        """Read text content from a PDF file."""
        try:
            with open(file_path, 'rb') as pdf_file:
                p_r = PyPDF2.PdfReader(pdf_file)
                txt = ""
                for p_n in range(len(p_r.pages)):
                    page = p_r.pages[p_n]
                    txt += page.extract_text()
                return txt
        except FileNotFoundError:
            return "File doesnt exist"
        except Exception as e:
            return f"Aerror: {str(e)}"


class PDFReadingArgs(BaseModel):
    file_path: str = Field(..., description="Path to the PDF file to be read.")


class PDFReading(BaseTool):
    name = "pdf_reading"
    description = "A tool for extracting text content from a PDF file."
    args_schema: Optional[Type[BaseModel]] = PDFReadingArgs

    def _run(self, file_path: AnyStr) -> AnyStr:
        tool = CustomPDFReaderTool()
        text_content = tool.run(file_path)
        return text_content

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    pdf_text = PDFReading()._run("samplefile.pdf")
    print(pdf_text)

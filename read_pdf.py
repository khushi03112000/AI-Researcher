# How to read PDF available on Web
from langchain_core.tools import tool
import io
import PyPDF2
import requests

@tool
def read_pdf(url: str) -> str:
 
#Step1 : Access PDF provided by URL from arxiv_too.py file
#url = "https://arxiv.org/pdf/2601.14257v1" #hardcording the url for testing

#Doctring for the tool
 """Read and extract text from a PDF file given its URL.

    Args:
        url: The URL of the PDF file to read

    Returns:
        The extracted text content from the PDF
    """
 try:
    # response = requests.get(url)

    response = requests.get(
            url,
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0"}
        )
    response.raise_for_status()
    #print(respone.content)                      #returns huge bytes of data

    #Step2 : Convert the PDF available on Web to Bytes and then Parse it
    pdf_file = io.BytesIO(response.content)          #convert the huge bytes into readable form
    # print(pdf_file)

    #Step3 : Retrieve only Text from PDF data among the metadata,images etc  

    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    #Extract text from pages is giving error as tool should never return full PDFs.

#     text =""
#     for i, page in enumerate(pdf_reader.pages,1):
#         print(f"Extracting text from page{i}/{num_pages}")
#         text += page.extract_text() + "\n"

#     print(f"Successfully extracted {len(text)} characters of text from PDF")
#     return text.strip()
#  except Exception as e:
#   print(f"Error Reading pdf: {str(e)} ")
#   raise

    # Step 3: Extract LIMITED text (first few pages only)
    extracted_text = ""
    max_pages = min(3, len(pdf_reader.pages))  # 🔥 LIMIT PAGES

    for i in range(max_pages):
        page_text = pdf_reader.pages[i].extract_text()
        if page_text:
            extracted_text += page_text + "\n"

    # Step 4: HARD LIMIT output size (CRITICAL)
    extracted_text = extracted_text.strip()
    extracted_text = extracted_text[:3000]  # 🔥 TOKEN SAFETY
    return extracted_text

 except Exception as e:
    return f"Error reading PDF: {str(e)}"

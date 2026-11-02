from langchain_community.document_loaders import pyPDFLoader

loader = pyPDFLoader("path/to/your/pdffile.pdf")
docs = loader.load()
print(docs)

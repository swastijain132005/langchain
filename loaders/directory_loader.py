from langchain_community.document_loaders import pyPDFLoader,DirectoryLoader


loader=DirectoryLoader("path/to/your/directory", glob="**/*.pdf", loader_cls=pyPDFLoader)

docs=loader.lazy_load()
print(docs)

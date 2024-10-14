from loaders.pdf_loader import PDFLoader
from loaders.ppt_loader import PPTLoader
from loaders.docs_loader import DOCXLoader
from extractor.data_extractor import DataExtractor
from storage.file_storage import FileStorage
from storage.sql_storage import SQLStorage

if __name__ == "__main__":
    # Example usage with a PDF file
    file_loader = PDFLoader('/home/shtlp_0128/Desktop/harshtest/Assignment_4/test.pdf')
 
    extractor = DataExtractor(file_loader)

    # File storage
    file_storage = FileStorage(extractor)
    file_storage.store()

    # SQL storage
    sql_storage = SQLStorage(extractor)
    sql_storage.store()

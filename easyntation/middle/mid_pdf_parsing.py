from easyntation.back.src.pdf_parsing import parse_annotation
import eel

@eel.expose
def parse_annotation_py(doc_name: str, annot_page_number: int):
    return parse_annotation(doc_name, annot_page_number)
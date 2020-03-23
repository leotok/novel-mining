import ebooklib
from ebooklib import epub
from ebooklib.utils import debug


if __name__ == "__main__":
        
    book = epub.read_epub('data/one_hundred_years_of_solitude_EN.epub')

    title, _ = book.get_metadata('DC', 'title')[0]
    print (title)

    for i, item in enumerate(book.get_items_of_type(ebooklib.ITEM_DOCUMENT)):
        content = item.get_content()

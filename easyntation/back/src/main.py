import eel
from easyntation.middle.mid_pdf_parsing import *

if __name__ == '__main__':
    eel.init('front')
    eel.start('index.html', mode="chrome", size=(760, 760))
import fitz
from PyPDF2 import PdfReader
import os
import fitz
import io
from PIL import Image
import tabula
from tabulate import tabulate
import pandas as pd
import pdftotree
import os
import re
from nltk.tokenize import word_tokenize

# doc_name = 'C:/Users/compf/Documents/Diploma/data/НИР_ВласенкоНА.pdf'

def parse_annotation(doc_name: str, annot_page_number: int):
  doc = fitz.open(doc_name)
  page = doc.load_page(annot_page_number)
  links = page.get_links()
  textboxes = []

  for i in range(len(links)):
    page_num = links[i]['page']
    rect = links[i]['from']
    textboxes.append({'text': page.get_textbox(rect), 'page': page_num})
  return textboxes

def search_text(doc_name: str, text: str, page_number: int):
  doc = fitz.open(doc_name)
  page = doc.load_page(page_number)
  areas = page.searchFor(text, hit_max=16)
  return areas

def parse_images(doc_name: str, image_page_number: int):
  doc = fitz.open(doc_name)
  page = doc.load_page(image_page_number+4)
  pix = page.get_pixmap()
  print(pix)
  pix.save("page-%i.png" % page.number)
  large_img = Image.open("page-%i.png" % page.number, mode='r', formats=None)
  image_list = page.get_images(full=True)
  print('img', image_list)
  im_size = (image_list[0][0], image_list[0][1], image_list[0][2], image_list[0][3])
  # print(image_list[0][0])
  print(im_size)
  if image_list:
    print(f"[+] Found a total of {len(image_list)} images in page {image_page_number}")
  else:
    print(f"[!] No images found on page {image_page_number}")
    # Iterate over the images on the page
  for image_index, img in enumerate(image_list, start=1):
    # Get the XREF of the image
    xref = img[0]
    # Extract the image bytes
    base_image = doc.extract_image(xref)
    image_bytes = base_image["image"]
    # Get the image extension
    image_ext = base_image["ext"]
    # Load it to PIL
    image = Image.open(io.BytesIO(image_bytes))
    # Check if the image meets the minimum dimensions and save it
    output_dir = "C:/Users/compf/PycharmProjects/Easyntation/data/extracted_images"
    image.save(
      open(os.path.join(output_dir, f"image{image_page_number + 1}_{image_index}.{'png'}"), "wb"),
      format='png'.upper())
  return image

def parse_text(doc_name: str, file_name: str, text_page_number: int = None):
  doc = fitz.open(doc_name)
  file1 = open("%s.txt" % doc_name, "a")
  print(doc.page_count)
  count = 0
  arr_of_tokenized_sent = []
  c=0
  if text_page_number == None:
    for p in range(4, doc.page_count):

      page = doc.load_page(p)
      text = page.get_text().replace('\n', '')
      # print(text)
      # print(text[0:8])
      # arr_sent_tokenize = word_tokenize(text)
      # n = []
      # print(text[0:20])
      # if 'ВВЕДЕНИЕ' not in text[0:20] and count==0:
      #   continue
      # else:
      #   count=1
      # for idx_sent in range(len(arr_sent_tokenize)):
      #   match = re.search(r'[А-Я]{7,}', arr_sent_tokenize[idx_sent])
      #   if match:
      #     n.append(idx_sent)
      #     c+=1
      #   print(match[0] if match else '')
      #
      # if len(n)>0:
      #   arr_of_tokenized_sent.append(arr_sent_tokenize[n[0]:])
      # else:
      #   # print(arr_sent_tokenize)
      #   arr_of_tokenized_sent[len(arr_of_tokenized_sent) - 1]+=arr_sent_tokenize
      #   # arr_of_tokenized_sent[len(arr_of_tokenized_sent)-1].append(arr_sent_tokenize[0].split())

      with open("%s_1.txt" % doc_name, "a", encoding="utf-8") as logg:
        # for aa in arr_of_tokenized_sent:
        #   for a in aa:
          logg.write(text)

          logg.write("\n\n")
      #  logg.close()
  else:
    page = doc.load_page(text_page_number)
    text = page.get_text()
    return text

def parse_table(doc_name: str, table_page_number: int):

  # # reads the table from pdf file

  df = tabula.read_pdf(doc_name, pages=table_page_number)  # address of pdf file
  # print(df)
  # doc = fitz.open(doc_name)
  # page = doc.load_page(table_page_number)
  # page = pdftotree.parse(doc_name, html_path=None, model_type=None, model_path=None, visualize=True)
  #
  # html_tables = pd.read_html(page)

  return df

if __name__ == '__main__':
  # print(parse_annotation(doc_name, 1))
  # print(parse_images(doc_name, 10))
  # print(parse_text(doc_name, 10))
  rootdir = 'C:/Users/compf/Documents/Diploma/data/2023/bachelor/'
  for subdir, dirs, files in os.walk(rootdir):
    print(dirs)
    #                         print(f.read())
    #                     except:
    #                         print(f.decode())
    directory = os.fsencode(subdir)
    for dir in dirs:
      for subdirr, dirss, filess in os.walk(rootdir+dir):
        for file in filess:
          filename = os.fsdecode(file)
          if filename.endswith(".pdf"):
            # print(os.path.join(directory, filename))
            # filename = '337796_mag1_28052023014348.pdf'
            parse_text(rootdir+dir+'/'+filename, rootdir+dir)

    # t = parse_table(doc_name, 10)
    # print(t[0].values.tolist())
    # # file path you want to extract images from
    # file = "C:/Users/compf/PycharmProjects/Easyntation/data/extracted_images/image41_1.png"
    # # open the file
    # pdf_file = fitz.open(file)

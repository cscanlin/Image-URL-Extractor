import mechanize
import re
import csv

my_url = "Type the URL you want to use here"

br = mechanize.Browser()
br.open(my_url)
print(br.response().get_data())

images_list = re.findall('"(IMG_.*JPG)"', br.response().get_data())
print(images_list)

images_list = [my_url + i for i in images_list]

with open('Type the file path you want to output to here', 'wb') as csv_to_write:
  writer = csv.writer(csv_to_write)
  writer.writecolumn(images_list)

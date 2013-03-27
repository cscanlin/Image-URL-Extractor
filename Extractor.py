import mechanize
import re
import csv

my_url = "http://cscanlin.com/Part%201%20(112)/10129%20TOTAL%20TEA%20INFUSER/"

br = mechanize.Browser()
br.open(my_url)
print(br.response().get_data())

images_list = re.findall('"(IMG_.*JPG)"', br.response().get_data())
print(images_list)

images_list = [my_url + i for i in images_list]

with open('C:\Users\Chris\My Documents\pic-urls.csv', 'wb') as my_csv:
  writer = csv.writer(my_csv)
  writer.writerow(images_list)

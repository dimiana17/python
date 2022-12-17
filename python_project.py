import requests
from bs4 import BeautifulSoup as bss4
import csv
from itertools import zip_longest
Description = []
Review=[]
Price = []
Links =[]
url = requests.get("https://www.amazon.eg/s?i=electronics&bbn=21832883031&rh=n%3A21832883031%2Cp_89%3AHUAWEI%2Cp_n_feature_twelve_browse-bin%3A27361676031&dc&language=en&pf_rd_i=21832883031&pf_rd_m=A1ZVRGNO5AYLOV&pf_rd_p=bf9d5754-be4e-409a-ad87-89abbc6d8911&pf_rd_r=TXHD83ZNX6GCQ496EMB5&pf_rd_s=merchandised-search-14&pf_rd_t=101&qid=1671311224&rnid=27361674031&ref=sr_nr_p_n_feature_twelve_browse-bin_3&ds=v1%3AHFnCGUhAuJfa8AmN%2BTwv9r4WJtv7kxrHGN7TQlJd8W8")
soup = bss4(url.text,'lxml')
#products_title = soup.findAll('h2',{"class":"a-size-mini a-spacing-none a-color-base s-line-clamp-4"})
#print(products_title)
products = soup.findAll('div',{"class": "sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"})

description = soup.find_all('span',{"class":"a-size-base-plus a-color-base a-text-normal"})
review=soup.find_all('span',{"class":"a-size-base"})
price = soup.find_all('span',{"class":"a-price-whole"})
links = soup.find_all('a',{"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
#

for i in range(len(products)):
  print("phone number",i+1,"\n")
  print("Phone features  ")
  print(description[i].text,"\n")
  Description.append(description[i].text)
 # Links.append(description[i].findNext("a").attrs['href'])
  Links.append(links[i].attrs['href'])
  print("Phone reviews  ")
  print(review[i].text,"\n")
  Review.append(review[i].text)
  print("Phone price  ")
  print(price[i].text,"\n")
  Price.append(price[i].text)
  #print("Phone delivery  ")
  #print(delivery[i].text,"\n")
  print("------------------------------------------------------------------------------------------------------------")
file_liste=[Description,Review,Price,Links]
exported =zip_longest(*file_liste)
with open('mobiles.csv' , 'w' , newline='') as my_file:
 writer = csv.writer(my_file)
 writer.writerow(['Features' , 'Reviews' , 'Prices','Link'])
 writer.writerows(exported)



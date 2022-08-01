import bs4
import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url='https://www.ebay.com/sch/i.html?_from=R40&_nkw=%E4%B8%83%E5%BD%A9%E8%99%B9+graphics+card&_sacat=0&LH_TitleDesc=0&rt=nc&Brand=Colorful&_dcat=27386'
page=urllib.request.urlopen(url)
page_soup=BeautifulSoup(page,'html.parser')
img_items=page_soup.find('div',id='srp-river-results')
img_div=img_items.find_all('div',{'class':'s-item__image'})

i=1
for img in img_div:
    img_tag=img.find('img',class_='s-item__image-img')
    img_src=img_tag.get('src')
    #img_title=img_tag.get('title')
    #if img_src[:1]=='/':
        #image='https:'+img_src
    #else:
    image=img_src
    print(image)
    file_name=str(i)
    i+=1
    img_file=open(file_name +'.jpeg','wb')
    img_file.write(urllib.request.urlopen(image).read())
    img_file.close()




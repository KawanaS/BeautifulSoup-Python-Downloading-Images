import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


url='https://www.newegg.com/Drones/SubCategory/ID-3708?cm_sp=Cat_Drones_1-_-VisNav-_-Drones//c1.neweggimages.com/WebResource/Themes/2005/Nest/logo_424x210.png'
page=urllib.request.urlopen(url)
page_soup=BeautifulSoup(page,'html.parser')
img_items=page_soup.find('div',{'class':'items-view is-grid'})
img_div=img_items.find_all(class_='item-container')

i=1
for img in img_div:
    img_tag=img.find('img')
    img_src=img_tag.get('src')
    if img_src[:1]=='/':
        image='https:'+img_src
    else:
        image=img_src
    print(image)
    file_name=str(i)
    i+=1
    img_file=open(file_name +'.jpeg','wb')
    img_file.write(urllib.request.urlopen(image).read())
    img_file.close()





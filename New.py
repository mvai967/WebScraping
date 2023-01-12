import requests
from bs4 import BeautifulSoup
import pandas as pd
final_data=[]
header={ 'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
link=[]
j=0
for i in range(1,50):
    try:
        page=requests.get('https://www.flipkart.com/mobiles-accessories/mobiles/pr?sid=tyy%2c4io&otracker=categorytree&page={0}'.format(i))
        if page.status_code == 200:
            link.append('https://www.flipkart.com/mobiles-accessories/mobiles/pr?sid=tyy%2c4io&otracker=categorytree&page={0}'.format(i))

    except:
        print('not ok')

print(len(link))
with open('ValidUrls.txt', 'w') as f:
    for line in link:
        f.write(line)
        f.write('\n')

# for accessing the txt url data
new=[]
file = open('ValidUrls.txt','r')
topology_list = file.readlines()
for i in topology_list:
    new.append(i)


for url in new:
    URL = requests.get(url)
    if URL.status_code == 200:
        page = requests.get(url,headers=header)
        soup=BeautifulSoup(page.content, 'html.parser')
        aab=soup.find_all('div', attrs={'class':'_13oc-S'})
        for ii in aab:
            try:
                Each_product_url="https://www.flipkart.com/"+ii.find('a', attrs={'class':'_1fQZEK'}).get('href')
            except:
                Each_product_url="No url"
            try:
                Product_name = ii.find('div', attrs={'class': '_4rR01T'}).text.strip()
            except:
                Product_name = "No Product Name "
            try:
                Rating = ii.find('div', attrs={'class': '_3LWZlK'}).text.strip()
            except:
                Rating = "No rating find"
            try:
                Price = ii.find('div', attrs={'class': '_30jeq3 _1_WHN1'}).text.strip()
            except:
                Price = "NOT AVAILABLE"
            try:
                RatingsReviews = ii.find('span', attrs={'class': '_2_R_DZ'}).text.strip()
            except:
                RatingsReviews = 'No find'
            try:
                Specification = ii.find('ul', attrs={'class': '_1xgFaf'}).text.strip()
            except:
                Specification = 'Not find'
            try:
                offer = ii.find('div', attrs={'class': '_3Ay6Sb'}).text.strip()
            except:
                offer = 'No offer now'

            record = {'Product_Url': Each_product_url,
                      'Product_Name': Product_name,
                      'Rating-Star': Rating,
                      'Price': Price,
                      'Ratings & Reviews': RatingsReviews,
                      'Specification': Specification,
                      'Offer': offer}
            final_data.append(record)

    else:
        print(url)
        with open('Resume.txt', 'w') as f:
            for line in url:
                f.write(line)
                # f.write('\n')






df=pd.DataFrame(final_data)
# print(df.Rat)
df.to_csv('Data.csv',index=False, encoding='utf-8')



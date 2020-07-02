import re

def following():
    f=open("dtfollowing.txt", errors='ignore')
    encrypt=f.read()
    pat=re.findall(r'title="[0-9a-zA-Z_/$.]+"',encrypt)
    listPattern=[]
    for i in pat:
        listPattern.append(i[6:])
    f.close()
    return listPattern

def followers():
    f=open("dtfollowers.txt", errors='ignore')
    encrypt=f.read()
    pat=re.findall(r'title="[0-9a-zA-Z_/$.]+"',encrypt)
    listPattern=[]
    for i in pat:
        listPattern.append(i[6:])
    f.close()
    return listPattern


f1=following()
f2=followers()
f1=set(f1)
f2=set(f2)

remain=f1.difference(f2)

print("!!!! These are the guys who does'nt follow you !!!!!")
print(f"total {len(remain)} peoples ,does'nt follow you")

for item in remain:
    print(item)

#####################  Future Inhancement ###############


# import bs4 as bs
# import urllib.request

# source = urllib.request.urlopen('https://www.instagram.com/deepak_tiwari_22/followers/').read()

# soup = bs.BeautifulSoup(source,'lxml')

# print(soup.title)

# from selenium import webdriver
# from bs4 import BeautifulSoup
# from requests import get

# url = "https://www.instagram.com/deepak_tiwari_22/followers/"

# def open_browser():
#     driver = webdriver.Chrome("/home/felipe/Downloads/chromedriver")
#     driver.get(url)
#     driver.find_element_by_link_text('followers').click()

# open_browser()


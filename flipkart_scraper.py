import requests 
import csv
from bs4 import BeautifulSoup
import pandas as pd

i=1
count=0
url = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Mi_mobile-phones-store_ZHYC957RFL_wp3&fm=neo%2Fmerchandising&iid=M_a2d552d8-84c1-4254-a5b2-24ff1eacaf81_2.ZHYC957RFL&ppt=CLP&ppn=CLP%3Asamsung-mobile-store&page=" + str(i)
while i<9:
	i = i+1
	r=requests.get(url)
	r.content
	soup=BeautifulSoup(r.content,'html.parser')
	if r.status_code != 200:
		break
	url = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Mi_mobile-phones-store_ZHYC957RFL_wp3&fm=neo%2Fmerchandising&iid=M_a2d552d8-84c1-4254-a5b2-24ff1eacaf81_2.ZHYC957RFL&ppt=CLP&ppn=CLP%3Asamsung-mobile-store&page=" + str(i)
	
	"""
	#How to print Html content of a webpage
	print(soup.prettify()) 
	links=soup.find_all("a")
	for link in links:
		if "http" in link.get("href"):
			print("<a href='%s'>%s</a>"%(link.get("href"),link.text))

	"""
	g_data=soup.find_all("a",{"class":"_31qSD5"})

	for item in g_data:
		count=count+1
		name=item.find("div", attrs={"class":"_3wU53n"}).text
		price=item.find("div", attrs={"class":"_1vC4OE _2rQ-NK"}).text
		print(name,price)
		
		
print("count is : " +str(count))





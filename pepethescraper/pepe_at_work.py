import requests
from bs4 import BeautifulSoup
import urllib.request
import os

from tqdm.auto import tqdm
import re

_HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}  # defining headers for browser

class Scraper:
	def __init__(self):
		pass

	def scrape(self, search_query, number_of_memes=100):
		pass

class KYMScraper(Scraper):
	def __init__(self, output_format="csv", save_dir_path="memes", save_img=True):
		self.output_format = output_format
		self.save_dir_path = save_dir_path
		self.save_img = save_img
		self.allowed_image_extensions = ['.jpg', '.jpeg', '.png']

	def scrape(self, search_query, number_of_memes=100):
		search_query = search_query.replace(" ","+")
		pat = re.compile('<img [^>]*data-src="([^"]+)')

		if not os.path.exists(self.save_dir_path):
			os.makedirs(self.save_dir_path)

		if(self.output_format == "csv"):
			file = open(os.path.join(self.save_dir_path,'data.csv'),'w')
			file.write("Name,URL,Image URLs")
			file.write("\n")

		meme_paths = []
		
		for page_number in range(1,2000):
			try:
				search_url = "http://knowyourmeme.com/search?page=" + str(page_number) + "&q=" + search_query
				search_page = requests.get(search_url, headers=_HEADERS)

				soup = BeautifulSoup(search_page.content, 'html.parser')
				meme_search_list = soup.find(class_='entry_list')
				if meme_search_list is None:
					break
				
				meme_paths_for_page = meme_search_list.find_all('a', href=True)
				meme_paths_for_page = [meme_path['href'] for meme_path in meme_paths_for_page]

				meme_paths += list(set(meme_paths_for_page))
				if len(meme_paths) >= number_of_memes:
					meme_paths = meme_paths[:number_of_memes]
					break
			except:
				continue

		# remove duplicates
		meme_paths = list(set(meme_paths))
		meme_page_urls = ["http://knowyourmeme.com" + meme_path for meme_path in meme_paths if meme_path[0] == '/']

		print("Crawling " + str(len(meme_page_urls)) + " templates...")
		
		meme_page_urls_tqdm = tqdm(meme_page_urls)
		for meme_page_url in meme_page_urls_tqdm:
			
			# extract the text
			template_name = meme_page_url.split('/')[-1].replace('/','')
			dir_for_meme = os.path.join(self.save_dir_path, template_name)
			if not os.path.exists(dir_for_meme):
				os.makedirs(dir_for_meme)
			
			meme_page = requests.get(meme_page_url, headers=_HEADERS)
			meme_text_soup = BeautifulSoup(meme_page.text, 'html.parser')
			meme_text = meme_text_soup.findAll("div", {"class": "entry-section"})
			

			# extract the image urls
			try:
				img_urls = []
				meme_page_url_with_examples = meme_page_url + "/photos/sort/score"
				meme_page_with_imgs = requests.get(meme_page_url_with_examples, headers=_HEADERS)
				meme_imgs_soup = BeautifulSoup(meme_page_with_imgs.content, 'html.parser')
				meme_imgs = meme_imgs_soup.findAll("div",{"class":"item"})

				for meme_img_ctr, meme_img in enumerate(meme_imgs):
					img_url = pat.findall(str(meme_img))
					_, ext = os.path.splitext(img_url[0])
					if ext in self.allowed_image_extensions:
						img_urls.append(img_url[0])
					
					if self.save_img:
						
						if ext in self.allowed_image_extensions:
							try:
								urllib.request.urlretrieve(img_url[0], os.path.join(dir_for_meme,str(meme_img_ctr) + ext))
							except Exception as e:
								# print(e)
								continue

			except Exception as e:
				continue

			if(self.output_format == "csv"):
				text_string = ""
				for i in range(len(meme_text)):
					text_string += " ".join(meme_text[i].text.split()) + "\n"
				text_string = text_string[:-1]


				file.write(template_name + "," + meme_page_url + "," + " ".join(img_urls))
				file.write("\n")

			# write the text to a text file
			meme_file = open(os.path.join(dir_for_meme,'meme_data.txt'), "w")
			meme_file.write("NAME OF TEMPLATE: " + template_name)
			meme_file.write("\n")
			meme_file.write("MEME PAGE URL: " + meme_page_url)
			meme_file.write("\n")
			meme_file.write("TEXT: \n")
			meme_file.write(text_string)
			meme_file.write("\n")
			meme_file.close()

		file.close()
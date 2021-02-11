# Pepe The Scraper

Library for scraping memes off Know Your Meme and Reddit (along with the explanations and background provided for all the memes)


<p align="center">
  <img width="200" height="200" src="misc/images/pepe_the_frog.jpg">
</p>

### Setting Up Pepe The Scraper
```
git clone https://github.com/abheesht17/pepethescraper.git
cd pepethescraper
python setup.py install
pip install clean-text[gpl]==0.3.0
pip install praw==7.1.4
```

### Examples:

- Help Pepe scrape memes off KYM!

```
from pepethescraper.pepe_at_work import KYMScraper
scraper = KYMScraper(save_dir_path="memes", save_img=False)
scraper.scrape(search_query="political memes",number_of_memes=5)
```

- Help Pepe scrape memes off Reddit!

```
from pepethescraper.pepe_at_work import RedditScraper
scraper = RedditScraper(save_dir_path="memes", save_img=False)
scraper.scrape(search_query="PoliticalMemes",number_of_memes=5)
```

### Pepe's Helpers

- clean-text
- praw

### Upcoming Updates:

- Pepe's learning how to scrape memes off Twitter and ImgFlip.
- Pepe will also try to clean the text from KYM.
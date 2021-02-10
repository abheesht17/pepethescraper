# Pepe The Scraper

Library for scraping memes off Know Your Meme (along with the explanations and background provided for all the memes)


<p align="center">
  <img width="200" height="200" src="misc/images/pepe_the_frog.jpg">
</p>

### Examples:

- Help Pepe scrape memes off KYM!

```
from pepethescraper.pepe_at_work import KYMScraper
scraper = KYMScraper(save_dir_path="memes", save_imgs=False)
scraper.scrape(search_query="political memes",number_of_memes=5)
```

- Help Pepe scrape memes off Reddit!

```
from pepethescraper.pepe_at_work import RedditScraper
scraper = KYMScraper(save_dir_path="memes", save_imgs=False)
scraper.scrape(search_query="PoliticalMemes",number_of_memes=5)
```

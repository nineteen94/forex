USD to INR API. Extensible to any X to Y Currency.

Install Dependencies
- pip install scrapy
- pip install scrapyrt

Step 1 - Fetch Data
Fetching the data of USD to INR using scrapy.

Step 2 - Convert crawler service to an API. Install scrapyrt.
scrapyrt -p <PORT_NUMBER>
http://localhost:<PORT_NUMBER>/crawl.json?start_requests=true&spider_name=usd_inr


Disclaimer: 
This is for educational purpose only. Bombarding a site with requests impacts the site's performance. Your IP can also get blocked. 
Use an API service instead. It will be more reliable.  

# -*- coding: utf-8 -*-
import scrapy
import re


class Imdb2019Spider(scrapy.Spider):
    name = 'imdb2019'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31']

    def parse(self, response):
        for movie in response.xpath("//div[@class='lister-list']/div[@class='lister-item mode-advanced']"):
            ### 'rank' adalah bersifat opsional, bisa digunakan jika ingin tahu ranking title based on popularity.
            # rank = movie.xpath(".//div[@class='lister-item-content']/h3/span[@class='lister-item-index unbold text-primary']/text()").get()
            # rank = re.findall(r'\d+', rank)
            judul = movie.xpath(".//div[@class='lister-item-content']/h3/a/text()").get()
            imdb_rating = movie.xpath(".//div[@class='lister-item-content']/div[@class='ratings-bar']/div[@class='inline-block ratings-imdb-rating']/strong/text()").get()
            metascore = movie.xpath(".//div[@class='lister-item-content']/div[@class='ratings-bar']/div[@class='inline-block ratings-metascore']/span[@class='metascore  mixed']/text()").get()
            votes = movie.xpath(".//div[@class='lister-item-content']/p[@class='sort-num_votes-visible']/span[@name='nv']/text()").get()
            votes = re.sub('[^0-9]','', str(votes))
            
            yield {
                # 'rank' : rank ,
                'judul' : judul,
                'imdb_rating' : imdb_rating,
                'metascore' : metascore,
                'votes' : votes
            }

        next_page = response.xpath("(//a[@class='lister-page-next next-page'])[2]/@href").get()

        if next_page: 
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse )
            
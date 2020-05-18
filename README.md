# alg_caps_webscrapping

NOTE 1

Saya menggunakan scrapy untuk webscrapping.

Python code scrapping nya ada di folder: imdb/spiders/imdb2019.py


Note 2

Hasil scrap saya simpan sebagai file: movies.csv

Total titles di imdb (url: https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31) ada 308,330 titles.

Kode saya seharusnya bisa berhasil scrap semua titles. Tapi untuk project capstone ini, saya hentikan proses scrapingnya sampai 12.450 movies saja, dan output ke file: movies.csv


Note 3

File app.py ada di folder: web/app.py

Saya menggunakan scrapyrt dan flask

Untuk keperluan app.py, dan mempercepat proses penampilan di web, saya melimit scraping hanya sampai 100 movies.

Settingan nya ada di folder: imdb/settings.py yaitu:

CLOSESPIDER_ITEMCOUNT = 100

Jika ingin scrape keseluruhan movie, buang line "CLOSESPIDER_ITEMCOUNT = 100" ini.
(WARNING: Jika line ini dibuang, maka scrapyrt akan memproses keseluruhan 308.330 movies dan akan membutuhkan loading time yang sangat lama, sebelum akhirnya menampilkan tampilan data movies di web browser)

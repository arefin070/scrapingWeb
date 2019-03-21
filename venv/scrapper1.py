import wlog
import upscraping

wlog.set_customer_log_info('error.log')



news_scrap = upscraping.NewsScraper(upscraping.url_aj, wlog)


#news_scrap.retrieve_webpage()
news_scrap.write_webpage_as_html()

news_scrap.read_webpage_from_html()
news_scrap.convert_data_to_bs4()
#news_scrap.print_beautiful_soup()
news_scrap.parse_soup_to_simple_html()

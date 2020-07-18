import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.acnc.gov.au/charity?location%5B0%5D=266&location%5B1%5D=251&location%5B2%5D=276&location%5B3%5D=286&location%5B4%5D=342&location%5B5%5D=271&location%5B6%5D=246&location%5B7%5D=281&facet__select__field_beneficiaries=0&facet__select__field_countries=0&facet__select__acnc_search_api_sub_history=0&facet__select__field_status=0#search',
    ]

    def parse(self, response):
        for quote in response.css('div.table-responsive'):
            yield {
                'text': quote.css('td.views-field-acnc-search-api-status-normalised active::text').getall(),
                'author': quote.css('td.views-align-center::text').getall(),

            }




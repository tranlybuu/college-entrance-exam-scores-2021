import scrapy
from ..items import Diemthidaihoc2021Item

class ScoreBotSpider(scrapy.Spider):
    start_urls = []
    # start_urls = ['https://vietnamnet.vn/vn/giao-duc/tra-cuu-diem-thi-thpt/?y=2021&sbd=33000001']
    for item in range(33000001,33010001):
        url = 'https://vietnamnet.vn/vn/giao-duc/tra-cuu-diem-thi-thpt/?y=2021&sbd=' + str(item)
        start_urls.append(url)
    name = 'score_bot'

    def parse(self, response):

        id = "-"
        w_math = "-"
        w_literature = "-"
        w_foreign_language = "-"
        x_physics = "-"
        x_chemistry = "-"
        x_biology = "-"
        y_history = "-"
        y_geography = "-"
        y_civic_education = "-"
        z_average = 0
        z_max = 0
        z_min = 10

        count_subjects = response.xpath('//div[@class="d-flex justify-content-between search-result-line py-3 px-3"]').getall()
        count_subjects = str(count_subjects)
        check = count_subjects.split("<div>")
        count_subjects = len(check) - 1

        id = response.xpath('//span[@class="student-id text-dc3545"]/text()').get()
        for x in range(1,count_subjects+1):
            subjects = response.xpath(f'//div[@class="d-flex justify-content-between search-result-line py-3 px-3"][{x}]/div[1]/text()').get()
            if "Toán" in subjects:
                try:
                    w_math = response.xpath(f'//div[@class="d-flex justify-content-between search-result-line py-3 px-3"][{x}]/div[2]/text()').get()
                except:
                    pass
            elif "Văn" in subjects:
                try:
                    w_literature = response.xpath(f'//div[@class="d-flex justify-content-between search-result-line py-3 px-3"][{x}]/div[2]/text()').get()
                except:
                    pass
            elif "Ngoại ngữ" in subjects:
                try:
                    w_foreign_language = response.xpath(f'//div[@class="d-flex justify-content-between search-result-line py-3 px-3"][{x}]/div[2]/text()').get()
                except:
                    pass
            elif "Sử" in subjects:
                try:
                    y_history = response.xpath(f'//div[@class="d-flex justify-content-between search-result-line py-3 px-3"][{x}]/div[2]/text()').get()
                except:
                    pass

            elif "Địa" in subjects:
                try:
                    y_geography = response.xpath(f'//div[@class="d-flex justify-content-between search-result-line py-3 px-3"][{x}]/div[2]/text()').get()
                except:
                    pass

            elif "GDCD" in subjects:
                try:
                    y_civic_education = response.xpath(f'//div[@class="d-flex justify-content-between search-result-line py-3 px-3"][{x}]/div[2]/text()').get()
                except:
                    pass

            elif "Lí" in subjects:
                try:
                    x_physics = response.xpath(f'//div[@class="d-flex justify-content-between search-result-line py-3 px-3"][{x}]/div[2]/text()').get()
                except:
                    pass

            elif "Hóa" in subjects:
                try:
                    x_chemistry = response.xpath(f'//div[@class="d-flex justify-content-between search-result-line py-3 px-3"][{x}]/div[2]/text()').get()
                except:
                    pass

            elif "Sinh" in subjects:
                try:
                    x_biology = response.xpath(f'//div[@class="d-flex justify-content-between search-result-line py-3 px-3"][{x}]/div[2]/text()').get()
                except:
                    pass

        list = [w_math, w_literature, w_foreign_language, x_physics, x_chemistry, x_biology, y_history, y_geography, y_civic_education]
        count = 0
        for x in list:
            if "-" not in x:
                x = float(str(x).strip())
                z_average += x
                if x>z_max:
                    z_max = x
                elif x<z_min:
                    z_min = x
        z_average = round((z_average/count_subjects),2)

        item = Diemthidaihoc2021Item()
        item["id"] = id
        item["w_math"] = w_math
        item["w_literature"] = w_literature
        item["w_foreign_language"] = w_foreign_language
        item["x_physics"] = x_physics
        item["x_chemistry"] = x_chemistry
        item["x_biology"] = x_biology
        item["y_history"] = y_history
        item["y_geography"] = y_geography
        item["y_civic_education"] = y_civic_education
        item["z_average"] = z_average
        item["z_max"] = z_max
        item["z_min"] = z_min
        yield item
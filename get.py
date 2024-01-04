import requests  # 用于向网站发送请求
from lxml import etree  # lxml为第三方网页解析库，强大且速度快
import json  # 数据处理与写入


def getData(user):
    url = f'https://codeforces.com/submissions/{user}'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    }
    response = requests.get(url, headers=headers, timeout=10)
    html = response.text

    parse = etree.HTML(html)  # 解析网页

    all_tr = parse.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr')

    datalist = {'data': []}

    for tr in all_tr:
        tr = {
            '#': ''.join(tr.xpath('./td[1]/a/text()')).strip(),
            'When': ''.join(tr.xpath('./td[2]//text()')).strip(),
            'Problem': ''.join(tr.xpath('./td[4]/a/text()')).strip(),
            'Lang': ''.join(tr.xpath('./td[5]/text()')).strip(),
            'Verdict': ''.join(tr.xpath('./td[6]/span/span/text()')).strip(),
            'Time': ''.join(tr.xpath('./td[7]/text()')).strip().replace('\u00a0', ' '),
            'Memory': ''.join(tr.xpath('./td[8]/text()')).strip().replace('\u00a0', ' '),
        }
        datalist['data'].append(tr)

    with open("datas.json", 'w') as file:
        json.dump(datalist, file, indent=4)


if __name__ == '__main__':
    getData('AlkyneTrp')
    print("已完成数据爬取!")

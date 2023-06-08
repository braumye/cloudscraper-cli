import argparse
import cloudscraper

# 创建解析器
parser = argparse.ArgumentParser(
    description='Request a URL and print the response.')
parser.add_argument('url', type=str, help='The URL to request')

# 解析参数
args = parser.parse_args()

# 请求URL
scraper = cloudscraper.create_scraper()
response = scraper.get(args.url)

# 打印响应
print(response.text)

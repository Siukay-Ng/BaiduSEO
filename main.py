
# Project: BaiduSearch
# File: main.py
# Author: ClassmateLin
# Email: 406728295@qq.com
# Time: 2020/4/1 9:34 下午
# DESC:

from search import PcSearch
from browser import Browser


if __name__ == '__main__':
    keys = [
        '资源分享',
        'python教程'
    ]
    site = 'fenlanli.com'
    browser = Browser(driver_path='./chromedriver.exe')
    app = PcSearch(browser=browser, keys=keys, site=site)
    app.run()



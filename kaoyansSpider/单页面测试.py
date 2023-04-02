from pymysql import Connection
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def share_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    # path是你自己浏览器的路径
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser


browser = share_browser()
url = 'https://www.kaoyan.cn/school/495/major'
browser.get(url)
def get_syl_jianshe():
    flag = True
    try:
        find_more = browser.find_element(By.XPATH, '//div[@class="school-page-major_fold__14HqV"]')
        find_more.click()
        print(flag)
        # return flag
    except:
        flag = False
        print(flag)
    print(flag)
        # return flag

    # find_more = browser.find_element(By.XPATH, '//div[@class="school-page-major_fold__14HqV"]').text
    # if flag:
    #     syl = browser.find_elements(By.XPATH, '//p[@class="school-page-major_majorDoubleTitle__39nC8"]')
    #     str = ''
    #     for l in syl:
    #         str = str + l.text + '  '
    #     print(str)
    # else:
    #     print("没有双一流")
if __name__=='__main__':
    get_syl_jianshe()

# str="'三个代表'重要思想武装教育干部，为吉林经济建设和社会发å'"
# newstr=str.replace("'","\"")
# print(newstr)

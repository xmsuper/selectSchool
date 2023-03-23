# from pymysql import Connection
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# def share_browser():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-gpu")
#     # path是你自己浏览器的路径
#     path=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
#     chrome_options.binary_location=path
#     browser=webdriver.Chrome(chrome_options=chrome_options)
#     return browser
# browser=share_browser()
# url='https://www.kaoyan.cn/school'
# browser.get(url)
# nextBtn=browser.find_element(By.XPATH,'//li[@title="下一页"]')
# s=nextBtn.get_attribute('aria-disabled')
# print(s)

str="'三个代表'重要思想武装教育干部，为吉林经济建设和社会发å'"
newstr=str.replace("'","\"")
print(newstr)
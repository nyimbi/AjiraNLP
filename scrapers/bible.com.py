
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from html.parser import HTMLParser
from bs4 import BeautifulSoup

# Right Click Button
xButton = '//*[@id="react-app-Bible"]/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/a/div'
# xButton = '//*[@id="react-app-Bible"]/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/a/div/svg'

xBook = '//*[@id="react-app-Bible"]/div/div[2]/div/div/div[1]/div/div/div'
xReader = '//*[@id="react-app-Bible"]/div/div[2]/div/div/div[1]'
xBible = '//*[@id="react-app-Bible"]'

#react-app-Bible > div > div.row > div:nth-child(2) > div > div.bible-reader.primary-chapter
# //*[@id="react-app-Bible"]/div/div[2]/div[2]/div/div[1]
# #react-app-Bible > div > div.row > div > div > div.bible-reader.primary-chapter > div
xCopyright ='//*[@id="react-app-Bible"]/div/div[2]/div/div/div[2]'
cCopyright = 'version-copyright'
# //*[@id="react-app-Bible"]/div/div[2]/div/div/div[2]/a/span
homeURL='https://www.bible.com/zu/bible/1810/GEN.1.DHO15'
# homeURL='https://www.bible.com/zu/bible/1810/ESG.1.DHO15'
# homeURL='https://www.bible.com/zu/bible/1810/2MA.1.DHO15'
# homeURL='https://www.bible.com/zu/bible/1810/JOB.1.DHO15'
# homeURL='https://www.bible.com/zu/bible/1810/BAR.1.DHO15 '
parURL = 'https://www.bible.com/zu/bible/1202/GEN.1.GIKDC?parallel=1810'

timeout = 10 # Pge load timeout period





option = webdriver.ChromeOptions()
option.add_argument('—incognito')

browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=option)
browser.implicitly_wait(15)
browser.get(homeURL)
# browser.refresh()

right_button = browser.find_element_by_xpath(xButton) #'//*[@id="react-app-Bible"]/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/a/div')


for i in range(2):
    browser.refresh()
    
    try:
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'book'))
        )
    except TimeoutException:
        print('Timed out waiting for page to load')
        continue
        # browser.quit()
    
    
    # Now on New Page
    # page = browser.page_source
    # bib = browser.find_element_by_xpath(xBible).text
    bib = browser.find_element_by_class_name('reader').text
    
    soup = BeautifulSoup(bib, 'lxml')
    pg = soup.get_text()
    
    # get filename
    x =  browser.current_url.split('/')
    fname = x[len(x) -1]
    file = open(fname+'.txt','w')
    file.write(pg)
    file.close()
    
    # print(str(i) + ':' + browser.title)
    print(str(i) +' ' + browser.current_url + ' ' +str(len(pg)) )
    # Next Page
    right_button = browser.find_element_by_xpath(xButton)
    right_button.click()
    
    # print(len(pg))
    # print(pg[:300])
    # print(len(rdr))
    # print(rdr[5000:5080])
    #print(chapter)
    
# browser.quit()


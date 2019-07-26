from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('https://en.wikipedia.org/wiki/Lists_of_Americans')

content_blocks = browser.find_elements_by_css_selector("div[class='div-col columns column-width']")
a_elements = []
elements = content_blocks[0].find_elements_by_tag_name("a")
for el in elements:
    a_elements.append(el)
    
links = [link.get_attribute('href') for link in a_elements]

count = 0
num = 0

skipWords = ["_Americans", "List_of", "Category", "Special", "Main_Page", "Portal", "Help", "Contact_us", "Wikipedia:", "Template:", "Template_talk:"]
for link in links:
    browser.get(link)
    if (num % 2) == 0:
        allLinks = browser.find_elements_by_tag_name("a")
        sublinks = []
        for i in allLinks:
            if i.get_attribute("class") == "":
                sublinks.append(i.get_attribute('href'))
        cleanLinks = []
        for val in sublinks: 
            if val != None and ("https://en.wikipedia.org/wiki/" in val) and not(any(x in val for x in skipWords)): 
                cleanLinks.append(val) 
                
        for link in cleanLinks:
            print(link)
            print(count)
            browser.get(link)
            allRowScope = browser.find_elements_by_css_selector("th[scope='row']")
            allRowScopeText = (i.text for i in allRowScope)
            if "Born" in allRowScopeText:
                count+=1
        print("************************DONE WITH A CATE**************************")
    num+=1
print(count)   
    
    
    
    
    
    
browser.quit()
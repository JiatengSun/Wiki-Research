from selenium import webdriver
from selenium.webdriver.common.keys import Keys


'''->TODO '''
#def check_repeat:
'''<- '''

'''->disable images to get faster'''
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
'''<-'''

#browser = webdriver.Chrome()
browser = webdriver.Chrome(chrome_options=chrome_options)

#blockList = ["List_of_people", "Academy_of_Honor", "people_from", "_Alabama", "Category:", "Portal:", "_area", "_Area", "Template_", "Template:", "_Plateau", "_Shore", "_District", "Valley", "_Region", "(United_States)", "_Plain", "Alabama_"]


def Alabama(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        a_ele.append(k.find_elements_by_css_selector("a")[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Hank_Aaron')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Delmon_Young')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return   

def Alaska(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    td160_ele = bodyContent.find_elements_by_css_selector("td[width='160pt']")
    a_ele = []
    for i in td160_ele:
        a_ele.append(i.find_element_by_css_selector("a"))
    links = [link.get_attribute('href') for link in a_ele]
    print(links)
    print(len(links))
    global totalCount 
    totalCount += len(links)
    return
    
def Arizona(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Max_Cannon')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/James_Rallison')
    excludeIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Helen_Lorraine')
    for i in range(startIndex,endIndex+1):
        if i != excludeIndex:
            peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return
    
def Arkansas(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Joey_Lauren_Adams')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Roger_L._Worsley')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return
    
def California(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/12th_Planet_(musician)')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Steve_Young')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return
    
def Colorado(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Amy_Adams')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/James_Q._Wilson')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Connecticut(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Christopher_Abbott')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Ruth_Madoff')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Delaware(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Wilbur_L._Adams')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Aleksandra_Ziolkowska-Boehm')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

#Florida's format is td without width
def Florida(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    tr_ele = bodyContent.find_elements_by_css_selector("tr")
    td_ele = []
    for i in tr_ele:
        td = i.find_elements_by_css_selector("td")
        if len(td) > 0:
            td_ele.append(td[0])
    a_ele = []
    for i in td_ele:
        a_ele.append(i.find_element_by_css_selector("a"))
    links = [link.get_attribute('href') for link in a_ele]
    startIndex = links.index('https://en.wikipedia.org/wiki/Sara_Blakely')
    endIndex = links.index('https://en.wikipedia.org/wiki/Carlos_Vald%C3%A9s_(actor)')
    cleanLinks = []
    for i in range(startIndex,endIndex+1):
        cleanLinks.append(links[i])
    print(cleanLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Georgia(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/2_Chainz')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Yung_Joc')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Hawaii(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Brian_Adams_(wrestler)')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Zhang_Xueliang')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Idaho(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/William_Agee')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Norma_Zimmer')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Illinois(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Emma_Abbott')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Tony_Zych')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Indiana(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Squire_Boone')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Homer_Van_Meter')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Iowa(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Dudley_W._Adams')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Larry_Zox')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Kansas(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Milton_S._Eisenhower')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Marc_Sappington')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Kentucky(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    tr_ele = bodyContent.find_elements_by_css_selector("tr")
    td_ele = []
    for i in tr_ele:
        td = i.find_elements_by_css_selector("td")
        if len(td) > 0:
            td_ele.append(td[0])
    a_ele = []
    for i in td_ele:
        L = i.find_elements_by_css_selector("a")
        if len(L)>0:
            a_ele.append(L[0])
    links = [link.get_attribute('href') for link in a_ele]
    startIndex = links.index('https://en.wikipedia.org/wiki/James_Lane_Allen')
    endIndex = links.index('https://en.wikipedia.org/wiki/Forest_Shely')
    cleanLinks = []
    for i in range(startIndex,endIndex+1):
        cleanLinks.append(links[i])
    print(cleanLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Louisiana(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://es.wikipedia.org/wiki/Ashley_Grace')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Buckwheat_Zydeco')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Maine(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Angela_Adams')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Nick_Wyman')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Maryland(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Spiro_T._Agnew')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/George_Young_(American_football_executive)')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Massachusetts(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Lucius_W._Briggs')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Bernard_Wolfman')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Michigan(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Ford_Beebe')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Floyd_Wilcox')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Minnesota(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Johan_Arnd_Aasgaard')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Ben_Wyatt')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Mississippi(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/James_Bevel')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Toby_Turner')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

def Missouri(url):
    browser.get(url)
    bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
    ul_ele = bodyContent.find_elements_by_css_selector("ul")
    li_ele = []
    a_ele = []
    for i in ul_ele:
        j = i.find_elements_by_css_selector("li")
        li_ele = li_ele + j
    for k in li_ele:
        allLinks = k.find_elements_by_css_selector("a")
        if len(allLinks)>0:
            a_ele.append(allLinks[0])
    links = [link.get_attribute('href') for link in a_ele]
    cleanLinks = []
    #and not(any(x in val for x in blockList))
    for val in links: 
        if val != None and ("wikipedia.org" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Helen_Andelin')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Roy_Wilkins')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    global totalCount 
    totalCount += len(cleanLinks)
    return

'''=>chang's half'''
temp_indices = []

def vcard_state(url, state):
    sub_counter = 0 # for counting people in this state
    browser.get(url)
    persons = browser.find_elements_by_css_selector("span[class='vcard']")
    for p in persons:
        person = p.find_element_by_tag_name('a') #note i put "element" here, not "elements".
        results.append(person)
        sub_counter += 1
    print(state, 'has', str(sub_counter), 'people')
    global totalCount
    totalCount += sub_counter

def ul_state(url, state):
    sub_counter = 0 #for counting people in this state
    browser.get(url)
    sections = browser.find_elements_by_css_selector('ul')
    for i in temp_indices:
        persons = sections[i].find_elements_by_tag_name('li')

        for p in persons:  
#            print(i, sub_counter)
            allLinks = p.find_elements_by_tag_name('a')
            if (len(allLinks) == 0):
                continue
            person = allLinks[0]
#            print(p.get_attribute('class'))
#            print('hi')
            '''->in case of gallery and exclude weird [li]s:'''
            if p.get_attribute('class') == 'gallerybox':
#                print(allLinks[0].get_attribute('href'))
#                print(allLinks[1].get_attribute('href'))
                person = allLinks[1]
            elif p.get_attribute('class') != '':
                continue
            '''<-'''
#            print(person.get_attribute('href'))
            results.append(person)
            sub_counter += 1
#        print('---')
#        break
    print(state, 'has', str(sub_counter), 'people')
    global totalCount
    totalCount += sub_counter
    
def test_ul_state(url, state):
    print('----------', state, '----------')
    browser.get(url)
    sections = browser.find_elements_by_css_selector('ul')
    for i in range(0, 200):        
#    for i in temp_indices:        
        print(i, sections[i].find_element_by_tag_name('li').text)
#        break
    return

def Montana(url):
    return vcard_state(url, 'Montana')

def Nebraska(url):
    global temp_indices
    temp_indices = []
    for i in range(2,15):   #2-14
        temp_indices.append(i)
    temp_indices.append(16)
    return ul_state(url, 'Nebraska')

def Nevada(url):
    global temp_indices
    temp_indices = []
    for i in range(3,15):   #3-14
        temp_indices.append(i)
    return ul_state(url, 'Nevada')

def New_Hampshire(url):
    global temp_indices
    temp_indices = []
    for i in range(2,21):   #2-20
        temp_indices.append(i)
    return ul_state(url, 'New_Hampshire')

def New_Jersey(url):
    global temp_indices
    temp_indices = []
    for i in range(2,9):   #2-8
        temp_indices.append(i)
    return ul_state(url, 'New_Jersey')

def New_Mexico(url):
    global temp_indices
    temp_indices = []
    for i in range(2,14):   #2-13
        temp_indices.append(i)
    return ul_state(url, 'New_Mexico')

def New_York(url):
    global temp_indices
    temp_indices = []
    for i in range(4,34):   #4-33
        temp_indices.append(i)
    return ul_state(url, 'New_York')

def North_Carolina(url):
    global temp_indices
    temp_indices = []
    for i in range(1,23):   #1-22
        temp_indices.append(i)
    return ul_state(url, 'North_Carolina')

def North_Dakota(url):
    global temp_indices
    temp_indices = []
    for i in range(1,5):   #1-4
        temp_indices.append(i)
    return ul_state(url, 'North_Dakota')
 
'''TODO: redlink'''
def Ohio(url):
    global temp_indices
    temp_indices = []
    for i in range(1,36):   #1-35
        temp_indices.append(i)
    return ul_state(url, 'Ohio')
 
def Oklahoma(url):
    global temp_indices
    temp_indices = []
    for i in range(1,23):   #1-22
        temp_indices.append(i)
    return ul_state(url, 'Oklahoma')
 
def Oregon(url):
    global temp_indices
    temp_indices = []
    for i in range(2,26):   #2-25
        temp_indices.append(i)
    return ul_state(url, 'Oregon')
 
    '''TODO: redlink'''
def Pennsylvania(url):
    global temp_indices
    temp_indices = []
    for i in range(1,35):   #1-34
        temp_indices.append(i)
    return ul_state(url, 'Pennsylvania')
 
def Rhode_Island(url):
    global temp_indices
    temp_indices = []
    for i in range(1,17):   #1-16
        temp_indices.append(i)
    return ul_state(url, 'Rhode_Island')
 
def South_Carolina(url):
    global temp_indices
    temp_indices = []
    for i in range(3,16):   #1-15
        temp_indices.append(i)
    return ul_state(url, 'South_Carolina')
 
def South_Dakota(url):
    global temp_indices
    temp_indices = []
    for i in range(1,14):   #1-13
        temp_indices.append(i)
    return ul_state(url, 'South_Dakota')
 
def Tennessee(url):
    global temp_indices
    temp_indices = []
    for i in range(2,26):   #2-25
        temp_indices.append(i)
    return ul_state(url, 'Tennessee')
 
def Texas(url):
    global temp_indices
    temp_indices = []
    for i in range(6,127):   #6-126
        temp_indices.append(i)
    return ul_state(url, 'Texas')
 
def Utah(url):
    global temp_indices
    temp_indices = []
    for i in range(2,27):   #2-26
        temp_indices.append(i)
    return ul_state(url, 'Utah')
 
def Vermont(url):
    global temp_indices
    temp_indices = []
    for i in range(2,27):   #2-26
        temp_indices.append(i)
    return ul_state(url, 'Vermont')
 
def Virginia(url):
    global temp_indices
    temp_indices = []
    for i in range(2,32):   #2-31
        temp_indices.append(i)
    return ul_state(url, 'Virginia')
 
def Washington(url):
    global temp_indices
    temp_indices = []
    for i in range(2,27):   #2-26
        temp_indices.append(i)
    return ul_state(url, 'Washington')
 
def West_Virginia(url):
    global temp_indices
    temp_indices = []
    for i in range(1,16):   #1-15
        temp_indices.append(i)
    return ul_state(url, 'West_Virginia')
 
def Wisconsin(url):
    global temp_indices
    temp_indices = []
    for i in range(3,45):   #3-44
        temp_indices.append(i)
    return ul_state(url, 'Wisconsin')
 
def Wyoming(url):
    global temp_indices
    temp_indices = []
    for i in range(2,13):   #2-12
        temp_indices.append(i)
    return ul_state(url, 'Wyoming')


def American_Samoa(url):
    global temp_indices
    temp_indices = []
    for i in range(1,15):   #1-14
        temp_indices.append(i)
    return ul_state(url, 'American_Samoa')

def Guam(url):
    global temp_indices
    temp_indices = []
    for i in range(5,18):   #5-17
        temp_indices.append(i)
    return ul_state(url, 'Guam')


def Puerto_Rico(url):
    global temp_indices
    temp_indices = []
    for i in range(5,136):   #5-135
        temp_indices.append(i)
    return ul_state(url, 'Puerto_Rico')
 
def United_States_Virgin_Islands(url):
    global temp_indices
    temp_indices = []
    for i in range(1,12):   #1-11
        temp_indices.append(i)
    return ul_state(url, 'United_States_Virgin_Islands')
'''<='''




#MAIN PROGRAM
totalCount = 0
browser.get('https://en.wikipedia.org/wiki/Lists_of_Americans')
bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
allBlocks = bodyContent.find_elements_by_css_selector("div[class='div-col columns column-width']")
stateBlock = allBlocks[1]
stateList = stateBlock.find_elements_by_css_selector("li")
stateNameList = [i.text for i in stateList]
stateLinkList = [i.find_element_by_css_selector("a").get_attribute('href') for i in stateList]

territoryBlock = allBlocks[2]
territoryList = territoryBlock.find_elements_by_css_selector("li")
territoryNameList = [i.text for i in territoryList]
territoryLinkList = [i.find_element_by_css_selector("a").get_attribute('href') for i in territoryList]

Alabama(stateLinkList[0])
Alaska(stateLinkList[1])
Arizona(stateLinkList[2])
Arkansas(stateLinkList[3])
California(stateLinkList[4])    
Colorado(stateLinkList[5])
Connecticut(stateLinkList[6])
Delaware(stateLinkList[7])  
Florida(stateLinkList[8])  
Georgia(stateLinkList[9])
Hawaii(stateLinkList[10])
Idaho(stateLinkList[11])
Illinois(stateLinkList[12])
Indiana(stateLinkList[13])
Iowa(stateLinkList[14])
Kansas(stateLinkList[15])
Kentucky(stateLinkList[16])
Louisiana(stateLinkList[17])
Maine(stateLinkList[18])
Maryland(stateLinkList[19])
Massachusetts(stateLinkList[20])
Michigan(stateLinkList[21])
Minnesota(stateLinkList[22])
Mississippi(stateLinkList[23])
Missouri(stateLinkList[24])


Montana(stateLinkList[25])
Nebraska(stateLinkList[26])
Nevada(stateLinkList[27])
New_Hampshire(stateLinkList[28])
New_Jersey(stateLinkList[29])
New_Mexico(stateLinkList[30])
New_York(stateLinkList[31])
North_Carolina(stateLinkList[32])
North_Dakota(stateLinkList[33])
Ohio(stateLinkList[34])
Oklahoma(stateLinkList[35])
Oregon(stateLinkList[36])
Pennsylvania(stateLinkList[37])
Rhode_Island(stateLinkList[38])
South_Carolina(stateLinkList[39])
South_Dakota(stateLinkList[40])
Tennessee(stateLinkList[41])
Texas(stateLinkList[42])
Utah(stateLinkList[43])
Vermont(stateLinkList[44])
Virginia(stateLinkList[45])
Washington(stateLinkList[46])
West_Virginia(stateLinkList[47])
Wisconsin(stateLinkList[48])
Wyoming(stateLinkList[49])

American_Samoa(territoryLinkList[0])
Guam(territoryLinkList[1])
Puerto_Rico(territoryLinkList[2])
United_States_Virgin_Islands(territoryLinkList[3])

print(totalCount)
browser.quit()
 

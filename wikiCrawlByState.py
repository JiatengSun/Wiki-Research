from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
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
        if val != None and ("https://en.wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Hank_Aaron')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Delmon_Young')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
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
        if val != None and ("https://en.wikipedia.org/wiki/" in val) : 
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
        if val != None and ("https://en.wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Joey_Lauren_Adams')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Roger_L._Worsley')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
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
        if val != None and ("https://en.wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/12th_Planet_(musician)')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Steve_Young')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
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
        if val != None and ("https://en.wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Amy_Adams')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/James_Q._Wilson')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
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
        if val != None and ("https://en.wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Christopher_Abbott')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Ruth_Madoff')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
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
        if val != None and ("https://en.wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Wilbur_L._Adams')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Aleksandra_Ziolkowska-Boehm')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    return

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
        if val != None and ("https://en.wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/2_Chainz')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Yung_Joc')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
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
        if val != None and ("https://en.wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Brian_Adams_(wrestler)')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Zhang_Xueliang')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
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
        if val != None and ("https://en.wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/William_Agee')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Norma_Zimmer')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
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
        if val != None and ("https://en.wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Emma_Abbott')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Tony_Zych')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
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
        if val != None and ("https://en.wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Squire_Boone')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Homer_Van_Meter')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
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
        if val != None and ("https://en.wikipedia.org/wiki/" in val) : 
            cleanLinks.append(val)
    peopleLinks = []
    startIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Dudley_W._Adams')
    endIndex = cleanLinks.index('https://en.wikipedia.org/wiki/Larry_Zox')
    for i in range(startIndex,endIndex+1):
        peopleLinks.append(cleanLinks[i])
    print(peopleLinks)
    print(len(cleanLinks))
    return

#MAIN PROGRAM
browser.get('https://en.wikipedia.org/wiki/Lists_of_Americans')
bodyContent = browser.find_element_by_css_selector("div[id='bodyContent']")
allBlocks = bodyContent.find_elements_by_css_selector("div[class='div-col columns column-width']")
stateBlock = allBlocks[1]
stateList = stateBlock.find_elements_by_css_selector("li")
stateNameList = [i.text for i in stateList]
stateLinkList = [i.find_element_by_css_selector("a").get_attribute('href') for i in stateList]


#Alabama(stateLinkList[0])
#Alaska(stateLinkList[1])
#Arizona(stateLinkList[2])
#Arkansas(stateLinkList[3])
#California(stateLinkList[4])    
#Colorado(stateLinkList[5])
#Connecticut(stateLinkList[6])
#Delaware(stateLinkList[7])  
#Florida(stateLinkList[8])  
#Georgia(stateLinkList[9])
#Hawaii(stateLinkList[10])
#Idaho(stateLinkList[11])
#Illinois(stateLinkList[12])
#Indiana(stateLinkList[13])
Iowa(stateLinkList[14])
browser.quit()
 
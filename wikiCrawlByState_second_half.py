'''
chang edited

Montana - Wyoming;
puerto rico;
United States Virgin Islands.
'''

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
browser = webdriver.Chrome('/Users/XuChang/Downloads/wiki/chromedriver', chrome_options=chrome_options)
results = [] #as objects of person
population_per_state = []
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
    global counter
    counter += sub_counter

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
    global counter
    counter += sub_counter
    
def test_ul_state(url, state):
    print('----------', state, '----------')
    browser.get(url)
    sections = browser.find_elements_by_css_selector('ul')
    for i in range(0, 200):        
#    for i in temp_indices:        
        print(i, sections[i].find_element_by_tag_name('li').text)
#        break
        

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
 
    '''!!!'''
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
 
    '''!!!'''
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
 
    '''!!!'''
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


'''!!!'''
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


browser.get('https://en.wikipedia.org/wiki/Lists_of_Americans')

content_blocks = browser.find_elements_by_css_selector("div[class='div-col columns column-width']")
'''
in content_blocks:
[0] is "By ethnicity or place of origin";
[1] is "By U.S. state";
[2] is "Territories (insular areas)".

'''
#print(content_blocks[1].text)
a_elements = []
elements = content_blocks[1].find_elements_by_tag_name("a")
other_elements = content_blocks[2].find_elements_by_tag_name("a")
#print(elements[0].get_attribute('title'))

'''->a small test to make sure this is the right section'''
if (elements[0].text!='Alabama'):
    print('wrong content_block')
    browser.quit()
    exit();
'''<-'''
    
for el in elements:
    a_elements.append(el)

    

links = [el.get_attribute('href') for el in a_elements]
other_links = [el.get_attribute('href') for el in other_elements]
    
state_names = [el.text for el in a_elements]



counter = 0
#num = 0

skipWords = ["_Americans", "List_of", "Category", "Special", "Main_Page", "Portal", "Help", "Contact_us", "Wikipedia:", "Template:", "Template_talk:"]

#print(links)
'''->testing Montana:'''
#browser.get(chang_links[0])
#persons = browser.find_elements_by_css_selector("span[class='vcard']")
#print(persons[0].text)
#person = persons[0].find_element_by_tag_name("a") #note i put "element" here, not "elements".
#print(person.get_attribute('href'))
#for x in persons:
#    print(str(count), persons[count].text)
#    counter+=1
'''<-define table?'''
'''->testing ul:'''

#browser.get(chang_links[1])
#
#persons = browser.find_elements_by_css_selector('ul')
##print(persons[0].get_attribute('class')=='')
#for i in range(0,18):
#    print(persons[i].find_element_by_tag_name('li').get_attribute('innerHTML'))
#
##for x in persons:
##    person = x.find_element_by_tag_name('li')
##    p = x.find_element_by_tag_name("a")
##    print(p.get_attribute('innerHTML'))
'''<-'''

'''->testing Nebraska:'''
#browser.get(chang_links[1])
#
#persons = browser.find_elements_by_css_selector("li")
##print(persons[0].get_attribute('class')=='')
##print(persons[0].text)
#
#for x in persons:
#    if x.get_attribute('class')!='' or x.get_attribute('id')!='' or x.get_attribute('style')!='':
#        continue
#    person = x.find_element_by_tag_name("a") #getting the first link in this li
#    if person.text == '' or 'Category:' in person.get_attribute('href') or 'en.wikipedia.org' not in person.get_attribute('href') or '_Nebraska' in person.get_attribute('href') or 'List_of_:' in person.get_attribute('href') or 'Lists_of_:' in person.get_attribute('href'):
#        continue
#
#
#    if 
#    print(person.text, '[]', person.get_attribute('href'))
#    print('----------')
##    break
'''<-'''




Montana(links[25])
Nebraska(links[26])
Nevada(links[27])
New_Hampshire(links[28])
New_Jersey(links[29])
New_Mexico(links[30])
New_York(links[31])
North_Carolina(links[32])
North_Dakota(links[33])
Ohio(links[34])
Oklahoma(links[35])
Oregon(links[36])
Pennsylvania(links[37])
Rhode_Island(links[38])
South_Carolina(links[39])
South_Dakota(links[40])
Tennessee(links[41])
Texas(links[42])
Utah(links[43])
Vermont(links[44])
Virginia(links[45])
Washington(links[46])
West_Virginia(links[47])
Wisconsin(links[48])
Wyoming(links[49])

American_Samoa(other_links[0])
Guam(other_links[1])
Puerto_Rico(other_links[2])
United_States_Virgin_Islands(other_links[3])


print('total is', str(counter))

'''
idx = 0
for l in chang_links:
    sub_counter = 0 #for counting people in this state

    #if tables:
    browser.get(l)
    persons = browser.find_elements_by_css_selector("span[class='vcard']")
    for p in persons:
        person = p.find_element_by_tag_name("a") #note i put "element" here, not "elements".
        results.append(person)
        sub_counter += 1
    print(chang_state_names[idx], 'has', str(sub_counter), 'people')
    counter += sub_counter
    
    #if lists:
   
    idx+=1
print('u.s. has', str(counter), 'people')
'''

'''
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
'''
    
    
    
    
browser.quit()
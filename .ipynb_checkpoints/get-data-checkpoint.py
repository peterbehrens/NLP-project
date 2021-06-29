import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions


opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)

def getSnippet(search_term):


        browser.get("https://www.bing.com/search?q=" + search_term)
        
        try:
                snippet = browser.find_element_by_xpath("//div[contains(@class, 'b_caption hasdl')]")
                snippet = snippet.text
                snippet = ' '.join(snippet.split("\n")[1:])
                print(snippet)
                print(search_term)
                return snippet
        except:
                return 0




import csv 
with open ("list.csv") as csvfile: 
        reader = csv.reader(csvfile, delimiter=";")
        your_lst = list(reader)



def writeSheet(csvData):
        import csv
        with open('output_1s.csv', 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter="\t")
                csvData[0] = csvData[0] +["Snippet"]
                writer.writerow(csvData[0])
                for row in csvData[1:]:
                        snippet = getSnippet(row[6])
                        if(snippet==0):
                                snippet = "NaN"
                                writer.writerow(row+[snippet])
                                print(row + [snippet])
                                #time.sleep(3)
                        else: 
                                writer.writerow(row+[snippet])
                                print(row + [snippet])
                                #time.sleep(3)                               
                
                        
                             
                        

#writeSheet(your_lst)
test = getSnippet("www.biersack.de")
print(test)

browser.close()


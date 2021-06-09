from random import *
import time



def getSnippet(search_term):

        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver import FirefoxOptions


        opts = FirefoxOptions()
        opts.add_argument("--headless")
        browser = webdriver.Firefox(options=opts)
        browser.get("https://www.bing.com/search?q=" + search_term)

        try:
                snippet = browser.find_element_by_xpath("//div[contains(@class, 'b_caption hasdl')]")
                snippet = snippet.text
                browser.close()
                return snippet
        except:
                return 0




import csv 
with open ("list.csv") as csvfile: 
        reader = csv.reader(csvfile, delimiter=";")
        your_lst = list(reader)



def writeSheet(csvData):
        import csv
        with open('test.csv', 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=";")
                csvData[0] = csvData[0] +["Snippet"]
                writer.writerow(csvData[0])
                for row in csvData[1:]:
                        snippet = getSnippet(row[6])
                        if(snippet==0):
                                test = bissiTest(row[6])
                                if(test!=0):
                                         writer.writerow(row+[snippet])
                                         print(row)
                                         time.sleep(3)
                        else: 
                                         writer.writerow(row+[snippet])
                                         print(row)
                                         time.sleep(3)                               
                
                        
def bissiTest(keyword):
        print("------------------------Testmodus-------------------------")
        returnSnippet = 0
        for test in range(1,8):
                snippet = getSnippet(keyword)
                if(snippet!=0):
                        print("------------------------Retreived Data-------------------------")
                        returnSnippet = snippet
                        break
                else:
                        time.sleep(randint(3,20))
        if (returnSnippet!=""): 
                return snippet
        else:
                return 0
                print("------------------------Test denied-------------------------")
                             
                        

writeSheet(your_lst)
test = getSnippet("www.biersack.de")
print(test)



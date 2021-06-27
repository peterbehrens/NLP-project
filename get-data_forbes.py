import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions
from selenium.common.exceptions import TimeoutException

import pandas as pd

opts = FirefoxOptions()
opts.add_argument("--headless")

global browser
browser = webdriver.Firefox(options=opts)
browser.set_page_load_timeout(2)

def open_new_browser():
        global browser
        browser = webdriver.Firefox(options=opts)


def getSnippet(search_term):
        
        global browser


        try:
                browser.get("https://www.bing.com/search?q=" + search_term + " loc:de language:de")
        except TimeoutException as t:
                print(f"Timeout exception: {str(t)}")
                snippet = 0
                browser.close()

                open_new_browser()
                
                return snippet
        except:
                snippet = 0
                return snippet
        
        #snippet = browser.find_element_by_xpath("//div[contains(@class, 'b_caption hasdl')]")
        snippet = browser.find_elements_by_xpath("//div[contains(@class, 'b_caption hasdl')]")
        print(search_term)
        if len(snippet) == 0:
                snippet = browser.find_elements_by_xpath("//div[contains(@class, 'b_snippet')]")
                try:
                        snippet = snippet[0].find_element_by_tag_name("p")
                        snippet = str(snippet.get_attribute("textContent"))
                except:
                        print(f"No <p> for {search_term}")
                        if  len(snippet) > 0:
                                snippet = str(snippet[0].get_attribute("textContent"))
                        else:
                                snippet = 0
        else:
                snippet = str(snippet[0].get_attribute("textContent"))



        return snippet





your_df = pd.read_csv("Forbes Top2000.csv", ";")



def writeSheet(your_df):
        global counter
        counter = 0
        global nan
        nan = 0
        def add_snippet(Company):
                snippet = getSnippet(Company)
                global counter
                global nan

                print(snippet)

                if(snippet==0 or snippet == " " or snippet == ""):
                        snippet = "NaN"
                        #print(row + [snippet])
                        time.sleep(2)
                        nan += 1
                        print(f"Total: {counter+nan} Snippets: {counter}, NaNs: {nan}, %: {nan/(counter+nan) * 100}")                            

                        return snippet
                else: 
                        #print(row + [snippet])
                        time.sleep(2)
                        counter += 1
                        print(f"Total: {counter+nan} Snippets: {counter}, NaNs: {nan}, %: {nan/(counter+nan) * 100}")                            

                        return snippet
        
        your_df['Snippet'] = your_df.apply(lambda row : add_snippet(row["Company"]), axis = 1)

        return your_df





        # with open('output_forbes.csv', 'w') as csvfile:
        #         writer = csv.writer(csvfile, delimiter="\t")
        #         csvData[0] = csvData[0] +["Snippet"]
        #         writer.writerow(csvData[0])
        #         for row in csvData[1:]:
        #                 snippet = getSnippet(row[1])
        #                 #print(snippet)
        #                 if(snippet==0 or snippet == " " or snippet == ""):
        #                         snippet = "NaN"
        #                         writer.writerow(row+[snippet])
        #                         #print(row + [snippet])
        #                         time.sleep(2)
        #                         nan += 1
        #                 else: 
        #                         writer.writerow(row+[snippet])
        #                         #print(row + [snippet])
        #                         time.sleep(2)   
        #                         counter += 1

        #                         if counter%20 == 0:
        #                                 browser.close()
        #                                 browser = webdriver.Firefox(options=opts)
                
                        
                             
                        

writeSheet(your_df).to_csv("/media/stephan/SD1/Studium/DHBW/6. Semester/NLP/NLP-project/output_forbes.csv", "\t")
#print(getSnippet('Agricultural Bank of China'))



browser.close()


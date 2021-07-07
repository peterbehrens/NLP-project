import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions
from selenium.common.exceptions import TimeoutException

import pandas as pd


class Crawler:

    def __init__(self):

        self.opts = FirefoxOptions()
        self.opts.add_argument("--headless")

        self.browser = webdriver.Firefox(options=self.opts)
        self.browser.set_page_load_timeout(2)
        self.open_new_browser()

    def open_new_browser(self):
            self.browser = webdriver.Firefox(options=self.opts)


    def getSnippet(self, search_term):
            # Method to get Snippet from Bing

            try:
                    self.browser.get("https://www.bing.com/search?q=" + search_term + " loc:de language:de")
            except TimeoutException as t:
                    print(f"Timeout exception: {str(t)}")
                    snippet = 0
                    self.browser.close()

                    self.open_new_browser()
                    
                    return snippet
            except:
                    snippet = 0
                    return snippet
            
            #snippet = browser.find_element_by_xpath("//div[contains(@class, 'b_caption hasdl')]")

            #find Snippet on HTML page of search result
            snippet = self.browser.find_elements_by_xpath("//div[contains(@class, 'b_caption hasdl')]")
            #print(search_term)

            #If no Snippet has been found look for Alternatives 
            if len(snippet) == 0:
                    snippet = self.browser.find_elements_by_xpath("//div[contains(@class, 'b_snippet')]")
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

    def close_browser(self):
        self.browser.close()






def writeSheet(your_df):
        #Add Snippets to DF and save to csv
        global counter
        counter = 0
        global nan
        nan = 0
        crawler = Crawler()

        def add_snippet(crawler, Company):
                snippet = crawler.getSnippet(Company)
                global counter
                global nan

                print(snippet)

                #check snippet of company, if it's empty add "NaN"
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
        
        your_df['Snippet'] = your_df.apply(lambda row : add_snippet(crawler, row["Company"]), axis = 1)

        crawler.close_browser()
        return your_df
        
                        
#your_df = pd.read_csv("Forbes Top2000.csv", ";")

#writeSheet(your_df).to_csv("/media/stephan/SD1/Studium/DHBW/6. Semester/NLP/NLP-project/output_forbes.csv", "\t")


from bs4 import BeautifulSoup
import requests

class RockawaySurfScraper:

    def __init__(self):
        #Surf Captain Website for surf summary
        url = 'https://surfcaptain.com/forecast/rockaway-new-york'
        page = requests.get(url)
        surf_summary_html_ele_id = 'fcst-current-title'
        surf_summary_html_ele_type = 'h1'
        #Grab the 'soup' of html from the website
        self.soup = BeautifulSoup(page.text, 'html')
        self.summary = self.retrieve_element(surf_summary_html_ele_type, surf_summary_html_ele_id)
        self.output_summary()

    def retrieve_element(self, element_type:str, element_id:str):
        """
        Returns a section of the html from website,based on the type and id of the html element

        Args:
            element_type (str): html code for the element (i guess), don't really know what's its called
            element_id (str): id for the element in the html 'soup' 
        """
        return(self.soup.find(element_type, id=element_id))
        

    def output_summary(self):
        full_summary = []
        for ele in self.summary.contents:
            full_summary.append(ele.text.strip())
        
        self._surf_output_summary = " ".join(full_summary)

    @property
    def surf_summary(self):
        return self._surf_output_summary
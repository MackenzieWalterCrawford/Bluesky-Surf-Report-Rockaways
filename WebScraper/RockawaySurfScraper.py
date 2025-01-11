class RockawaySurfScraper:

    def __init__(self):
        url = 'https://surfcaptain.com/forecast/rockaway-new-york'
        page = requests.get(url)
        self.soup = BeautifulSoup(page.text, 'html')

    def retrieve_summary(self):
        self.summary = self.soup.find('h1', id="fcst-current-title")

    def output_summary(self):
        full_summary = []
        for ele in self.summary.contents:
            print(ele.text.strip())
            full_summary.append(ele.text.strip())
        
        self.surf_output_summary = " ".join(full_summary)


    def get_surf_summary(self):
        return self.surf_output_summary
import cloudscraper
from bs4 import BeautifulSoup
from time import sleep


class KickAss():
    def __init__(self, url):
        self.url = url

        self.main_function()

    def main_function(self):    
        self.scrap_content()
        self.data_scrap()
        self.colect_data()
        

    def scrap_content(self):
        scraper = cloudscraper.create_scraper()
        self.scrap = scraper.get(self.url).text


    def data_scrap(self):
        name ={"class": "cellMainLink"}
        mag = {"title": "Torrent magnet link"}
        size = {"class": "nobr center"}
        seed = {"class": "green center"}
        cat = {"id": "cat_12975568"}

        self.seeds = list()
        self.size = list()
        self.title = list()
        self.magnet = list()
        self.category = list()

        bs = BeautifulSoup(self.scrap, "lxml")

        self.title = bs.findAll("a", attrs=name)
        self.magnet = bs.findAll("a", attrs=mag)
        self.size = bs.findAll(attrs=size)
        self.seeds = bs.findAll(attrs=seed)
        self.category = bs.findAll(attrs=cat)


    def colect_data(self):
        title = list() 
        magnet = list()
        size = list() 
        seeds = list()
        category = list()
        
        for t in self.title:
            title.append(t.text)

        for m in self.magnet:
            magnet.append(m["href"])

        for sz in self.size:
            size.append(sz.text)

        for se in self.seeds:
            seeds.append(se.text)
            print(se.text)
        
        for cat in self.category:
            category.append(cat.text)

        return title, magnet, size, seeds, category


def data_collector(url):
    
    title = list() 
    magnet = list()
    size = list() 
    seeds = list()
    category = list()
        
    for i in range(1):            
        url = f"{url}/{i +1 }/"

        k = KickAss(url)
        t, m, sz, sd, cat = k.colect_data()
        
        title.extend(t)
        magnet.extend(m)
        size.extend(sz)
        seeds.extend(sd)
        category.extend(cat)
    
    return title, magnet, size, seeds, category


def json_maker(title, magnet, size, seeds, category):
    jsonfile = []

    for i in range(len(title)):
        try:
            jsonfile.append({
                    "title": title[i],
                    "size": size[i],
                    "seeds": int(seeds[i]),
                    "magnet": magnet[i],
                    "category": category[i]
            })
        except:
            print(title[i])

    return jsonfile


def returning_json(url):
    title, magnet, size, seeds, category = data_collector(url)
    jsonfile = json_maker(title, magnet, size, seeds, category)
    return jsonfile

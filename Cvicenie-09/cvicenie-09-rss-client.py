# RSS client

import urllib.request 
# https://docs.python.org/3/library/urllib.request.html

import xml.etree.ElementTree as ET

import tkinter as tk

def getRssText(paURL):    
    returnText = ''
    raw_page = urllib.request.urlopen(paURL)
    # Open the URL url, which can be either a string or a Request object.

    page = raw_page.read()

    root = ET.fromstring(page)
    #root = ET.fromstring(urllib.request.urlopen(paURL).read())

    for channel in root:
        for item in channel:
            if item.tag == "title":
                returnText += "Nadpis: " + item.text + "\n"
            if item.tag == "description":
                returnText += "Popis: {}\n".format(item.text) 
            if item.tag == "item":
                for i in item:
                    if i.tag == "title":
                        returnText += "Nadpis itemu: " + i.text + "\n"
                    if i.tag == "description":
                        returnText += "  Popis itemu: {}\n".format(i.text) 
                    if i.tag == "pubDate":
                        returnText += "  Datum itemu: {}\n".format(i.text) 
    
    return returnText

def setWindow(self):
    self.title("RSS citacka v Pythone")
    self.geometry("800x600+100+100")
    self.resizable(False, False)

    labelUrl = tk.Label(self, text = "URL: ")
    labelUrl.grid(row = 0, column = 0, sticky = "w", padx = 20)

    entryUrl = tk.Entry(self)
    entryUrl.grid(row = 1, column = 0, padx = 20, ipadx = "150", sticky = "w")

    rss_url1 = "http://feeds.bbci.co.uk/news/world/europe/rss.xml"
    rss_url2 = "https://www.slovensko.sk/sk/rss/oznamy"
    rss_url3 = "https://www.sme.sk/rss-title"
    entryUrl.insert(0, rss_url1)

    outputText = tk.Text(self)
    outputText.grid(row = 2, column = 0, sticky = "w", padx = 20)

    buttonSubmit = tk.Button(self, text = "Stiahni", command = lambda:outputText.insert(tk.END, getRssText(entryUrl.get())))
    buttonSubmit.grid(row = 1, column = 1, padx = 20)



rss_url1 = "http://feeds.bbci.co.uk/news/world/europe/rss.xml"
rss_url2 = "https://www.slovensko.sk/sk/rss/oznamy"
rss_url3 = "https://www.sme.sk/rss-title"
# print(getRssText(rss_url3))


hlavna_obrazovka = tk.Tk()
setWindow(hlavna_obrazovka)
hlavna_obrazovka.mainloop()

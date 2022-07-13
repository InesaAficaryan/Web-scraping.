'''
Implemented by Inesa Aficaryan.

Description:
        Script get minimum prices for given product from sas.am web page

Dependencies & Supported Versions:

    Python 3.8.x

Libraries:

    os, re, sys, json, logging, requests, argparse, configparser, enum, bs4, lxml.html, urllib.parse, url_normalize

Revision:

    v0.1 alpha (15/04/2022)

Usage: python3 sas.py -c config_file

'''



try:
    import os
    import sys
    import logging
    import requests
    from bs4 import BeautifulSoup
    import lxml
    import numpy as np
except ImportError as exception:
    print("%s - Please install the necessary libraries." % exception)
    sys.exit(1)



products = { 'bread' : "khleb/", 'bakery': 'vypechka/', 'pastry':"pirozhnoe/",'cakes':"tort", 
        'eastern sweets and gata':"vostochnye_sladosti_gata/", 'coffee':"kofe2564/", 'tea':"chay/", 'poultry':"ptitsa2/",
        'ice': "led/", 'vegetables,fruits,berries':"frukty_ovoshchi_yagody/",
        "Cholesterol lowering products": "produkty_ponizhayushchie_kholesterin1/", 
        "Products low in and with no cholesterol":"produkty_bez_soderzhaniya_kholesterina/", "butter":"slivochnoe/",
        "margarine":"slivochnoe/","yoghurts":"yogurty_i_slivki/","Cheese":"syr/","milk":"moloko/","non-dairy drink":"moloko",
        "condensed milk":"sgushchennoe_moloko/","kefir":"kefir/","milk, non-dairy drink":"moloko/","tan, okroshka":"tan_okroshka/",
        "matsoun":"matsoni/","sour cream":"smetana/","eggs": "yaytso/","curd products":"tvorozhnye_izdeliya/",
        "yoghurts, creams":"yogurty_i_slivki/","cheese":"syr","cream":"drugie_molochnye_produkty/","wine":"vino/",
        "vermouth":"vermut/","champaign, sparkling wine":"shampanskoe_igristoe_vino/",
        "smoke free products and accessories": "bez_dyma_tovary_i_aksessuary/","lighter, accessories, charcoal":"aksessuary/",
        "cigar, cigarillo, tobacco":"sigara_sigarilla/","cigarettes":"sigareta","electric pods":"electsig/","honey":"med_med",
        "nuts":"orekhi/","dried fruits":"assorti_suhofrukty/","pastry":"konditerskie_izdeliya/",
        "chips, seeds, flakes":"chipsy_semechki_popkorn/","beer snacks":"pivnik_dzherki/",
        "chocolates, cream":"shokoladnye_konfety_krem/", "chewing gum, candies":"zhevatelnaya_rezinka_konfety/",
        "smoked meat products":"kopchenye_myasoprodukty/","basturma sudjuk":"basturma_i_sudzhuk/",
        "meat delicacies":"myasnoy_delikates/","cut meat":"myasnaya_narezka/","fresh meat":"svezhee_myaso/",
        "boiled meat products":"varenye_myasoprodukty/"}



def solution():

    choice = input("Choose what you want: ") 

    if choice in products:
        print("Your choice is approved") 
    else:
        print("This product is currently out of stock")
        sys.exit(1)
    value = products[choice]  
    response = requests.get('https://www.sas.am/en/catalog/' + str(value))
    soup = BeautifulSoup(response.text, 'lxml')  
      
    prod_name = soup.find_all('div', class_ = 'product__name hidden-sm')
    prod_price = soup.find_all('span', class_ = 'price__text')
    prod_and_price = {}

    for name, price in zip(prod_name, prod_price):
        prod_and_price[name.text] = int(price.text.replace("\xa0", " ").replace(" AMD", "").replace(" ", ""))       
 
       
    min_value = min(prod_and_price.values()) 
    Key = 0

    for key, value in prod_and_price.items():
             if min_value == value:
                Key = key 

    print("The product with the lowest price is: " +str(Key)+ ' ' + str(min_value))
        
        
solution()        
        
        
        
        
        
        

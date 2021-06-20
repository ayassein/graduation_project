import requests as rq
import pandas as pd



CNN_URL = ('https://money.cnn.com/data/markets/')

from bs4 import BeautifulSoup as bs
CNN_page = rq.get(CNN_URL).text
CNN_soup = bs(CNN_page,'html.parser')
CNN_results_1  = CNN_soup.find_all('li', attrs={'class':'row first'})


CNN_records_1 = []
for result in CNN_results_1:
    company = result.find_all('span')[0].contents[-1]
    price = result.find_all('span')[1].text
    change = result.find_all('span')[2].text
    CNN_records_1.append((company, price, change))
df_0 = pd.DataFrame(CNN_records_1, columns=['company', 'price', 'change'])
with open('CNN.csv','w') as file:
    file.write('Most Popular Stocks\n')
    df_0.to_csv(file,index = False,line_terminator='\n',encoding='utf-8')

CNN_results_2  = CNN_soup.find_all('li', attrs={'class':'row'})
row = CNN_results_2[5:10]

CNN_records_2 = []
for result in row:
    company = result.find_all('span')[0].contents[-1]
    price = result.find_all('span')[1].text
    change = result.find_all('span')[5].text
    CNN_records_2.append((company, price, change))

df_1 = pd.DataFrame(CNN_records_2, columns=['company', 'price', 'change'])
with open('CNN.csv','a') as file:
    file.write('Key Stats\n')
    df_1.to_csv(file, index = False,line_terminator='\n',encoding='utf-8')
 
    
    
    
APPLE_INC_URL = ('https://money.cnn.com/quote/quote.html?symb=AAPL')

APPLE_page = rq.get(APPLE_INC_URL).text

APPLE_soup = bs(APPLE_page,'html.parser')
APPLE_results_Trading  = APPLE_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnLeft'})


Todays_Trading_results = APPLE_results_Trading[0]
my_list = [0,2,4,6,8,10]
APPLE_records_Trading=[]
for i in my_list:
    Todays_Trading = Todays_Trading_results.find_all('td')[i].text,Todays_Trading_results.find_all('td')[i+1].text
    APPLE_records_Trading.append((Todays_Trading))
    

df = pd.DataFrame(APPLE_records_Trading, columns=['Status','Price'])
with open('APPLE.csv','w') as file:
    file.write('Todays Trading\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8')

APPLE_results_Growth_and_Valuation  = APPLE_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnRight'})

Growth_and_Valuation_results = APPLE_results_Growth_and_Valuation[0]
my_list = [0,2,4,6,8,10]
APPLE_records_Growth_and_Valuation=[]
for i in my_list:
    Growth_and_Valuation = Growth_and_Valuation_results.find_all('td')[i].text,Growth_and_Valuation_results.find_all('td')[i+1].text
    APPLE_records_Growth_and_Valuation.append((Growth_and_Valuation))
    
df = pd.DataFrame(APPLE_records_Growth_and_Valuation, columns=['Status','Price'])
with open('APPLE.csv','a') as file:
    file.write('Growth and Valuation\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8')
    
APPLE_results_Competitors = APPLE_soup.find_all('div', attrs={'class':'clearfix'})

Competitors_results = APPLE_results_Competitors[15]
table_list = [0,3,6,9]
head_list = [0]
APPLE_records_Competitors=[]
for j in head_list:
        Competitors_head = "      ",Competitors_results.find_all('th')[j+1].text,Competitors_results.find_all('th')[j+2].text
        APPLE_records_Competitors.append((Competitors_head))
for i in table_list:
    Competitors = Competitors_results.find_all('span')[i].text
    Competitors_1 = Competitors_results.find_all('span')[i+1].text
    Competitors_2= Competitors_results.find_all('span')[i+2].text
    APPLE_records_Competitors.append((Competitors,Competitors_1,Competitors_2))
    
df = pd.DataFrame(APPLE_records_Competitors)
with open('APPLE.csv','a') as file:
    file.write('Competitors\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8',header = False)
    
APPLE_results_Financials  = APPLE_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnRight'})

Financials_results = APPLE_results_Financials[1]
my_list = [0,2,4,6,8]
APPLE_records_Financials=[]
for i in my_list:
    Financials = Financials_results.find_all('td')[i].text,Financials_results.find_all('td')[i+1].text
    APPLE_records_Financials.append((Financials))

CITIGRUP_Inc_URL = ('https://money.cnn.com/quote/quote.html?symb=C')

CITIGRUP_page = rq.get(CITIGRUP_Inc_URL).text

CITIGRUP_soup = bs(CITIGRUP_page,'html.parser')
CITIGRUP_results_Trading  = CITIGRUP_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnLeft'})


Todays_Trading_results = CITIGRUP_results_Trading[0]
my_list = [0,2,4,6,8,10]
CITIGRUP_records_Trading=[]
for i in my_list:
    Todays_Trading = Todays_Trading_results.find_all('td')[i].text,Todays_Trading_results.find_all('td')[i+1].text
    CITIGRUP_records_Trading.append((Todays_Trading))
    

df = pd.DataFrame(CITIGRUP_records_Trading, columns=['Status','Price'])
with open('CITIGRUP.csv','w') as file:
    file.write('Todays Trading\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8')

CITIGRUP_results_Growth_and_Valuation  = CITIGRUP_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnRight'})

Growth_and_Valuation_results = CITIGRUP_results_Growth_and_Valuation[0]
my_list = [0,2,4,6,8,10]
CITIGRUP_records_Growth_and_Valuation=[]
for i in my_list:
    Growth_and_Valuation = Growth_and_Valuation_results.find_all('td')[i].text,Growth_and_Valuation_results.find_all('td')[i+1].text
    CITIGRUP_records_Growth_and_Valuation.append((Growth_and_Valuation))
    
df = pd.DataFrame(CITIGRUP_records_Growth_and_Valuation, columns=['Status','Price'])
with open('CITIGRUP.csv','a') as file:
    file.write('Growth and Valuation\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8')
    
CITIGRUP_results_Competitors = CITIGRUP_soup.find_all('div', attrs={'class':'clearfix'})

Competitors_results = CITIGRUP_results_Competitors[15]
table_list = [0,3,6,9]
head_list = [0]
CITIGRUP_records_Competitors=[]
for j in head_list:
        Competitors_head = "      ",Competitors_results.find_all('th')[j+1].text,Competitors_results.find_all('th')[j+2].text
        CITIGRUP_records_Competitors.append((Competitors_head))
for i in table_list:
    Competitors = Competitors_results.find_all('span')[i].text
    Competitors_1 = Competitors_results.find_all('span')[i+1].text
    Competitors_2= Competitors_results.find_all('span')[i+2].text
    CITIGRUP_records_Competitors.append((Competitors,Competitors_1,Competitors_2))
    
df = pd.DataFrame(CITIGRUP_records_Competitors)
with open('CITIGRUP.csv','a') as file:
    file.write('Competitors\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8',header = False)
    
CITIGRUP_results_Financials  = CITIGRUP_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnRight'})

Financials_results = CITIGRUP_results_Financials[1]
my_list = [0,2,4,6,8]
CITIGRUP_records_Financials=[]
for i in my_list:
    Financials = Financials_results.find_all('td')[i].text,Financials_results.find_all('td')[i+1].text
    CITIGRUP_records_Financials.append((Financials))
    
df = pd.DataFrame(CITIGRUP_records_Financials, columns=['Status','Price'])
with open('CITIGRUP.csv','a') as file:
    file.write('Financials\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8')
    
    
General_Electric_Co_URL = ('https://money.cnn.com/quote/quote.html?symb=GE')

General_Electric_Co_page = rq.get(General_Electric_Co_URL).text

GENERAL_ELECTRIC_soup = bs(General_Electric_Co_page,'html.parser')
GENERAL_ELECTRIC_results_Trading  = GENERAL_ELECTRIC_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnLeft'})


Todays_Trading_results = GENERAL_ELECTRIC_results_Trading[0]
my_list = [0,2,4,6,8,10]
GENERAL_ELECTRIC_records_Trading=[]
for i in my_list:
    Todays_Trading = Todays_Trading_results.find_all('td')[i].text,Todays_Trading_results.find_all('td')[i+1].text
    GENERAL_ELECTRIC_records_Trading.append((Todays_Trading))
    

df = pd.DataFrame(GENERAL_ELECTRIC_records_Trading, columns=['Status','Price'])
with open('GENERAL_ELECTRIC.csv','w') as file:
    file.write('Todays Trading\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8')

GENERAL_ELECTRIC_results_Growth_and_Valuation  = GENERAL_ELECTRIC_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnRight'})

Growth_and_Valuation_results = GENERAL_ELECTRIC_results_Growth_and_Valuation[0]
my_list = [0,2,4,6,8,10]
GENERAL_ELECTRIC_records_Growth_and_Valuation=[]
for i in my_list:
    Growth_and_Valuation = Growth_and_Valuation_results.find_all('td')[i].text,Growth_and_Valuation_results.find_all('td')[i+1].text
    GENERAL_ELECTRIC_records_Growth_and_Valuation.append((Growth_and_Valuation))
    
df = pd.DataFrame(GENERAL_ELECTRIC_records_Growth_and_Valuation, columns=['Status','Price'])
with open('GENERAL_ELECTRIC.csv','a') as file:
    file.write('Growth and Valuation\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8')
    
GENERAL_ELECTRIC_results_Competitors = GENERAL_ELECTRIC_soup.find_all('div', attrs={'class':'clearfix'})

Competitors_results = GENERAL_ELECTRIC_results_Competitors[15]
table_list = [0,3,6,9]
head_list = [0]
GENERAL_ELECTRIC_records_Competitors=[]
for j in head_list:
        Competitors_head = "      ",Competitors_results.find_all('th')[j+1].text,Competitors_results.find_all('th')[j+2].text
        GENERAL_ELECTRIC_records_Competitors.append((Competitors_head))
for i in table_list:
    Competitors = Competitors_results.find_all('span')[i].text
    Competitors_1 = Competitors_results.find_all('span')[i+1].text
    Competitors_2= Competitors_results.find_all('span')[i+2].text
    GENERAL_ELECTRIC_records_Competitors.append((Competitors,Competitors_1,Competitors_2))
    
df = pd.DataFrame(GENERAL_ELECTRIC_records_Competitors)
with open('GENERAL_ELECTRIC.csv','a') as file:
    file.write('Competitors\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8',header = False)
    
GENERAL_ELECTRIC_results_Financials  = GENERAL_ELECTRIC_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnRight'})

Financials_results = GENERAL_ELECTRIC_results_Financials[1]
my_list = [0,2,4,6,8]
GENERAL_ELECTRIC_records_Financials=[]
for i in my_list:
    Financials = Financials_results.find_all('td')[i].text,Financials_results.find_all('td')[i+1].text
    GENERAL_ELECTRIC_records_Financials.append((Financials))
    
df = pd.DataFrame(GENERAL_ELECTRIC_records_Financials, columns=['Status','Price'])
with open('GENERAL_ELECTRIC.csv','a') as file:
    file.write('Financials\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8')



Alphabet_Inc_URL = ('https://money.cnn.com/quote/quote.html?symb=GOOGL')

Alphabet_Inc_page = rq.get(Alphabet_Inc_URL).text

ALPHABET_soup = bs(Alphabet_Inc_page,'html.parser')
ALPHABET_results_Trading  = ALPHABET_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnLeft'})


Todays_Trading_results = ALPHABET_results_Trading[0]
my_list = [0,2,4,6,8,10]
ALPHABET_records_Trading=[]
for i in my_list:
    Todays_Trading = Todays_Trading_results.find_all('td')[i].text,Todays_Trading_results.find_all('td')[i+1].text
    ALPHABET_records_Trading.append((Todays_Trading))
    

df = pd.DataFrame(ALPHABET_records_Trading, columns=['Status','Price'])
with open('ALPHABET.csv','w') as file:
    file.write('Todays Trading\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8')

ALPHABET_results_Growth_and_Valuation  = ALPHABET_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnRight'})

Growth_and_Valuation_results = ALPHABET_results_Growth_and_Valuation[0]
my_list = [0,2,4,6,8,10]
ALPHABET_records_Growth_and_Valuation=[]
for i in my_list:
    Growth_and_Valuation = Growth_and_Valuation_results.find_all('td')[i].text,Growth_and_Valuation_results.find_all('td')[i+1].text
    ALPHABET_records_Growth_and_Valuation.append((Growth_and_Valuation))
    
df = pd.DataFrame(ALPHABET_records_Growth_and_Valuation, columns=['Status','Price'])
with open('ALPHABET.csv','a') as file:
    file.write('Growth and Valuation\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8')
    
ALPHABET_results_Competitors = ALPHABET_soup.find_all('div', attrs={'class':'clearfix'})

Competitors_results = ALPHABET_results_Competitors[15]
table_list = [0,3,6,9]
head_list = [0]
ALPHABET_records_Competitors=[]
for j in head_list:
        Competitors_head = "      ",Competitors_results.find_all('th')[j+1].text,Competitors_results.find_all('th')[j+2].text
        ALPHABET_records_Competitors.append((Competitors_head))
for i in table_list:
    Competitors = Competitors_results.find_all('span')[i].text
    Competitors_1 = Competitors_results.find_all('span')[i+1].text
    Competitors_2= Competitors_results.find_all('span')[i+2].text
    ALPHABET_records_Competitors.append((Competitors,Competitors_1,Competitors_2))
    
df = pd.DataFrame(ALPHABET_records_Competitors)
with open('ALPHABET.csv','a') as file:
    file.write('Competitors\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8',header = False)
    
ALPHABET_results_Financials  = ALPHABET_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnRight'})

Financials_results = ALPHABET_results_Financials[1]
my_list = [0,2,4,6,8]
ALPHABET_records_Financials=[]
for i in my_list:
    Financials = Financials_results.find_all('td')[i].text,Financials_results.find_all('td')[i+1].text
    ALPHABET_records_Financials.append((Financials))
    
df = pd.DataFrame(ALPHABET_records_Financials, columns=['Status','Price'])
with open('ALPHABET.csv','a') as file:
    file.write('Financials\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8')

Microsoft_Corp_URL = ('https://money.cnn.com/quote/quote.html?symb=MSFT')

Microsoft_Corp_page = rq.get(Microsoft_Corp_URL).text

MICROSOFT_soup = bs(Microsoft_Corp_page,'html.parser')
MICROSOFT_results_Trading  = MICROSOFT_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnLeft'})


Todays_Trading_results = MICROSOFT_results_Trading[0]
my_list = [0,2,4,6,8,10]
MICROSOFT_records_Trading=[]
for i in my_list:
    Todays_Trading = Todays_Trading_results.find_all('td')[i].text,Todays_Trading_results.find_all('td')[i+1].text
    MICROSOFT_records_Trading.append((Todays_Trading))
    

df = pd.DataFrame(MICROSOFT_records_Trading, columns=['Status','Price'])
with open('MICROSOFT.csv','w') as file:
    file.write('Todays Trading\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8')

MICROSOFT_results_Growth_and_Valuation  = MICROSOFT_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnRight'})

Growth_and_Valuation_results = MICROSOFT_results_Growth_and_Valuation[0]
my_list = [0,2,4,6,8,10]
MICROSOFT_records_Growth_and_Valuation=[]
for i in my_list:
    Growth_and_Valuation = Growth_and_Valuation_results.find_all('td')[i].text,Growth_and_Valuation_results.find_all('td')[i+1].text
    MICROSOFT_records_Growth_and_Valuation.append((Growth_and_Valuation))
    
df = pd.DataFrame(MICROSOFT_records_Growth_and_Valuation, columns=['Status','Price'])
with open('MICROSOFT.csv','a') as file:
    file.write('Growth and Valuation\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8')
    
MICROSOFT_results_Competitors = MICROSOFT_soup.find_all('div', attrs={'class':'clearfix'})

Competitors_results = MICROSOFT_results_Competitors[15]
table_list = [0,3,6,9]
head_list = [0]
MICROSOFT_records_Competitors=[]
for j in head_list:
        Competitors_head = "      ",Competitors_results.find_all('th')[j+1].text,Competitors_results.find_all('th')[j+2].text
        MICROSOFT_records_Competitors.append((Competitors_head))
for i in table_list:
    Competitors = Competitors_results.find_all('span')[i].text
    Competitors_1 = Competitors_results.find_all('span')[i+1].text
    Competitors_2= Competitors_results.find_all('span')[i+2].text
    MICROSOFT_records_Competitors.append((Competitors,Competitors_1,Competitors_2))
    
df = pd.DataFrame(MICROSOFT_records_Competitors)
with open('MICROSOFT.csv','a') as file:
    file.write('Competitors\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8',header = False)
    
MICROSOFT_results_Financials  = MICROSOFT_soup.find_all('div', attrs={'class':'clearfix wsod_DataColumnRight'})

Financials_results = MICROSOFT_results_Financials[1]
my_list = [0,2,4,6,8]
MICROSOFT_records_Financials=[]
for i in my_list:
    Financials = Financials_results.find_all('td')[i].text,Financials_results.find_all('td')[i+1].text
    MICROSOFT_records_Financials.append((Financials))
    
df = pd.DataFrame(MICROSOFT_records_Financials, columns=['Status','Price'])
with open('MICROSOFT.csv','a') as file:
    file.write('Financials\n')
    df.to_csv(file, index = False,line_terminator='\n',sep = ',',encoding='utf-8')



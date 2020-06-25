from urllib import request
import json
import sys

#url for alpha vantage
url='https://www.alphavantage.co/query'

#My API key
API_KEY='BKBO1C16P2517EW9'

def getStockData(symbol):
    baseUrl='https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='
    end= '&apikey='+ API_KEY
    completeURL= baseUrl + symbol + end

    #opening connection
    connection= request.urlopen(completeURL)
    responseString= connection.read().decode()

    return responseString
    

def main():
    
    #Opening file to store output
    
    f=open('japi.out', 'w')
    
    #Asking user for input until enters quit
    while 1:
        stockSymbol= input('Please Enter the Stock Symbol or QUIT to quit : ').upper()
        if stockSymbol != 'QUIT':
            
            #Passing symbol to getStockData Function
            result=getStockData(stockSymbol)
            
            #prining JSON formatted respose to screen
            print(result)
            
            #converting response to python dictionary
            json_data=json.loads(result)
            pyDict=(json_data['Global Quote'])
           
            #printing price only into form
            for key,value in pyDict.items():
                if key =='05. price' :
                    stockValue = value
            data ='The Price of' + " " + stockSymbol + " " + 'is:' + " " + stockValue +'\n'
            print(data)
            f.write(data)
            print('Stock Quotes retrieved successfully')
            
        else:
            sys.exit("You Have exited the program")
        
main()


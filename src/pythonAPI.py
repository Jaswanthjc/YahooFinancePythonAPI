import requests
from bs4 import BeautifulSoup


def retrieve_data(stockname):
    """Get Stock Data.
    This function returns closing price of given stock from yahoo finance.

    Parameters:
        stockname(str): A valid stockname
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/94.0.4606.81 Safari/537.36'}
        url = f'https://ca.finance.yahoo.com/quote/{stockname}'
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        stock = {
            'stockname': stockname,
            'closing_price': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[0].text,
        }
        print(stock)
    except AttributeError:
        print("Oops!  Not a valid stockname. Please entry a valid one..")


def main():
    """Main Function."""
    userdata = input("Enter your instrument value: ")
    retrieve_data(userdata.upper())


if __name__ == "__main__":
    while True:
        main()
        if input('\nDo you want to run again? [y/n]: ') == 'y':
            continue
        else:
            break




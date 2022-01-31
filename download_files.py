import datetime
today_date = datetime.date.today()
DD = datetime.timedelta(days=90)
earlier = today_date - DD

date1 = earlier.strftime("%d-%m-%Y")
date2 = today_date.strftime("%d-%m-%Y")


def down1():
    import requests
    import pandas as pd
    baseurl = "https://www.nseindia.com/"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, ''like Gecko) ''Chrome/80.0.3987.149 Safari/537.36','accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
    session = requests.Session()
    request = session.get(baseurl, headers=headers, timeout=5)
    cookies = dict(request.cookies)
    url="https://www.nseindia.com/api/corporate-share-holdings-master?index=equities"
    data = session.get(url, headers=headers, timeout=5, cookies=cookies).json()
    keys=data[0].keys()
    df = pd.DataFrame(data,columns=keys)
    df.to_csv("CF-Shareholding-Pattern-equities-14-Jan-2022.csv",index=False)
def down2():
    import requests
    url="https://archives.nseindia.com/content/equities/EQUITY_L.csv"
    baseurl = "https://www.nseindia.com/"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, ''like Gecko) ''Chrome/80.0.3987.149 Safari/537.36','accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
    session = requests.Session()
    request = session.get(baseurl, headers=headers, timeout=5)
    cookies = dict(request.cookies)
    data1= session.get(url, headers=headers, timeout=5, cookies=cookies).text
    with open("EQUITY_L.csv","w") as f:
        f.write(data1)
def down3():
    # date1 = "28-10-2021"
    # date2 = "28-01-2022"
    url=f"https://www.nseindia.com/api/corporate-sast-reg29?index=equities&from_date={date1}&to_date={date2}&csv=true"
    import requests
    import pandas as pd
    baseurl = "https://www.nseindia.com/"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, ''like Gecko) ''Chrome/80.0.3987.149 Safari/537.36','accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
    session = requests.Session()
    request = session.get(baseurl, headers=headers, timeout=5)
    cookies = dict(request.cookies)

    data1 = session.get(url, headers=headers, timeout=5, cookies=cookies).text
    with open("CF-SAST- Reg29-14-Jan-2022.csv","w") as f:
        f.write(data1)
def down4():
    url="https://www.nseindia.com/api/corporate-pledgedata?index=equities&csv=true"

    import requests
    import pandas as pd
    baseurl = "https://www.nseindia.com/"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, ''like Gecko) ''Chrome/80.0.3987.149 Safari/537.36','accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
    session = requests.Session()
    request = session.get(baseurl, headers=headers, timeout=5)
    cookies = dict(request.cookies)

    data1 = session.get(url, headers=headers, timeout=5, cookies=cookies).text
    with open("CF-SAST-Pledged-Data-14-Jan-2022.csv","w") as f:
        f.write(data1)
def down5():

    import requests
    # date1="28-10-2021"
    # date2="28-01-2022"
    baseurl = "https://www.nseindia.com/"

    url = f"https://www.nseindia.com/api/corporates-pit?index=equities&from_date={date1}&to_date={date2}"

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, ''like Gecko) ''Chrome/80.0.3987.149 Safari/537.36','accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
    session = requests.Session()
    request = session.get(baseurl, headers=headers, timeout=5)
    cookies = dict(request.cookies)
    data_in_dict = session.get(url, headers=headers, timeout=5, cookies=cookies).json()

    import pandas as pd
    data=(data_in_dict["data"])
    df=pd.DataFrame.from_dict(data)
    df.to_csv('CF-Insider-Trading-equities-14-12-2021-to-14-01-2022.csv', index=False)
def down6():
    url="https://www1.nseindia.com/products/content/sec_bhavdata_full.csv"
    import requests
    import pandas as pd
    baseurl = "https://www.nseindia.com/"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, ''like Gecko) ''Chrome/80.0.3987.149 Safari/537.36','accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
    session = requests.Session()
    request = session.get(baseurl, headers=headers, timeout=5)
    cookies = dict(request.cookies)

    data = session.get(url, headers=headers, timeout=5, cookies=cookies).text
    with open("sec_bhavdata_full.csv","w") as f:
        f.write(data)
def delete_files():
    import os
    file_list=["CF-Shareholding-Pattern-equities-14-Jan-2022.csv","EQUITY_L.csv","CF-SAST- Reg29-14-Jan-2022.csv","CF-SAST-Pledged-Data-14-Jan-2022.csv","CF-Insider-Trading-equities-14-12-2021-to-14-01-2022.csv","sec_bhavdata_full.csv"]
    for file in file_list:
        if os.path.exists(file):
            print(f"deleting {file}")
            os.remove(file)
    print(f"all files deleted")
#calling each func
def down_all():
    delete_files()
    for i in range(1,8):
        if i==1:
            print(f"{i} start downloading")
            down1()
        if i==2:
            down2()
        if i==3:
            down3()
        if i==4:
            down4()
        if i==5:
            down5()
        if i==6:
            down6()
        if i==7:
            print("all downloaded check")
        print(f"{i} downloading completed")
down_all()
# delete_files()
#down5()

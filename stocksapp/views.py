from django.shortcuts import render
from .models import HistStocks
import requests
from django.contrib import messages
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render_to_response
from .models import Company,Indicator
from django.shortcuts import render
from collections import defaultdict
import logging
# from .models import Company
import sys
import csv
csv.field_size_limit(sys.maxsize)


def upload_csv(request):
    data = {}
    if request.method == "GET":
        return render(request, "upload_csv.html", data)
    # if not GET, then proceed

    c_part = {}

    with open('/home/rakibul/Desktop/SMAEMA/stocksapp/chunk1-part2.csv', newline='') as f_input:
        csv_input = csv.reader(f_input, skipinitialspace=True)
        for row in csv_input:  # first process the company part
            c_part[row[0]] = row
            if row[0] == 'indicator': break  # up to the indicator line
            # ok, we have the companies
            ''' companies = {(c_part['SimFin ID'][i], c_part['company'][i],
                      c_part['ticker'][i], c_part['financial year end (month)'][i], c_part['industry code'][i])

                     for i in range(1, len(c_part['SimFin ID']))}
                     print('ssssgddgdgdgd',companies)'''


        for row in csv_input:
            # now the indicator part
            print('mcmcc', row)
            date = row[0]
            print('xxxxxxxxxxxxxx', date)
            data = defaultdict(lambda: defaultdict(dict))
            #lambda: defaultdict(lambda: defaultdict(dict))

            for i in range(1, len(row)):
                data[c_part['SimFin ID'][i]][c_part['indicator'][i]] = row[i]
                #print('lllll', data)
            for i in data:
                data[i].update({'SimFin ID': i,'ticker':i, 'date': date})  # update with the date and id part
                #print('raaa', dict(data[i]))

                indicator_obj,created = Indicator.objects.get_or_create(
                    Sid=data[i]['SimFin ID'],
                    date=str(data[i]['date']),
                    EnterprizeValue=data[i]['Enterprise Value'],
                    CommonSharesOutstanding=data[i]['Common Shares Outstanding'],
                    AvgBasicSharesOutstanding=data[i]['Avg. Basic Shares Outstanding'],
                    AvgDilutedSharesOutstanding=data[i]['Avg. Diluted Shares Outstanding'],
                    revenues=data[i]['Revenues'],
                    COGS=data[i]['COGS'],
                    SGA=data[i]['SG&A'],
                    RD=data[i]['R&D'],
                    EBIT=data[i]['EBIT'],
                    EBITDA=data[i]['EBITDA'],
                    Interest_expense=data[i]['Interest expense'],
                    net=data[i]['net'],
                    AdnormalGainsOrLosses=data[i]['Abnormal Gains/Losses'],
                    IncomeTaxes=data[i]['Income Taxes'],
                    NetIncomefromDiscontinuedOp=data[i]['Net Income from Discontinued Op.'],
                    NetProfit=data[i]['Net Profit'],
                    Dividends=data[i]['Dividends'],
                    CashAndCashEquivalents=data[i]['Cash and Cash Equivalents'],
                    Receivables=data[i]['Receivables'],
                    CurrentAssets=data[i]['Current Assets'],
                    NetPPE=data[i]['Net PP&E'],
                    Intangible_Assets=data[i]['Intangible Assets'],
                    GoodWill=data[i]['Goodwill'],
                    TotalNoncurrentAssets=data[i]['Total Noncurrent Assets'],
                    TotalAssets=data[i]['Total Assets'],
                    ShortTermDebt=data[i]['Short term debt'],
                    AccountsPayable=data[i]['Accounts Payable'],
                    CurrentLiabilities=data[i]['Current Liabilities'],
                    LongTermDebt=data[i]['Long Term Debt'],
                    TotalNoncurrentLiabilities=data[i]['Total Noncurrent Liabilities'],
                    TotalLiabilities=data[i]['Total Liabilities'],
                    PrefferedEquity=data[i]['Preferred Equity'],
                    ShareCapital=data[i]['Share Capital'],
                    TreasuryStock=data[i]['Treasury Stock'],
                    RetainedEarnings=data[i]['Retained Earnings'],
                    EquityBeforeMinorities=data[i]['Equity Before Minorities'],
                    Minorities=data[i]['Minorities'],
                    TotalEquity=data[i]['Total Equity'],
                    DepreciationAmortisation=data[i]['Depreciation & Amortisation'],
                    ChangeinWorkingCapital=data[i]['Change in Working Capital'],
                    CashFromOperatingActivities=data[i]['Cash From Operating Activities'],
                    NetChangeinPPEIntangibles=data[i]['Net Change in PP&E & Intangibles'],
                    CashFromInvestingActivities=data[i]['Cash From Investing Activities'],
                    CashFromFinancingActivities=data[i]['Cash From Financing Activities'],
                    NetChangeinCash=data[i]['Net Change in Cash'],
                    FreeCashFlow=data[i]['Free Cash Flow'],
                    GrossMargin=data[i]['Gross Margin'],
                    OperatingMargin=data[i]['Operating Margin'],
                    NetProfitMargin=data[i]['Net Profit Margin'],
                    ReturnonEquity=data[i]['Return on Equity'],
                    ReturnonAssets=data[i]['Return on Assets'],
                    CurrentRatio=data[i]['Current Ratio'],
                    LiabilitiestoEquityRatio=data[i]['Liabilities to Equity Ratio'],
                    DebtToAssetsRatio=data[i]['Debt to Assets Ratio'],
                    EvEBITDA=data[i]['EV / EBITDA'],
                    EvSales=data[i]['EV / Sales'],
                    BooktoMarket=data[i]['Book to Market'],
                    OperatingIncomeEV=data[i]['Operating Income / EV'],
                    MarketCapitalisation=data[i]['Market Capitalisation'],

                )

                indicator_obj.save()
                print('indicator_obj', created)
            for i in range(1, len(c_part['SimFin ID'])):
                print('dataaaaa', i)
                compnay_obj, created = Company.objects.get_or_create(
                    simfinId=str(c_part['SimFin ID'][i]),
                    companyName=str(c_part['company'][i]),
                    ticker=str(c_part['ticker'][i]),
                    financialYearEndMonth=str(c_part['financial year end (month)'][i]),
                    industryCode=str(c_part['industry code'][i]),
                    indicator=indicator_obj

                )

                compnay_obj.save()
                print('company-obj', created)

    return HttpResponseRedirect(reverse("upload_csv"))

def get_ticker_list():
    ticker_list = []
    ticker = HistStocks.objects.values('symbol').distinct()
    for i in ticker:
        for k,v in i.items():
            if k == 'symbol':
                ticker_list.append(v)
                ticker_list.sort()
    return ticker_list


def get_function_list():
    function_list = ['TIME_SERIES_DAILY','TIME_SERIES_WEEKLY','TIME_SERIES_MONTHLY']
    return function_list


def get_function_list_for_adj_live_data():
    function_list = ['TIME_SERIES_DAILY_ADJUSTED' , 'TIME_SERIES_WEEKLY_ADJUSTED','TIME_SERIES_MONTHLY_ADJUSTED']
    return function_list


def get_interval_list_for_intra_live_data():
    interval_list = ['1min', '5min', '15min', '30min', '60min']
    return interval_list

def get_tecnical_indicator_function_list():
    function_list=['SMA','EMA']
    return function_list
def get_interval_list_for_technical_data():
    interval_list=['1min', '5min', '15min', '30min','60min', 'daily', 'weekly', 'monthly']
    return interval_list

def first(request):
    context={'a':10}
    return render(request,'base.html',context)
def home(request):
    query = request.GET.get('search_box')
    symbol = str(query)
    print('symbol',symbol)
    comany_name = Company.objects.get(ticker=symbol)
    print('aaaa', comany_name)

    qs_id = comany_name.simfinId
    qc = int(qs_id)
    print('xxxx', qc)
    indicator = Indicator.objects.filter(Sid=qc)
    print('indicator', indicator)

    company = Company.objects.filter(simfinId=qc)
    print('company', company)
    # all_company = Company.objects.all()
    main = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='

    rest = '&interval=1min&apikey=VX6YIV41711R3HSO'
    url = main + symbol + rest
    restsma = '&time_period=10&series_type=close'
    urlsma = 'https://www.alphavantage.co/query?function=SMA' + '&symbol=' + symbol + '&interval=1min' + restsma + '&apikey=VX6YIV41711R3HSO'
    restema = '&time_period=10&series_type=close'
    urlema = 'https://www.alphavantage.co/query?function=EMA' + '&symbol=' + symbol + '&interval=1min' + restema + '&apikey=LSFIEW3MWL734JUH'
    restmacd = '&series_type=close&fastmatype=10'
    urlmacd='https://www.alphavantage.co/query?function=MACD'+ '&symbol=' + symbol + '&interval=15min'+restmacd+'&apikey=LSFIEW3MWL734JUH'
    urlstoch = 'https://www.alphavantage.co/query?function=STOCH' + '&symbol=' + symbol + '&interval=15min&slowkmatype=1&slowdmatype=1' + '&apikey=VX6YIV41711R3HSO'
    urlrsi = 'https://www.alphavantage.co/query?function=RSI' + '&symbol=' + symbol + '&interval=15min&time_period=10&series_type=close' + '&apikey=VX6YIV41711R3HSO'
    urlobv = 'https://www.alphavantage.co/query?function=OBV' + '&symbol=' + symbol + '&interval=weekly' + '&apikey=VX6YIV41711R3HSO'
    try:

        var = 'Time Series (1min)'
        varsma='Technical Analysis: SMA'
        varema = 'Technical Analysis: EMA'
        varmacd='Technical Analysis: MACD'
        varstoch='Technical Analysis: STOCH'
        varrsi='Technical Analysis: RSI'
        varobv='Technical Analysis: OBV'
        datasma = requests.get(urlsma).json()[str(varsma)]
        dataema = requests.get(urlema).json()[str(varema)]
        datamacd=requests.get(urlmacd).json()[str(varmacd)]
        datastoch=requests.get(urlstoch).json()[str(varstoch)]
        datarsi=requests.get(urlrsi).json()[str(varrsi)]
        dataobv=requests.get(urlobv).json()[str(varobv)]

        transformedobv = [(v.update({'Time': k}) or v) for (k, v) in dataobv.items()]
        obv = transformedobv[0]
        singletransformedobv = [{k: v for (k, v) in obv.items()}]

        transformed_list_obv = []
        for x in singletransformedobv:
            x['OBV'] = x.pop('OBV')

            transformed_list_obv.append(x)
        print('obv', transformed_list_obv)


        transformedrsi = [(v.update({'Time': k}) or v) for (k, v) in datarsi.items()]
        rssi = transformedrsi[0]
        singletransformedrsi = [{k: v for (k, v) in rssi.items()}]

        transformed_list_rsi = []
        for x in singletransformedrsi:
            x['RSI'] = x.pop('RSI')


            transformed_list_rsi.append(x)
        print('rsi', transformed_list_rsi)

        transformedstoch = [(v.update({'Time': k}) or v) for (k, v) in datastoch.items()]
        sotc=transformedstoch[0]
        singletransformedstoch = [{k: v for (k, v) in sotc.items()}]

        transformed_list_stoch=[]
        for x in singletransformedstoch:
            x['SlowD'] = x.pop('SlowD')
            x['SlowK'] = x.pop('SlowK')

            transformed_list_stoch.append(x)
        print('stoch',transformed_list_stoch)
        transformedmacd = [(v.update({'Time': k}) or v) for (k, v) in datamacd.items()]
        mm = transformedmacd[0]
        singletransformedmacd = [{k: v for (k, v) in mm.items()}]
        transformed_list_macd = []
        print('macd',transformed_list_macd)
        for x in singletransformedmacd:
            x['close'] = x.pop('MACD')

            transformed_list_macd.append(x)
        print('macd',transformed_list_macd)

        transformedema = [(v.update({'Time': k}) or v) for (k, v) in dataema.items()]
        lll = transformedema[0]
        singletransformedema = [{k: v for (k, v) in lll.items()}]
        transformed_list_ema = []
        for x in singletransformedema:
            x['close'] = x.pop('EMA')

            transformed_list_ema.append(x)

        data = requests.get(url).json()[var]
        transformedsma = [(v.update({'Time': k}) or v) for (k, v) in datasma.items()]
        zzz=transformedsma[0]
        singletransformedsma = [{k: v for (k, v) in zzz.items()}]
        transformed_list_sma = []
        for x in singletransformedsma:
            x['close'] = x.pop('SMA')

            transformed_list_sma.append(x)

        # a = list(data.values())[0]
        # print ('aa',a)
        # print ("rakibvaidata",data)

        transformed_all = [(v.update({'Time': k}) or v) for (k, v) in data.items()]
        aaaa = transformed_all[0]

        singletransformed = [{k: v for (k, v) in aaaa.items()}]

        print (singletransformed)
        transformed_single = []
        for i in singletransformed:
            i['open'] = i.pop('1. open')
            i['high'] = i.pop('2. high')
            i['low'] = i.pop('3. low')
            i['close'] = i.pop('4. close')
            i['volume'] = i.pop('5. volume')
            transformed_single.append(i)

            # print ("pranto transformed",transformed)
        transformed_all_list = []
        for x in transformed_all:
            x['open'] = x.pop('1. open')
            x['high'] = x.pop('2. high')
            x['low'] = x.pop('3. low')
            x['close'] = x.pop('4. close')
            x['volume'] = x.pop('5. volume')
            transformed_all_list.append(x)



        context = {
            'ticker_list': get_ticker_list(),
            'interval_list': get_interval_list_for_intra_live_data(),
            'data': transformed_all_list,
            'datasma': transformed_list_sma,
            'dataema':transformed_list_ema,
            'datamacd': transformed_list_macd,
            'datastoch': transformed_list_stoch,
            'datarsi': transformed_list_rsi,
            'dataobv': transformed_list_obv,
            'singledata': transformed_single,
            'symbol': symbol,
            'indicator':indicator,
            'company':company

        }
        return render(request, "index.html", context)
    except KeyError:
        return render(request, '404.html')



'''
def home(request):
    query=request.GET.get('search_box')
    symbol=str(query)
    main='https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='

    rest='&interval=1min&apikey=VX6YIV41711R3HSO'
    url=main+symbol+rest
    response = requests.get(url)

    data = response.json()
    #data = requests.get(url).json()[str(var)]

    geo= data['Time Series (1min)']
    a=list(geo.values())[0]
    generetsymbol=data['Meta Data']
    print('mestada',generetsymbol)
    trans = [{k : v  for (k, v) in generetsymbol.items()}]
    trans_list = []
    for xy in trans:

        xy['Symbol'] = xy.pop('2. Symbol')

        trans_list.append(xy)

    #print (geo)
    print ("rakib",trans_list)

   # Time_l=list(Time)
   # print (Time_l)
    transformed = [{k : v  for (k, v) in a.items()}]
    print (transformed)
    transformed_list = []
    for x in transformed:
        x['open'] = x.pop('1. open')
        x['high'] = x.pop('2. high')
        x['low'] = x.pop('3. low')
        x['close'] = x.pop('4. close')
        x['volume'] = x.pop('5. volume')
        transformed_list.append(x)



    return render(request, 'index.html', {
        'Data': trans_list,
        'Time': transformed_list


    })
'''


def get_intra_day_data(request):
    if request.method == 'POST' and 'Livedata' in request.POST:
        symbol = str(request.POST.get('get_symbol'))
        interval = str(request.POST.get('get_interval'))
        key = 'LSFIEW3MWL734JUH'
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval='+interval+'&symbol=' + symbol + '&apikey=' + key
        try:
            if interval == '1min':
                var = 'Time Series (1min)'
            elif interval == '5min':
                var = 'Time Series (5min)'
            elif interval == '15min':
                var = 'Time Series (15min)'
            elif interval == '30min':
                var = 'Time Series (30min)'
            else:
                var = 'Time Series (60min)'
            data = requests.get(url).json()[str(var)]
            # print ("rakibvaidata",data)
            transformed = [(v.update({'Time': k}) or v) for (k, v) in data.items()]
            # print ("pranto transformed",transformed)
            transformed_list = []
            for x in transformed:
                x['open'] = x.pop('1. open')
                x['high'] = x.pop('2. high')
                x['low'] = x.pop('3. low')
                x['close'] = x.pop('4. close')
                x['volume'] = x.pop('5. volume')
                transformed_list.append(x)

            context = {
                'ticker_list': get_ticker_list(),
                'interval_list': get_interval_list_for_intra_live_data(),
                'data': transformed_list,
                'symbol': symbol,
                'interval': interval
            }
            return render(request, "intradaylivedata.html", context)
        except KeyError:
            return render(request, '404.html')

    else:
        context = {
            'ticker_list': get_ticker_list(),
            'interval_list': get_interval_list_for_intra_live_data(),
        }
        return render(request, "intradaylivedata.html", context)


def get_data(request):
    if request.method == 'POST' and 'Livedata' in request.POST:
        symbol = str(request.POST.get('get_symbol'))
        functions = str(request.POST.get('get_function'))
        key = 'LSFIEW3MWL734JUH'
        url = 'https://www.alphavantage.co/query?function='+functions+'&symbol='+symbol+'&apikey='+key
        try:
            if functions == 'TIME_SERIES_DAILY':
                var = 'Time Series (Daily)'
            elif functions == 'TIME_SERIES_WEEKLY':
                var = 'Weekly Time Series'
            else:
                var = 'Monthly Time Series'
            data = requests.get(url).json()[str(var)]
            transformed = [(v.update({'Time': k}) or v) for (k, v) in data.items()]
            transformed_list = []
            for x in transformed:
                x['open'] = x.pop('1. open')
                x['high'] = x.pop('2. high')
                x['low'] = x.pop('3. low')
                x['close'] = x.pop('4. close')
                x['volume'] = x.pop('5. volume')
                transformed_list.append(x)

            context = {
                'ticker_list': get_ticker_list(),
                'function_list': get_function_list(),
                'data': transformed_list,
                'symbol': symbol,
                'function': functions
            }
            return render(request, "livedata.html", context)
        except KeyError:
            return render(request, '404.html')
    else:
        context = {
            'ticker_list': get_ticker_list(),
            'function_list': get_function_list(),
        }
        return render(request, "livedata.html", context)


def get_adj_data(request):
    if request.method == 'POST' and 'Livedata' in request.POST:
        symbol = str(request.POST.get('get_symbol'))
        functions = str(request.POST.get('get_function'))
        key = 'LSFIEW3MWL734JUH'
        url = 'https://www.alphavantage.co/query?function='+functions+'&symbol='+symbol+'&apikey='+key
        try:
            if functions == 'TIME_SERIES_DAILY_ADJUSTED':
                var = 'Time Series (Daily)'
            elif functions == 'TIME_SERIES_WEEKLY_ADJUSTED':
                var = 'Weekly Adjusted Time Series'
            else:
                var = 'Monthly Adjusted Time Series'
            data = requests.get(url).json()[str(var)]
            transformed = [(v.update({'Time': k}) or v) for (k, v) in data.items()]
            transformed_list = []
            for x in transformed:
                x['open'] = x.pop('1. open')
                x['high'] = x.pop('2. high')
                x['low'] = x.pop('3. low')
                x['close'] = x.pop('4. close')
                x['volume'] = x.pop('6. volume')
                x['adjusted_close'] = x.pop('5. adjusted close')
                x['dividend_amount'] = x.pop('7. dividend amount')
                transformed_list.append(x)

            context = {
                'ticker_list': get_ticker_list(),
                'function_list': get_function_list_for_adj_live_data(),
                'data': transformed_list,
                'symbol': symbol,
                'function': functions
            }
            return render(request, "adjlivedata.html", context)
        except KeyError:
            return render(request, '404.html')

    else:
        context = {
            'ticker_list': get_ticker_list(),
            'function_list': get_function_list_for_adj_live_data(),
        }
        return render(request, "adjlivedata.html", context)



def get_sma(request):
    if request.method == 'POST' and 'Livedata' in request.POST:
        symbol = str(request.POST.get('get_symbol'))
        interval = str(request.POST.get('get_interval'))
        key = 'LSFIEW3MWL734JUH'
        rest = '&time_period=10&series_type=close'
        url = 'https://www.alphavantage.co/query?function=SMA'+ '&symbol=' + symbol +'&interval='+interval+ rest + '&apikey=' + key
        try:
            if interval == '1min':
                var = 'Technical Analysis: SMA'
            elif interval == '5min':
                var = 'Technical Analysis: SMA'
            elif interval == '15min':
                var = 'Technical Analysis: SMA'
            elif interval == '30min':
                var = 'Technical Analysis: SMA'
            elif interval == '60min':
                var = 'Technical Analysis: SMA'
            elif interval == 'daily':
                var = 'Technical Analysis: SMA'
            elif interval == 'weekly':
                var = 'Technical Analysis: SMA'
            elif interval == 'monthly':
                var = 'Technical Analysis: SMA'
            else:
                var = 'Technical Analysis: SMA'

            data = requests.get(url).json()[str(var)]

            transformed = [(v.update({'Time': k}) or v) for (k, v) in data.items()]

            transformed_list = []
            for x in transformed:
                x['close'] = x.pop('SMA')

                transformed_list.append(x)

            context = {
                'ticker_list': get_ticker_list(),
                'interval_list': get_interval_list_for_technical_data(),
                'data': transformed_list,
                'symbol': symbol,
                'interval': interval
            }
            return render(request, "smaema.html", context)
        except KeyError:
            return render(request, '404.html')

    else:
        context = {
            'ticker_list': get_ticker_list(),
            'interval_list': get_interval_list_for_technical_data(),
        }
        return render(request, "smaema.html", context)


def get_ema(request):
    if request.method == 'POST' and 'Livedata' in request.POST:
        symbol = str(request.POST.get('get_symbol'))
        interval = str(request.POST.get('get_interval'))
        key = 'LSFIEW3MWL734JUH'
        rest = '&time_period=10&series_type=close'
        url = 'https://www.alphavantage.co/query?function=EMA'+ '&symbol=' + symbol +'&interval='+interval+ rest + '&apikey=' + key
        try:
            if interval == '1min':
                var = 'Technical Analysis: EMA'
            elif interval == '5min':
                var = 'Technical Analysis: EMA'
            elif interval == '15min':
                var = 'Technical Analysis: EMA'
            elif interval == '30min':
                var = 'Technical Analysis: EMA'
            elif interval == '60min':
                var = 'Technical Analysis: EMA'
            elif interval == 'daily':
                var = 'Technical Analysis: EMA'
            elif interval == 'weekly':
                var = 'Technical Analysis: EMA'
            elif interval == 'monthly':
                var = 'Technical Analysis: EMA'
            else:
                var = 'Technical Analysis: EMA'

            data = requests.get(url).json()[str(var)]

            transformed = [(v.update({'Time': k}) or v) for (k, v) in data.items()]
            transformed_list = []
            for x in transformed:
                x['close'] = x.pop('EMA')

                transformed_list.append(x)

            context = {
                'ticker_list': get_ticker_list(),
                'interval_list': get_interval_list_for_technical_data(),
                'data': transformed_list,
                'symbol': symbol,
                'interval': interval
            }
            return render(request, "emadata.html", context)
        except KeyError:
            return render(request, '404.html')
    else:
        context = {
            'ticker_list': get_ticker_list(),
            'interval_list': get_interval_list_for_technical_data(),
        }
        return render(request, "emadata.html", context)

from django.db import models
# Create your models here.


class HistStocks(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=10)
    open = models.FloatField()
    close = models.FloatField()
    low = models.FloatField()
    high = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return self.symbol


class Indicator(models.Model):
    Sid = models.CharField(max_length=49,primary_key=True)
    date = models.CharField(max_length=49,blank=True)
    EnterprizeValue=models.CharField(max_length=49,blank=True)
    CommonSharesOutstanding=models.CharField(max_length=49,blank=True)
    AvgBasicSharesOutstanding=models.CharField(max_length=49,blank=True)
    AvgDilutedSharesOutstanding=models.CharField(max_length=49,blank=True)
    revenues=models.CharField(max_length=49,blank=True)
    COGS=models.CharField(max_length=49,blank=True)
    SGA=models.CharField(max_length=49,blank=True)
    RD=models.CharField(max_length=49,blank=True)
    EBIT=models.CharField(max_length=49,blank=True)
    EBITDA=models.CharField(max_length=49,blank=True)
    Interest_expense=models.CharField(max_length=49,blank=True)
    net=models.CharField(max_length=49,blank=True)
    AdnormalGainsOrLosses=models.CharField(max_length=49,blank=True)
    IncomeTaxes=models.CharField(max_length=49,blank=True)
    NetIncomefromDiscontinuedOp=models.CharField(max_length=49,blank=True)
    NetProfit=models.CharField(max_length=49,blank=True)
    Dividends=models.CharField(max_length=49,blank=True)
    CashAndCashEquivalents=models.CharField(max_length=49,blank=True)
    Receivables=models.CharField(max_length=49,blank=True)
    CurrentAssets=models.CharField(max_length=49,blank=True)
    NetPPE=models.CharField(max_length=49,blank=True)
    Intangible_Assets=models.CharField(max_length=49,blank=True)
    GoodWill=models.CharField(max_length=49,blank=True)
    TotalNoncurrentAssets=models.CharField(max_length=49,blank=True)
    TotalAssets=models.CharField(max_length=49,blank=True)
    ShortTermDebt=models.CharField(max_length=49,blank=True)
    AccountsPayable=models.CharField(max_length=49,blank=True)
    CurrentLiabilities=models.CharField(max_length=49,blank=True)
    LongTermDebt=models.CharField(max_length=49,blank=True)
    TotalNoncurrentLiabilities=models.CharField(max_length=49,blank=True)
    TotalLiabilities=models.CharField(max_length=49,blank=True)
    PrefferedEquity=models.CharField(max_length=49,blank=True)
    ShareCapital=models.CharField(max_length=49,blank=True)
    TreasuryStock=models.CharField(max_length=49,blank=True)
    RetainedEarnings=models.CharField(max_length=49,blank=True)
    EquityBeforeMinorities=models.CharField(max_length=49,blank=True)
    Minorities=models.CharField(max_length=49,blank=True)
    TotalEquity=models.CharField(max_length=49,blank=True)
    DepreciationAmortisation=models.CharField(max_length=49,blank=True)
    ChangeinWorkingCapital=models.CharField(max_length=49,blank=True)
    CashFromOperatingActivities=models.CharField(max_length=49,blank=True)
    NetChangeinPPEIntangibles=models.CharField(max_length=49,blank=True)
    CashFromInvestingActivities=models.CharField(max_length=49,blank=True)
    CashFromFinancingActivities=models.CharField(max_length=49,blank=True)
    NetChangeinCash=models.CharField(max_length=49,blank=True)
    FreeCashFlow=models.CharField(max_length=49,blank=True)
    GrossMargin=models.CharField(max_length=49,blank=True)
    OperatingMargin=models.CharField(max_length=49,blank=True)
    NetProfitMargin=models.CharField(max_length=49,blank=True)
    ReturnonEquity=models.CharField(max_length=49,blank=True)
    ReturnonAssets=models.CharField(max_length=49,blank=True)
    CurrentRatio=models.CharField(max_length=49,blank=True)
    LiabilitiestoEquityRatio=models.CharField(max_length=49,blank=True)
    DebtToAssetsRatio=models.CharField(max_length=49,blank=True)
    EvEBITDA=models.CharField(max_length=49,blank=True)
    EvSales=models.CharField(max_length=49,blank=True)
    BooktoMarket=models.CharField(max_length=49,blank=True)
    OperatingIncomeEV=models.CharField(max_length=49,blank=True)
    MarketCapitalisation=models.CharField(max_length=49,blank=True)

    def __str__(self):
        return self.Sid




class Company(models.Model):
    simfinId=models.CharField(max_length=49,primary_key=True)
    companyName=models.CharField(max_length=49)
    ticker=models.CharField(max_length=49)
    financialYearEndMonth=models.CharField(max_length=49)
    industryCode=models.CharField(max_length=49)
    indicator=models.ForeignKey('Indicator',null=False,db_column="Sid",on_delete=models.CASCADE)
    def __str__(self):
        return self.companyName


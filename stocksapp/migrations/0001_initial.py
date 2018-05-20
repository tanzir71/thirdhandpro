# Generated by Django 2.0.2 on 2018-05-16 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('simfinId', models.CharField(max_length=49, primary_key=True, serialize=False)),
                ('companyName', models.CharField(max_length=49)),
                ('ticker', models.CharField(max_length=49)),
                ('financialYearEndMonth', models.CharField(max_length=49)),
                ('industryCode', models.CharField(max_length=49)),
            ],
        ),
        migrations.CreateModel(
            name='HistStocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('symbol', models.CharField(max_length=10)),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('low', models.FloatField()),
                ('high', models.FloatField()),
                ('volume', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('Sid', models.CharField(max_length=49, primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, max_length=49)),
                ('EnterprizeValue', models.CharField(blank=True, max_length=49)),
                ('CommonSharesOutstanding', models.CharField(blank=True, max_length=49)),
                ('AvgBasicSharesOutstanding', models.CharField(blank=True, max_length=49)),
                ('AvgDilutedSharesOutstanding', models.CharField(blank=True, max_length=49)),
                ('revenues', models.CharField(blank=True, max_length=49)),
                ('COGS', models.CharField(blank=True, max_length=49)),
                ('SGA', models.CharField(blank=True, max_length=49)),
                ('RD', models.CharField(blank=True, max_length=49)),
                ('EBIT', models.CharField(blank=True, max_length=49)),
                ('EBITDA', models.CharField(blank=True, max_length=49)),
                ('Interest_expense', models.CharField(blank=True, max_length=49)),
                ('net', models.CharField(blank=True, max_length=49)),
                ('AdnormalGainsOrLosses', models.CharField(blank=True, max_length=49)),
                ('IncomeTaxes', models.CharField(blank=True, max_length=49)),
                ('NetIncomefromDiscontinuedOp', models.CharField(blank=True, max_length=49)),
                ('NetProfit', models.CharField(blank=True, max_length=49)),
                ('Dividends', models.CharField(blank=True, max_length=49)),
                ('CashAndCashEquivalents', models.CharField(blank=True, max_length=49)),
                ('Receivables', models.CharField(blank=True, max_length=49)),
                ('CurrentAssets', models.CharField(blank=True, max_length=49)),
                ('NetPPE', models.CharField(blank=True, max_length=49)),
                ('Intangible_Assets', models.CharField(blank=True, max_length=49)),
                ('GoodWill', models.CharField(blank=True, max_length=49)),
                ('TotalNoncurrentAssets', models.CharField(blank=True, max_length=49)),
                ('TotalAssets', models.CharField(blank=True, max_length=49)),
                ('ShortTermDebt', models.CharField(blank=True, max_length=49)),
                ('AccountsPayable', models.CharField(blank=True, max_length=49)),
                ('CurrentLiabilities', models.CharField(blank=True, max_length=49)),
                ('LongTermDebt', models.CharField(blank=True, max_length=49)),
                ('TotalNoncurrentLiabilities', models.CharField(blank=True, max_length=49)),
                ('TotalLiabilities', models.CharField(blank=True, max_length=49)),
                ('PrefferedEquity', models.CharField(blank=True, max_length=49)),
                ('ShareCapital', models.CharField(blank=True, max_length=49)),
                ('TreasuryStock', models.CharField(blank=True, max_length=49)),
                ('RetainedEarnings', models.CharField(blank=True, max_length=49)),
                ('EquityBeforeMinorities', models.CharField(blank=True, max_length=49)),
                ('Minorities', models.CharField(blank=True, max_length=49)),
                ('TotalEquity', models.CharField(blank=True, max_length=49)),
                ('DepreciationAmortisation', models.CharField(blank=True, max_length=49)),
                ('ChangeinWorkingCapital', models.CharField(blank=True, max_length=49)),
                ('CashFromOperatingActivities', models.CharField(blank=True, max_length=49)),
                ('NetChangeinPPEIntangibles', models.CharField(blank=True, max_length=49)),
                ('CashFromInvestingActivities', models.CharField(blank=True, max_length=49)),
                ('CashFromFinancingActivities', models.CharField(blank=True, max_length=49)),
                ('NetChangeinCash', models.CharField(blank=True, max_length=49)),
                ('FreeCashFlow', models.CharField(blank=True, max_length=49)),
                ('GrossMargin', models.CharField(blank=True, max_length=49)),
                ('OperatingMargin', models.CharField(blank=True, max_length=49)),
                ('NetProfitMargin', models.CharField(blank=True, max_length=49)),
                ('ReturnonEquity', models.CharField(blank=True, max_length=49)),
                ('ReturnonAssets', models.CharField(blank=True, max_length=49)),
                ('CurrentRatio', models.CharField(blank=True, max_length=49)),
                ('LiabilitiestoEquityRatio', models.CharField(blank=True, max_length=49)),
                ('DebtToAssetsRatio', models.CharField(blank=True, max_length=49)),
                ('EvEBITDA', models.CharField(blank=True, max_length=49)),
                ('EvSales', models.CharField(blank=True, max_length=49)),
                ('BooktoMarket', models.CharField(blank=True, max_length=49)),
                ('OperatingIncomeEV', models.CharField(blank=True, max_length=49)),
                ('MarketCapitalisation', models.CharField(blank=True, max_length=49)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='indicator',
            field=models.ForeignKey(db_column='Sid', on_delete=django.db.models.deletion.CASCADE, to='stocksapp.Indicator'),
        ),
    ]

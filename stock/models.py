from django.db import models


class Tcode(models.Model):
    scode = models.CharField(db_column='sCode', primary_key=True, max_length=10)
    sstockname = models.CharField(db_column='sStockName', max_length=30)

    class Meta:
        managed = False
        db_table = 'tCode'


class Tcompanyinfo(models.Model):
    scode = models.OneToOneField(Tcode, models.DO_NOTHING, db_column='sCode', primary_key=True)
    scompanyname = models.CharField(db_column='sCompanyName', max_length=30)
    nshares = models.IntegerField(db_column='nShares')
    txoutline = models.TextField(db_column='txOutline', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tCompanyInfo'


class Tstockholder(models.Model):
    scode = models.OneToOneField(Tcode, models.DO_NOTHING, db_column='sCode', primary_key=True)
    sstockholder = models.CharField(db_column='sStockHolder', max_length=100)
    nhavingshares = models.BigIntegerField(db_column='nHavingShares')
    npercentage = models.FloatField(db_column='nPercentage')

    class Meta:
        managed = False
        db_table = 'tStockHolder'


class Tstockprice(models.Model):
    scode = models.OneToOneField(Tcode, models.DO_NOTHING, db_column='sCode', primary_key=True)
    dtdate = models.DateField(db_column='dtDate')
    nopenprice = models.IntegerField(db_column='nOpenPrice')
    nlowprice = models.IntegerField(db_column='nLowPrice')
    nhighprice = models.IntegerField(db_column='nHighPrice')
    ncloseprice = models.IntegerField(db_column='nClosePrice')
    ntradingvolume = models.CharField(db_column='nTradingVolume', max_length=45)

    class Meta:
        managed = False
        db_table = 'tStockPrice'


class Tuserstocks(models.Model):
    userid = models.OneToOneField('Tusers', models.DO_NOTHING, db_column='userID', primary_key=True)
    scode = models.ForeignKey(Tcode, models.DO_NOTHING, db_column='sCode')
    nhavingshares = models.IntegerField(db_column='nHavingShares')

    class Meta:
        managed = False
        db_table = 'tUserStocks'
        unique_together = (('userid', 'scode'),)


class Tusers(models.Model):
    userid = models.CharField(db_column='userID', primary_key=True, max_length=15)
    userpw = models.CharField(db_column='userPW', max_length=30)
    username = models.CharField(db_column='userName', max_length=30)
    useragr = models.IntegerField(db_column='userAgr')

    class Meta:
        managed = False
        db_table = 'tUsers'

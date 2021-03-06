from django.db import models


# Create your models here.

# 用户模型类
class User(models.Model):
    # 用户账户唯一
    userAccount = models.CharField(max_length=20, unique=True)
    # 密码
    userPasswd = models.CharField(max_length=20)
    # 昵称
    userName = models.CharField(max_length=40)
    # 手机号
    userPhone = models.CharField(max_length=20)
    # 邮箱地址
    userAddress = models.CharField(max_length=100)
    # 头像路径
    userImg = models.CharField(max_length=150)
    # 等级
    userRank = models.IntegerField()
    # token验证值，每次登录之后都会更新
    userToken = models.CharField(max_length=50)
    @classmethod
    def creatuser(cls, account, passwd, name, phone, address, img, rank, token):
        u = cls(userAccount = account, userPasswd = passwd, userName = name, userPhone = phone,
                userAddress = address, userImg = img, userRank = rank, userToken = token)
        return u


class Portfolio(models.Model):  #资产组合表结构
    pname = models.CharField(max_length=100) #资产组合名称
    pnum = models.IntegerField() #资产数量
    isDelete = models.BooleanField(default=False) #是否删除

    def __str__(self):
        return "%s"%(self.pname)



class Asset(models.Model): #资产表结构
    aname = models.CharField(max_length=100) #资产名称
    acode = models.CharField(max_length=100) #资产代码
    abelong = models.ForeignKey("Portfolio", on_delete=models.CASCADE) #关联外键，所属资产组合
    isDelete = models.BooleanField(default=False) #是否删除
    def __str__(self):
        return "%s-%s"%(self.acode, self.aname)



class tData(models.Model): #交易数据表结构
    date = models.DateTimeField() #日期
    open = models.FloatField() #开盘价
    close = models.FloatField() #收盘价
    high = models.FloatField() #最高价
    low = models.FloatField() #最低价
    volume = models.FloatField() #成交量
    tbelong = models.ForeignKey("Asset", on_delete=models.CASCADE) #关联外键，交易数据所属资产
    isDelete = models.BooleanField(default=False) #是否删除
    def __str__(self):
        print("日期","开盘价","收盘价","最高价","最低价","成交量")
        return "%s%f%f%f%f%f"%(self.date, self.open, self.close, self.high, self.low, self.volume)
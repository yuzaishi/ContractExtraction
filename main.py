import model
if __name__ == '__main__':
    contract=model.ContractInfo('.\\data\\中山市合同OCR.txt')
    # print("合同文本：%s"%contract.CONTRACT_TEXT)
    # print("合同编号：%s"%contract.getCONTRACT_CODE())
    # print("合同名称：%s"%contract.getCONTRACT_NAME())
    # print("合同期限类型：%s" %contract.getCONTRACT_EXPIRE_TYPE())
    # print("合同起始日期：%s"%contract.getCONTRACT_START_DATE())
    # print("合同终止日期：%s"%contract.getCONTRACT_END_DATE())
    # print("合同期限：%s"%contract.getCONTRACT_TIME_LIMIT())
    # print("试用期开始日期：%s"%contract.getPROBATION_START())
    # print("试用期结束日期：%s"%contract.getPROBATION_END())
    # print("是否有试用期：%s"%contract.getPROBATION_ISNOT())
    # print("发放工资日期：%s"%contract.getSALARY_DATE())
    # print("计时工资：%s"%contract.getSALARY_BYTIME())
    # print("试用期工资：%s" % contract.getPROBATION_MONEY())
    # print("工资形式：%s" % contract.getSALARY_TYPE())
    # print("计时工资周期：%s" % contract.getSALARY_PERIOD())
    # print("工作内容：%s" % contract.getWORK_CONT())
    # print("工作性质：%s" % contract.getWORK_TYPE())
    # print("工作地点：%s" % contract.getWORK_ADDR())
    print("每日工作时间：%s" % contract.getWORK_HOUR_DAY())
    # print("每周工作时间：%s" % contract.getWORK_DAY_WEEK())
    # print("工作方式：%s" % contract.getWORK_TIME_TYPE())
import re
import xlwt
import os

def main():
    filenames = os.listdir('./data')

    for filename in filenames:
        f = open('./data/' + filename, 'r', encoding='utf-8')
        fContent = f.read()

        investornoList = re.findall(r'<a href="/profile/index/oid/(.*?).html" target="_blank">', fContent)
        nameList = re.findall(r'<u class="ellipsis">(.*?)</u>', fContent)
        amountList = re.findall(r'<p>投资金额：(.*?)</p>', fContent)
        timeList = re.findall(r'<p>跟投时间：(.*?)</p>', fContent)

        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet(filename)

        for indexInvestorno in range(len(investornoList)):
            worksheet.write(indexInvestorno, 0, investornoList[indexInvestorno])
        for indexName in range(len(nameList)):
            worksheet.write(indexName, 1, nameList[indexName])
        for indexAmount in range(len(amountList)):
            worksheet.write(indexAmount, 2, amountList[indexAmount])
        for indexTime in range(len(timeList)):
            worksheet.write(indexTime, 3, timeList[indexTime])
        workbook.save(filename + '.xls')
        
if __name__ == "__main__":
    main()
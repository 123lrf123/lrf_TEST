import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
url = "https://iftp.chinamoney.com.cn/english/bdInfo/"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
# 定义筛选条件
bond_type = "Treasury Bond"
issue_year = "2023"

table = soup.find("table", class_="tblDataList")

if table is None:
    print("未找到数据表格")
    exit()

header = [th.get_text() for th in table.find("tr").find_all("th")]

data_rows = []

for row in table.find_all("tr"):
    cells = row.find_all("td")

    if len(cells) == 0:
        continue

    isin = cells[0].get_text()
    bond_code = cells[1].get_text()
    issuer = cells[2].get_text()
    bond_type = cells[3].get_text()
    issue_date = cells[4].get_text()
    latest_rating = cells[5].get_text()

    if bond_type == bond_type and issue_date.endswith(issue_year):
        data_rows.append([isin, bond_code, issuer, bond_type, issue_date, latest_rating])

filename = "bond_data.csv"

try:
    with open(filename, mode='w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(data_rows)
    print("数据保存成功！")
except IOError:
    print("保存文件时发生错误")

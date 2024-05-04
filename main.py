import requests
from bs4 import BeautifulSoup
import pandas as pd

PayScale = requests.get(
    f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{1}").text
soup = BeautifulSoup(PayScale, "html.parser")
field_names = [header.text for header in soup.findAll(name="th")]
rows = []
for i in range(1, 33):
    PayScales = requests.get(
        f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{i}").text
    soup2 = BeautifulSoup(PayScales, "html.parser")
    pays = [pay.text for pay in soup2.findAll(class_="data-table__value")]
    for i in range(0, len(pays), 6):
        row = pays[i:i + 6]
        rows.append(row)

print(rows)
df = pd.DataFrame(rows, columns=field_names)
df.to_csv("PayScaleData.csv",index=False)
print("csv file created successfully")

import csv
# 从本地文件读取数据
data = []
with open("fyx_chinamoney.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # 跳过表头行
    for row in reader:
        data.append(row)
# 分割成多个批次
batches = [data[i:i+80] for i in range(0, len(data), 80)]
# 打印输出每个批次
for i, batch in enumerate(batches):
    print(f"Batch {i+1}:")
    for row in batch:
        print(row)

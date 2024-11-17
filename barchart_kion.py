import csv, japanize_matplotlib
import matplotlib.pyplot as plt

reader = csv.reader(open('/Users/iwasetomohiro/Documents/kion_data_trim.csv', encoding='utf-8'))


data = list(reader)

labels = data[0]
temps = [float(v) for v in data[1]]


plot = plt.bar(labels, temps)
plt.title('気温')
plt.show()

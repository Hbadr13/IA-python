import numpy as np
import numpy
from TinyStatistician import TinyStatistician
import statistics
import statistics as stat
import matplotlib.pyplot as plt

tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
# a = [1]
# a = [2, 7, 3, 12, 9]
print(tstat.var(a))
print(tstat.std(a))
# Expected result: 12279.439999999999
# plt.boxplot(a, vert=False)
# plt.axvline(lst[0], color='r', linestyle='--')
# plt.axvline(tstat.median(a), color='g', linestyle='-')
# plt.axvline(lst[1], color='b', linestyle='--')
# plt.xlabel('Data')
# plt.ylabel('Quartiles')
# plt.title('Box Plot of Quartiles')
# plt.show()
# # plt.savefig("data.png")
#Bar charts and analyzing data from csv

import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import pandas as pd

plt.style.use('seaborn-v0_8')
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()
for response in lang_responses:
    language_counter.update(response.split(';'))
languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()
plt.barh(languages,popularity)

plt.xlabel('Number of People')
plt.title('Most Popular Languages')
plt.show()
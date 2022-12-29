import json
from survay_analyzer import output
with open('clean-code-survey-master/data/1.json', 'r') as f:
  data_1 = json.load(f)
with open('clean-code-survey-master/data/2.json', 'r') as f:
  data_2 = json.load(f)

output(data_1)
output(data_2)
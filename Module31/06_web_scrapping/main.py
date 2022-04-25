import requests
import re

req = requests.get("http://www.columbia.edu/~fdc/sample.html")

text = req.text

search = re.findall(r'<h3.+<', text)

pre_result = re.findall(r'">.+?<', " ".join(search))

result = re.findall(r'\w[^<>]+', " ".join(pre_result))

print(result)

# зачтено

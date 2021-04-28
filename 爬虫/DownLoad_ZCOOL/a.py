import requests
import re

title = "4月字设 | 2021"
print(title)
# print(type(title))
title = re.sub(r'[\\/:\*\?"<>\|]',"",title)
print(title)
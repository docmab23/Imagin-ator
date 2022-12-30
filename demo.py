import openai
import os 
import subprocess


key = "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"
#openai.organization = "org-nz8FHEjXsTETH2ylM3LYIhGi"
openai.api_key = key
print(openai.Model.list())

cmd = """curl https://api.openai.com/v1/images/generations \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer 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' \
  -d '{
  "prompt": "A cute baby sea otter",
  "n": 2,
  "size": "1024x1024"
}'
"""

os.system(cmd)


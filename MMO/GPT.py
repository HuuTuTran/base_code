import requests
import json
import time



content_lst = []
def chat_GPT(question):
  url = "https://api.openai.com/v1/chat/completions"

  payload = json.dumps({
      "model": "gpt-3.5-turbo",
      "messages": [
          {
              "role": "system",
              "content": question
          }
      ]
  })
  headers = {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer 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',
          'Cookie': '__cf_bm=ZDjKolSrlEnWjTBB2LnGbQE2DB3ObaKZiHG.vjcwFlU-1711578586-1.0.1.1-ckuueob3rzQBMhysXsRUXu2n.K_0m2et6Xq4i.UZCDlDInQM68pNSzE8x3ienDiZ3mX5iF5hF7e4AcSNYxbrJw; _cfuvid=ZwDdlhPWKFjLMa2Xp9s2u1P_E4OH6.PUQKLeactXrkI-1711578586204-0.0.1.1-604800000'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  response = json.loads(response.text)
  result= response['choices'][0]['message']['content']
  return  result 


while True:
  question = input("Hello! How can I help you?\n")
  if question.upper() == "STOP":
    break


  answer = chat_GPT(question)
  print(answer)
  print("*"*100)        
# chat_GPT("1+1=?")

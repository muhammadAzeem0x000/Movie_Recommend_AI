import openai

openai.api_key="Your API_KEY"

prompts = input("Give your prompt: ")

response = openai.Completion.create(model="text-davinci-002", 
                                      prompt=prompts,
                                      max_tokens=256,
                                      top_p=0.1)
txt_response=response['choices'][0]['text'].strip()
print(txt_response)


#open our file, and append to it
f = open("playground.txt", "a")
#write the response we want to append 
f.write(("\n"))
f.write((txt_response))
#close our file
f.close()
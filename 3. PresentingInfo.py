# WRITE YOUR CODE HERE
import os
import openai
import secret

openai.api_key=secret.api_key
# functions

def InBox(sample):
  #this gives you the longest string
  biggest = max(sample, key = len)
  #THIS gets you the length of the biggest string
  biggest=len(biggest)
  print("+" + "-" * (biggest + 2) + "+")
  for i in sample:
    print("| " + i + (" "*(biggest-len(i))) + " |")
  print("+" + "-" * (biggest + 2) + "+")

def Moreflix():
  # ask the user for different inputs
  print("Enter 0, if you don't have an answer in mind")
  number_recs=int(input('How many movies do you want recommended: '))
  genre=input('What genre are you looking for: ')
  similar= input('What is a similar movie: ')
  # setting equal to 5 when no 0 is input
  if number_recs==0:
    number_recs=5
  if genre=="0" and similar=="0":
    return("In a python array form, give me " + str(number_recs) +" movie recommendation")
  if genre=="0" :
    return ("In a python array form, give me " + str(number_recs) +" movie recommendation, similar to " + similar)
  if similar=="0":
    return ("In a python array form, give me "+genre + " "+ str(number_recs) +" movie recommendations")
  return ("In a python array form, give me "+genre +" "+str(number_recs)+" movie recommendation similar to " + similar)

def Res(x):
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=x,
    top_p=1,
    max_tokens=100)
  return(response['choices'][0]['text'].strip())


# WRITE YOUR CODE HERE
Prompts=Moreflix() + "rec ="
results = Res(Prompts)

# Split the result into individual movie recommendations
recommendations = results.split("[")

# Display the formatted output
InBox(recommendations)

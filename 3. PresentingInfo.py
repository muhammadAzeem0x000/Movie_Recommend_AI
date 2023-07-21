import openai
import ast

openai.api_key="your_api_key"

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

# Function of getting information about the prompt
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

# Function for API call
def Res(x):
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=x,
    top_p=1,
    max_tokens=100)
  return(response['choices'][0]['text'].strip())


# Driver Code
Prompts=Moreflix() + "rec ="
movies = (Res(Prompts))
try:
  movie_list = ast.literal_eval(movies)
except:
  movie_list2 = ""
  for i in movies:
    if i=="]":
      movie_list2+=(i)
      break
    else:
      movie_list2+=(i)
  movie_list = ast.literal_eval(movie_list2)
InBox(movie_list)
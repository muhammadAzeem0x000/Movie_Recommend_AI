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

sample=["One life","Two","Potato Pie and Life"]
InBox(sample)

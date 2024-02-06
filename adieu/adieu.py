import inflect
p = inflect.engine()                         #import inflect module
lst = [ ]                                    #making empty list
while True:
    try:
        name = input("Names: ")
        lst.append(name)                     #append = the content in variable "name" is added to the list
    except EOFError:
        print ("\n")
        break
for name in lst:
    mylist = p.join((lst), final_sep=",")            
print(f"Adieu, adieu, to {mylist}")

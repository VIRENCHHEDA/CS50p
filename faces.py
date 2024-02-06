#input statement
def main():
    statement = input("any statement")
    result = convert(statement)
    print(result)

def convert(statement):
    statement=statement.replace(":)","🙂")
    statement=statement.replace( ":(","🙁")
    return statement

main()




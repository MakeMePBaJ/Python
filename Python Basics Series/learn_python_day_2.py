
# day 2 - python learn course
# if, else, elif

def coding_language_test():

    while True:

        coding_language = input(
            f"\n\nwhich coding language is the easiest?\n(chose between: Python, Java, C++)\n\nwrite here:"
            ).lower() #input to lowercase


        #boolesche logic
        if coding_language in ["python", " python"]:
            print(f"\nyou are right!")
            
        elif coding_language in ["java", "c++"]: #both integraded
            print(f"\nclose but not right :)")
            
        else:
            print(f"\nyou are my wrong!!!")
            

        #end application
        if coding_language in ["python", " python"]:
            input(f"\n\npress any key to close the application")
            exit()
            
        else:()
            

coding_language_test()
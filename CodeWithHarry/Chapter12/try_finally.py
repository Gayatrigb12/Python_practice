try:
    a = int(input("Enter a number : "))
    print(a)
except Exception as e:
    print(e)    
    
# finally:
#     print("thank you") 

print("without finally")# here it will execute 
# why finally one example 

def main():
    try:
        a = int(input("Enter a number : "))
        print(a)
        return
    except Exception as e:
        print(e) 
        return   
        
    finally:
        print("thank you") # if you used finally it will help you to execute whatever like here is return but still its execute     
    print("without finally") # this whill not work when there is return

main()

# from one and two example we get like finally will execute all the time even its written latter return keyword


"""
Output :
--CASE 1 --
PS D:\PYTHON\Python_practice\CodeWithHarry\Chapter12> python try_finally.py
Enter a number : 3
3
thank you

--CASE 2 --

PS D:\PYTHON\Python_practice\CodeWithHarry\Chapter12> python try_finally.py
Enter a number : g
invalid literal for int() with base 10: 'g'
thank you

"""
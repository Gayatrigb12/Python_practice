# def demo():
#     print("Hello Python !!")
# demo()
# print(__name__)

def demo():
    print("Hello Python !!")
    
if(__name__ == "__main__"):
    print("we are running directly this code")
    demo()
    print(__name__)


"""
--CASE 1 --(if you run imported file )
python main.py
Hello Python !!
module // give name as module 

--CASE 2 --(if you run main while whwrw the code is written file )
 python module.py
Hello Python !!
__main__


"""
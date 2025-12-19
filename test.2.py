# code
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except Exception as e:
       # By this way we can know about the type of error occurring
        print("The error is: ",e)

        
divide(3, "GFG") 
divide(3,0)
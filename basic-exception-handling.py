# Using try and except to deal with unexpected/ abnormal/ unwanted situations

# Example: Dividing two numbers
# Two possible problems: input isn't a pair of integers, and/or we try to divide by 0

# The "try" block attempts to execute the statements it contains. If it succeeds, then no error recovery is necessary. If something goes wrong (raises an excepetion), the "try"block immediately halts, and the "excepts" block begins to execute. Once either the "try" or the "except" block finishes, we continue with the code that comes *after* that section of the program; if the "except" block activates, we DO NOT return to finish the "try" block afterward.

successful = False # Use this "Flag" to determine whether the code on the "try" block was fully completed, or if it was interrupted by an exception

while not successful: # If successful is False, "not successful" is True, so the loop executes again; once successful becomes True, "not successful" is False, so the loop ends (it becomes "while False:", which won't run)
    try:
        numerator = int(input("Enter the number to be divided: "))
        denominator = int(input("Enter the number to divide by: "))
        result = numerator / denominator
        print("The result is:", result)
        successful = True # Signal that everything went right
    except ValueError:
        print("Please make sure that you're entering digits, not letters or symbols!")
        successful = False
    except ZeroDivisionError:
        print("Uh oh! You can't divide by zero!")
        successful = False
    except: # Handle anything the previous except blocks can't deal with
        print("Sorry! Something went wrong, but I don't know what it is!")
        successful = False
        
#    except Exception as e: # Saves the exception that was raised as a variable named "e"
 #       # Code to execute if something goes wrong
  #      print("Could not complete task; something went wrong!")
   #     print("Here's the problem:", e)
    #    successful = False


print("This code exists after the try-except block.")

try:
    if result < 5:
        raise Exception("foo")
    print("Your result was greater than or equal to 5")
except Exception as e:
    if "foo" in str(e): # e is an Exception, not a string, so we need to "string-ify" it before we can use the "in" operator
        print("Your result was less than 5")

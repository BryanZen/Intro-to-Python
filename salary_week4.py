# Salary rules / policies
# The first 40 hours are paid at the normal hourly rate
# If you work more than that, hours 41-50 are paid at time-and-a-half,
# and hours 51-on are paid at double-time

hours = int(input("How many hours did you work this week?"))
rate = float(input("How much do you earn per hour?"))

if hours <= 40:
    salary = hours * rate
elif hours <= 50:
    extra_hours = hours - 40 # Figure out the number of overtime hours
    salary = (40 *rate) + (extra_hours * rate * 1.5) # first 40 hrs + OT
elif hours > 50:
    extra_hours = hours - 50
    salary = (40 * rate) + (10 * rate * 1.5) + (extra_hours * rate * 2)
    
print ("You earned $", salary, " this week", sep="")

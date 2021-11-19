# Choose an activity based on current temperature

temperature = int(input("What is the temperature outside?"))

if temperature >= 90:
    activity = "swimming"
elif temperature >+ 70:
    activity = "tennis"
elif temperature >= 60:
    activity = "running"
else:
    activity = "watching movies inside"

print("Today's activity is:", activity) 

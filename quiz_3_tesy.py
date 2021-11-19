time = input("Time (HH:MM:SS): ")
list = time.split(":")
hours = int(list[0]) * 3600
minutes = int(list[1]) * 60
seconds = int(list[2])

total_secs = hours + minutes + seconds
print(total_secs)

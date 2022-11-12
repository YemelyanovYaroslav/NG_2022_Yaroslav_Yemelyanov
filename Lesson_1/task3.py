all_seconds = int(input("Enter the number of seconds: "))

days = all_seconds // 86400
hours = all_seconds // 3600 % 24
minutes = all_seconds // 60 % 60
seconds = all_seconds % 60

print(f"{days}:{hours:02}:{minutes:02}:{seconds:02}")
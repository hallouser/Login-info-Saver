print("testing")
f = open("info.txt", "w")

app = input("What is the app you want to save info for?: ")
username = input("What is your username for the app your using?: ")
password = input("What is your password for the app your using?: ")

f = open("info.txt", "w")
f.write(app)
f.write("\nusername:")
f.write(username)
f.write("\npassword:")
f.write(password)
f.close()

f = open("info.txt", "r")
print(f.read())

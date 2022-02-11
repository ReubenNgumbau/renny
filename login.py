#program to login
username=str(input("enter username:"))#user enter username
pwd=int(input("enter password:"))#user enter password
logins=["BSCIT-05-0322/2020",1487]
if username in logins and pwd in logins:
   print("login successful")
else:
  print("incorrect username or password")

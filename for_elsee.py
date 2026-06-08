
files=["a.txt","b.csv","c.txt"]
for file in files:
    if file.endswith("txt"):
        print("The csv file is: ",file)
        break
else:
    print("All values are checked")


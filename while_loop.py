name = "Ram Srinivas"
width = 50
line = "_" * width
design = " " * 9 + "\\" + " " * 36 + "/" + "\n" + " " * 8 + "\\" + " " * 38 + "/" + "\n" + " " * 7 + "\\" + " " * 40 + "/" + "\n" + " " * 6 + "\\" + "_" * 42 + "/"

print(line)
print("|" + " " * ((width - 2 - len(name)) // 2) + "WELCOME, " + name.upper() + " TO THE CHATBOT" + " " * ((width - 3 - len(name)) // 3) + "|")
print("|" + "_" * (width - 2) + "|")
print(design)

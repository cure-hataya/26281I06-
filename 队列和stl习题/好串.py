alpha =input()
if not alpha.startswith("a") and alpha.endswith("b"):
    print("Bad")
elif not alpha.count("a") == alpha.count("b"):
    print("Bad")
else:
    print("Good")
user_input =input("")
try:
    with open('user_file.txt', 'a+') as f:
        if user_input.lower() == "show":
            f.seek(0)
            print(f.read())
        else:
            f.write(user_input + "\n")
            print("note saved.")

except Exception as e:
    print("oops, somethings went wrong")

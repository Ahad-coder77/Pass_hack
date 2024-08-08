with open("comm_pass_list.txt","r") as f:
    input= str(input("Enter you password : "))
    data = True
    while data:
        data = f.read()
        if (input in data):
            print("Password found : ",input)
            break
        else:
            print("Password does not found ")
            break
         
        
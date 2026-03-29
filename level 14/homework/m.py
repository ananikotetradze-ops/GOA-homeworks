#range()-funqcia gamoiyeneba ricxvebis mimdevrobis shesaqmnelad yvelaze xshirad ki ciklebshi
#misi argumentebia--> start, stop, step
#start- saidan iwyeba ricxvis mimdevroba
#stop- sadac range cherdeba
#step- ramdenit izrdeba an mcirdeba ricxvebi yovel nabijze
# for loop- viyenebt mashin roca gvinda ragac moqmedeba ramdenjerme gavimeorot
for i in range(5):
    print("anime")
# anime, anime, anime, anime, anime
for i in range(6):
    print(i)
# 0, 1, 2, 3, 4, 5
#while loop-mushaobs manamde sanam pasuxi weshmaritia 
i = 0
while i < 5:
    print(i)
    i += 1
# 0, 1, 2, 3, 4
password = "gojogojo"
under_pass = "enter your password: "
while under_pass != password:
    under_pass = input("enter your password: ")
    print("wrong password, try again")
    under_pass = input("enter your password: ")
    print("welcome")
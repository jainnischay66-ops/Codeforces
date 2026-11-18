t = int(input())
rat,wc,man,cap = [],[],[],[]
for _ in range(t):
    name,type = input().split()
    if type=="rat":
        rat.append(name)
    elif type=="woman" or type=="child":
        wc.append(name)
    elif type=="man":
        man.append(name)
    else:
        cap.append(name)
for name in rat+wc+man+cap:
    print(name)
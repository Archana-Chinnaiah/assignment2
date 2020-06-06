port1 =  {21: "FTP", 22:"SSH", 23: "telnet", 80:"http"} 
print (" port1= ") 
print(port1) 
print() 
port2 = {} 
for key, value in port1.items(): 
 if value in port2: 
    port2[value].append(key) 
 else: 
    port2[value]=[key] 
print ("port2 = { ")  
for i in port2: 
	print(i, " :", port2[i]) 
print ("} ")

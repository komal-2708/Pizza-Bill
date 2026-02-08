print("Pizza Bill Calculator")
print()
print("Small(s)-$100","Medium(m)-$150","Large(l)-$200",sep="\n")
print()
p=input("Do you want a pizza?[yes/no]")
b=True
if(p=="yes"):
    tot=0
    total=0
    s=100
    m=150
    l=200
    while(b):
        size=input("What size of pizza do you want?[s,m,l]")
        if(size=="s"):
            tot=tot+s
            print("Total Bill amount : $",tot)
        elif(size=="m"):
            tot=tot+m
            print("Total Bill amount : $",tot)
        elif(size=="l"):
            tot=tot+l
            print("Total Bill amount : $",tot)
        both=input("Do you want both cheese and pepperoni?[yes/no]")
        if(both=="yes"):
            if(size=="s"):
                tot=tot+40
                print("Total Bill amount : $",tot)
            elif(size=="m"):
                tot=tot+50
                print("Total Bill amount : $",tot)
            elif(size=="l"):
                tot=tot+70
                print("Total Bill amount : $",tot)
        elif(both=="no"):
            pep=input("Do you want some extra pepperoni on your pizza?[yes/no]")
            if(pep=="yes"):
                if(size=="s"):
                    tot=tot+20
                    print("Total Bill amount : $",tot)
                elif(size=="m"):
                    tot=tot+20
                    print("Total Bill amount : $",tot)
                elif(size=="l"):
                    tot=tot+20
                    print("Total Bill amount : $",tot)
            c=input("Do you want some extra cheese on your pizza?[yes/no]")
            if(c=="yes"):
                if(size=="s"):
                    tot=tot+20
                    print("Total Bill amount : $",tot)
                elif(size=="m"):
                    tot=tot+30
                    print("Total Bill amount : $",tot)
                elif(size=="l"):
                    tot=tot+50
                    print("Total Bill amount : $",tot)
        rep=input("Do you want to take next order?[yes/no]")
        if(rep=="yes"):
            d=input("Do you want to add this to your previous bill or do you want new bill[previous/new]")
            if(d=="previous"):
                total=total+tot
                print("Total Bill Amount : $",total)
            elif(d=="new"):
                tot=0
        elif(rep=="no"):
            b=False
            print("OK Thank You")
            print("Total Bill amount : $",tot)
elif(p=="no"):
     print("Good Choice")    
        
    
    
    
    
    
    

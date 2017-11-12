import wolframalpha
print ("Lösen von Gleichungen der Form ax³+cx+d=0")
x3 = input("a= ")
c = input("c= ")
p = "("+c+"/"+x3+")"
q = "("+input("d= ")+"/"+x3+")"
if float(c)!=0:
    for x in range(0, 3):
        query = "simplify 2*sqrt(-" + p + "/3)*cos((1/3)*arccos((3"+q+")/(2"+p+")*sqrt(-3/"+p+"))-"+str(x)+"*(2pi/3))"
        app_id = "LY8WVT-VYYP2QGLUP"
        client = wolframalpha.Client(app_id)    
        res = client.query(query)
        answer = next(res.results).text
        print ("x"+str(x+1)+"= "+answer)
        #print (query)
else:
    query = "3rd root ("+q+")"
    app_id = "LY8WVT-VYYP2QGLUP"
    client = wolframalpha.Client(app_id)    
    res = client.query(query)
    answer = next(res.results).text
    print ("x= "+answer)
input()

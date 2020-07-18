i=1
def adder(a,b,c):
    return a+b+c

value_i = {
    "我想死" : [i,"賣安內","len 回傳 3"],
    "我老公" : ["湯姆漢克斯","len 回傳 2"],
    "加法" : [adder(1,2,3)]
}
if len(value_i["加法"]) == 1 : #TypeError: object of type 'int' has no len()
    print(len (value_i))
    print(value_i["加法"][0])

#print (value_i[i%(len(value_i))])
#if len (value_i[i% len(value_i)+1])==1 :
#    value_i[i% len(value_i)+1]
#print (len(value_i[i% len(value_i)+1]))
if i == 9999:
    adder(value_i[1])
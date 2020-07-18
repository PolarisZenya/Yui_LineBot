i=7
def adder(a,b,c):
    return a+b+c

value_i = {
    1 : [i,"賣安內","len 回傳 3"],
    2 : ["湯姆漢克斯","len 回傳 2"],
    3 : [adder(1,2,3)]
}
if len(value_i[i%len(value_i)+1]) == 2 : #TypeError: object of type 'int' has no len()
    print(len (value_i[i%len(value_i)+1]))
    print(value_i[i%len(value_i)+1][1])

#print (value_i[i%(len(value_i))])
#if len (value_i[i% len(value_i)+1])==1 :
#    value_i[i% len(value_i)+1]
#print (len(value_i[i% len(value_i)+1]))
if i == 9999:
    adder(value_i[1])
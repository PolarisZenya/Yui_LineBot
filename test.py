i=8
def xadd(a,b,c,d):
    return a+b+c+d

value_i ={
    1 : ["是可可蘿啦...(可可蘿機器人哭倒路邊","https://i.imgur.com/gIF9vdY.png"],
    2 : xadd(
            10,
            5,
            7,
            8
        ),
    3 : '真是的 騎士君又惹哭可哥蘿了...(咦?',
    4 : '真是的 騎士君又惹哭可哥蘿了...(咦?',
    5 : '真是的 騎士君又惹哭可哥蘿了...(咦?',
    0 : '可可萝同志乃我大美食殿堂\n不可分割之固有成员\n骑士君应充分理解和尊重\n美食殿堂的这一立场\n並立即正名"可可蘿"'
}
#print (value_i[i%(len(value_i))])
if len (value_i[i% len(value_i)])==2 :
    print (value_i[i% len(value_i)])
print (len(value_i[i% len(value_i)]))
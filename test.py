i=1


value_i = {
            1 : [
                    'https://i.imgur.com/wT28YYw.jpg',
                    'https://i.imgur.com/8BXeAO7.jpg',
                    'https://i.imgur.com/iZqYbd5.jpg',
                    'https://i.imgur.com/WXUitOs.jpg',
                    'https://i.imgur.com/mqKucrg.jpg',
                    'https://i.imgur.com/oa5rPGp.jpg',
                    'https://i.imgur.com/Fthdiox.jpg',
                    'https://i.imgur.com/QTyEwNd.jpg',
                    'https://i.imgur.com/kxrFnvP.jpg',
                    'https://i.imgur.com/plfXJWD.jpg',
                    'https://www.pixiv.net/artworks/73074675'
                ],   
            2 : [
                    'https://i.imgur.com/46S4XEm.jpg',
                    'https://i.imgur.com/q91hXfv.jpg',
                    'https://i.imgur.com/lMtUojt.jpg',
                    'https://i.imgur.com/gQmFzsA.jpg',
                    'https://i.imgur.com/zvSzHkF.jpg',
                    'https://i.imgur.com/IbvF511.jpg',
                    'https://i.imgur.com/fhMZcGb.jpg',
                    'https://i.imgur.com/dIMdlFH.jpg',
                    'https://i.imgur.com/QxKwmfO.jpg',
                    'https://i.imgur.com/kWuE6Oh.jpg',
                    'https://www.pixiv.net/artworks/62564661'
                ],  
            3 : "https://i.imgur.com/lINQsqA.jpg",
            4 : "https://i.imgur.com/ZjvdEr7.jpg",   
            5 : "https://i.imgur.com/x6y3KiT.jpg",  
            6 :  ['繪師: 真崎ケイ-pixiv',                   'https://i.imgur.com/XLEXScW.jpg'],
            7 :  ['繪師: 真崎ケイ-pixiv',                   'https://i.imgur.com/Re8GFIS.jpg'],   
            8 :  ['繪師: かにビーム-pixiv',                 'https://i.imgur.com/DIMIze8.jpg'],  
            9 :  ['繪師: かにビーム-pixiv',                 'https://i.imgur.com/ZqmBXrD.jpg'],
            10 : ['繪師: かにビーム-pixiv',                 'https://i.imgur.com/Dxysvop.jpg'],   
            11 : ['繪師: Hitsu-pixiv',                     'https://i.imgur.com/NocwYLL.jpg'],  
            12 : ['智乃香風 is not fuck your Waifu ok?',   'https://i.imgur.com/2ciqFyu.jpg']
        }
#print (value_i[i%(len(value_i))])
if len (value_i[i% len(value_i)])==2 :
    print (value_i[i% len(value_i)])
print (len(value_i[i% len(value_i)]))
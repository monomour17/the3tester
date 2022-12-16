Pt = (["AXA", "XAY"],
    ["AXA", "XAZ"],
    ["ayz", "cba"],
    ["111111111111111", "11111111111111"],
    ["XAX", "XXA"],
    ["XAA", "AXx"],
    ["zya", "cba"],
    ["zya", "abc"],
    ["ayz", "cba"],
    ["abcd", "zya'"],
    ["ariby", "#Axaz"],
    ["123", "111"],
    ["111", "456"],
    ["111", "654"],
    ["151", "161"],
    ["1111", "4321"])

It = (["tuz<abcd", ">#sAY#at", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["tuz<abcd", ">#sAY#at", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["tuz<abcd", ">#sAY#at", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["tuz<abcd", ">#sAY#at", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["AXAXAXAX", "AXAAAXXA", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["AXAXAXAX", "AXAAAXXA", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["AXAXAXAX", "AXAAAXXA", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["AXAXAXAX", "AXAAAXXA", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["AXAXAXAX", "AXAAAXXA", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["AXAXAXAX", "AXAAAXXA", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["tuz<abcd", ">#sAY#at", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["111111","123456","131111"],
    ["111111","123456","131111"],
    ["111111","123456","131111"],
    ["111111","123456","131111"],
    ["111111","123456","131111"])

Rt= ((1, 3, 270),
    False,
    (4,5,180),
    False,
    (0, 5, 0),
    (2, 3, 0),
    False,
    False,
    (4,5,180),
    False,
    (1,5,90),
    (0,0,90),
    (0,3,0),
    (1,3,180),
    (0,4,270),
    False)





"""KODUNUZU BU ARAYA YAPIŞTIRIN. fonksiyonunuzun isminin "pattern_search" olmasına dikkat edin"""





for x in range(len(Pt)):
    if pattern_search(Pt[x], It[x])==Rt[x]:
        print(x+1,"doğru")
    else:
        print(x+1,"yanlış, senin cevabın:", pattern_search(Pt[x], It[x])," doğru cevap:",Rt[x] )

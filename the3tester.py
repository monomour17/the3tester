images=open("the3I.txt")
results=open("the3R.txt")
patterns=open("the3P.txt")
image=images.read().splitlines()
result=results.read().splitlines()
pattern=patterns.read().splitlines()
imagelist=[]
resultlist=[]
patternlist=[]
for i in range(len(image)):
    imagelist.append(eval(image[i]))
    resultlist.append(eval(result[i]))
    patternlist.append(eval(pattern[i]))



"""KODUNUZU BU ARAYA YAPIŞTIRIN. fonksiyonunuzun isminin "pattern_search" olmasına dikkat edin.
the3Itxt the3R.txt the3P.txt the3tester.py dosyalarının aynı konumda olduğundan emin olun
vscode, pycharm gibi programlar bazı kişilerde /home üzerinden çalıştığı için dosyaları okumayıp hata verebilir. 
o durumlarda bu dosyayı terminalde çalıştırın"""




uzunluk=len(imagelist)
print(f"toplamda {uzunluk} kadar liste vardır. bazı listeler uzun olduğu için bekletebilir, erken kapatmayın.")
for x in range(len(imagelist)):
    if pattern_search(patternlist[x], imagelist[x])==resultlist[x]:
        print(x+1,"doğru")
    else:
        print(x+1,"yanlış, senin cevabın:", pattern_search(patternlist[x], imagelist[x])," doğru cevap:",resultlist[x] )

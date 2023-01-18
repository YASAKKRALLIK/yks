#!/usr/bin/env python
# coding: utf-8

# # # 02210201001 Yasin Demirel

# In[ ]:


class insan():
    atributenames=["Ad_Soyad","kan_grubu"]
    def __init__(self,tc,attrbts):
        self.tc=str(tc)
        self.attrbts=attrbts
    def getir(self):
        s25=[]
        s25.append(self.tc)
        for c45w in self.attrbts:
            s25.append(c45w)
        return s25
    def atributeEkle(atr):
        insan.atributenames.append(atr)
        return 1
    def atributeSil(atr):
        if atr in insan.atributenames:
            insan.atributenames.remove(atr)
            return 1
        else:
            return -1
    def atributeleri():
        return insan.atributenames
    def atributeKur(atrpack):
        insan.atributenames=atrpack
        return 1


# In[ ]:


class ogrenci(insan):
    atributenames=["Ad_Soyad","kan_grubu","okul"]
    def atributeEkle(atr):
        ogrenci.atributenames.append(atr)
        return 1
    def atributeSil(atr):
        if atr in ogrenci.atributenames:
            ogrenci.atributenames.remove(atr)
            return 1
        else:
            return -1
    def atributeleri():
        return ogrenci.atributenames
    def atributeKur(atrpack):
        ogrenci.atributenames=atrpack
        return 1


# In[ ]:


class personel(insan):
    atributenames=["Ad_Soyad","kan_grubu","bagli_oldugu_kurum_adi"]
    def atributeEkle(atr):
        personel.atributenames.append(atr)
        return 1
    def atributeSil(atr):
        if atr in personel.atributenames:
            personel.atributenames.remove(atr)
            return 1
        else:
            return -1
    def atributeleri():
        return personel.atributenames
    def atributeKur(atrpack):
        personel.atributenames=atrpack
        return 1


# In[ ]:


class oda():
    def __init__(self,yatak_Sayisi,odaNo):
        self.odaNo=str(odaNo)
        self.yatakSayisi=str(yatak_Sayisi)
        self.kayitliler=[]
    def kayitliEkle(self,instc):
        self.kayitliler.append(str(instc))
        return 1
    def kayitliSil(self,instc):
        if str(instc) in self.kayitliler:
            self.kayitliler.remove(str(instc))
            return 1
        else:
            return -1
    def kapasitesi(self):
        return int(int(self.yatakSayisi)-len(self.kayitliler))
    def yatakSayisiarttir(self,ert):
        self.yatakSayisi=str(int(self.yatakSayisi)+int(ert))
        return 1
    def kkurulum(self,kayitlileR):
        self.kayitliler=kayitlileR
        return 1
    def kayitlimi(self,instc):
        return str(instc) in self.kayitliler
    def getThisOda(self):
        asew3001=[]
        asew3001.append(self.yatakSayisi)
        asew3001.append(self.odaNo)
        for cr453 in range(len(self.kayitliler)):   
            asew3001.append(self.kayitliler[cr453])
        return asew3001


# In[ ]:


class yurt():
    def __init__(self,yurt_No):
        self.yurtNo=str(yurt_No)
        self.odalar=[]
    def insanEkle(self,instc):
        kapsul=[]
        for x in range(len(self.odalar)):
            kapsul.append(self.odalar[x].kapasitesi())
        self.odalar[kapsul.index(max(kapsul))].kayitliEkle(instc)
        return 1
    def kisilerGoster(self):
        for x in self.odalar:
            print(x.kayitliler)
        return 1
    def direkEkle(self,oda_no,instc):
        for i in range(len(self.odalar)):
            if self.odalar[i].odaNo==str(oda_no):
                self.odalar[i].kayitliEkle(instc)
                return 1
        return -1
    def getkisiler(self):
        ace=""
        for u in self.odalar:
            for t in u.kayitliler:
                ace+=t+"#"
            ace=ace[0:-1]
            ace+="$"
        q=ace[0:-1]
        return q
    def getodalar(self):
        acu=""
        for yo in self.odalar:
            acu+=yo.odaNo+"#"
        p=acu[0:-1]
        return p
    def odaEkle(self,oda):
        self.odalar.append(oda)
        return 1
    def insanSil(self,instc):
        for xq in range(len(self.odalar)):
            if self.odalar[xq].kayitlimi(instc):
                self.odalar[xq].kayitliSil(instc)
                return 1
        return 0
    def getThesepeoplewithhome(self):
        pekaci=[]
        for dew2312 in range(len(self.odalar)):
            pekaci.append(self.odalar[dew2312].getThisOda())
        return pekaci
    def yerVarmi(self):
        for han7 in self.odalar:
            if han7.kapasitesi()>0:
                return 1
        return 0


# In[ ]:


class pasifDosa():
    def __init__(self,dosadi,derce):
        self.dosadi=dosadi
        self.derece=derce
    def oku(self):
        a=open(self.dosadi,mode="a+",encoding="utf-8")
        a.seek(0,0)
        b=a.readlines()
        a.close()
        t=""
        for x in b:
            t+=x
        if self.derece==1:
            c=t.split("#")
            c.pop()
            return c            
        elif self.derece==2:
            twk=t.split("$")
            twk.pop()
            mu=[]
            for x in twk:
                mu.append(x.split("#"))
            return mu    
    def yaz(self,veri,bastanmi):
        if bastanmi:
            mode="w"
        else:
            mode="a"
        a=open(self.dosadi,mode=mode,encoding="utf-8")
        if self.derece==1:
            c=""
            for x in veri:
                c+=str(x)+"#"
            a.write(c)
            a.close()   
        elif self.derece==2:
            q0=""
            for m in veri:
                for w in m:
                    q0+=str(w)+"#"
                q0=q0[0:-1]
                q0+="$"
            a.write(q0)
            a.close()


# In[ ]:


class d12fcv():
    def onceliklimi(self,q):
        import random
        return round(random.random)


# In[ ]:


class kripto():   
    def sifreVer(self,Snum):
        import random
        as23=list(Snum)
        z=""
        q152b=["0","1","2","3","4","5","6","7","8","9"]
        for q7 in as23:
            z+=q152b[round(random.random()*9)-int(q7)]
        return z


# In[ ]:


class controller7312():
    def kbasamak(self,degu,tcb=11):
        if len(degu)==tcb:
            return 1
        else:
            return 0  
    def icermez(self,wser,qw,degree):
        teku=qw.split()
        for tiplk in range(degree):
            if teku[tiplk] in wser:
                return 0
        return 1


# In[ ]:


class tcKontrol(controller7312):
    def kontrul(self,deger):
        if self.kbasamak(deger,11)==1:
            if self.icermez(deger,"# \ $",3)==1:
                return 1
            else:
                return 0
        else:
            return 0


# In[ ]:


class basitK(controller7312):
    def kontrul(self,deger):
        if self.icermez(deger,"# \ $",3):
            return 1
        return -1


# In[ ]:


class yks:
    wqr=0
    def __init__(self,yurt00):
        yks.wqr+=1
        self.pequ=str(yks.wqr)
        self.ilkkurulum()
        self.auo=yurt00
        self.twe564=d12fcv()#sorgular için
    def sistembaslat(self):
        self.odaDosyasi=pasifDosa("odalar"+self.pequ+".txt",2)
        self.odali=self.odaDosyasi.oku()
        odaa=[]
        mou9=0
        for a in self.odali:
            odaa.append(oda(a[0],a[1]))
            odaa[mou9].kkurulum(a[2:])
            mou9+=1
        for re in range(len(odaa)):
            self.auo.odaEkle(odaa[re])
        self.insDosyasi=pasifDosa("insanlar"+self.pequ+".txt",2)
        self.insanlar=self.insDosyasi.oku()
        self.insKuDosyasi=pasifDosa("insanlarKu"+self.pequ+".txt",2)
        self.insKular=self.insKuDosyasi.oku()
        self.insKuDosyasi2=pasifDosa("insanlar2Ku"+self.pequ+".txt",2)
        self.insKu2ler=self.insKuDosyasi2.oku()
        self.baslangic()
    def ilkkurulum(self):
        dosya0=open("odalar"+self.pequ+".txt",mode="a+",encoding="utf-8")
        dosya0.close()
        dosya1=open("insanlar"+self.pequ+".txt",mode="a+",encoding="utf-8")
        dosya1.close()
        dosya2=open("insanlarKu"+self.pequ+".txt",mode="a+",encoding="utf-8")
        dosya2.close()
        dosya3=open("insanlar2Ku"+self.pequ+".txt",mode="a+",encoding="utf-8")
        dosya3.close()
        dosya4=open("insan"+self.pequ+"k.txt",mode="a+",encoding="utf-8")
        dosya4.close()
    def adGi49(self,teloke):
        if teloke !=1034:
            return -1
        pqm=1
        print("Admin girişi başarılı")
        while pqm==1:
            print("iptal etmek için iptal yaz")
            print("islem yapacağın class seç")
            print("insan için i")
            print("ogrenci için o")
            print("personel için p")
            in0qh56=input(">>>>>>")
            if in0qh56=="iptal":
                pqm=0
                break
            print("yapacağın işlemi seç")
            print("atribute eklemek için e")
            print("atribute silmek için s")
            print("atributelari goruntulemek için g")
            print("atributeları kurmak için k")
            in0qh98=input(">>>>>>")
            if in0qh56=="i":
                if in0qh98=="e":
                    poa=input("atribute adi=")
                    insan.atributeEkle(poa)
                elif in0qh98=="s":
                    poe=input("atribute adi=")
                    insan.atributeSil(poe)
                elif in0qh98=="g":
                    printu=insan.atributeleri()
                    print(printu)
                elif in0qh98=="k":
                    pou=input("atributlar arasında # koyunuz atributelar=")
                    qwsda=pou.split("#")
                    insan.atributeKur(qwsda)
            elif in0qh56=="o":
                if in0qh98=="e":
                    poa=input("atribute adi=")
                    ogrenci.atributeEkle(poa)
                elif in0qh98=="s":
                    poe=input("atribute adi=")
                    ogrenci.atributeSil(poe)
                elif in0qh98=="g":
                    printu=ogrenci.atributeleri()
                    print(printu)
                elif in0qh98=="k":
                    pou=input("atributlar arasında # koyunuz sona koymayınız atributelar=")
                    msl90r=pou.split("#")
                    ogrenci.atributeKur(msl90r)
            elif in0qh56=="p":
                if in0qh98=="e":
                    poa=input("atribute adi=")
                    personel.atributeEkle(poa)
                elif in0qh98=="s":
                    poe=input("atribute adi=")
                    personel.atributeSil(poe)
                elif in0qh98=="g":
                    printu=personel.atributeleri()
                    print(printu)
                elif in0qh98=="k":
                    pou=input("atributlar arasında # koyunuz sona koymayınız atributelar=")
                    mqj83=pou.split("#")
                    personel.atributeKur(mqj83)
    def griBio(self,terti):
        print("wellcome bro how are you")
        print("wellcome to the secret access")
        print("diyecekmifnrlqig")
        print("arızaaaaaa")
        print("yardım etmek için..")
        print("sistemtrkenşewjlkfi")
    def baslangic(self):
        print("system"+self.pequ,"is loading")
        tera=1
        mi=pasifDosa("insan"+self.pequ+"k.txt",1)
        keylermi=mi.oku()
        kriptocu=kripto()
        while tera==1:
            print("işleminizi seçin")
            print("kayıt başvurusu için yapmak için kb")
            print("kayıtlıysanız km giriniz")
            kom=input("-")
            if kom=="kb":
                print("hangisisiniz")
                print("ogrenci iseniz og")
                print("personel iseniz per")
                print("ikisi de değilseniz ik giriniz")#tüm veriler sorgulanacak
                gr349=input()
                atc=input("tc giriniz= ")
                atckontroler=tcKontrol()
                yanlissayisi=0
                while not atckontroler.kontrul(atc):
                    print("yanlış girdiniz tekrar girin")
                    atc=input("tc giriniz= ")
                    yanlissayisi+=1
                    if yanlissayisi==5:
                        tera=0
                        break
                dtek3=[]
                if gr349=="og":
                    for nu76 in ogrenci.atributenames:
                        dtek3.append(input(nu76+"="))
                elif gr349=="per":
                    for nu77 in personel.atributenames:
                        dtek3.append(input(nu77+"="))
                elif gr349=="ik":
                    for nu78 in insan.atributenames:
                        dtek3.append(input(nu78+"="))
                if self.auo.yerVarmi():
                    self.auo.insanEkle(atc)
                    odalisT2=self.auo.getThesepeoplewithhome()
                    self.odaDosyasi.yaz(odalisT2,1)                
                    temp1132=insan(atc,dtek3)
                    wq1132=temp1132.getir()
                    self.insanlar.append(wq1132)
                    qw1132=[wq1132]
                    self.insDosyasi.yaz(qw1132,0)
                    key0001=kriptocu.sifreVer(atc)
                    keylermi.append(atc)
                    keylermi.append(key0001)
                    mi.yaz([atc,key0001],0)
                    print("kaydınız tamamlandı şifreniz=",key0001,"\n şifrenizi kesinlikle unutmayın")
                else:
                    print("başvurunuz işleme alınmıştır onaylandığında bilgilendirileceksiniz")
                    temp1020=insan(atc,dtek3)
                    vewev21=temp1020.getir()
                    wevew12=[vewev21]
                    if self.twe564.onceliklimi(atc):
                        self.insKu2ler.append(vewev21)
                        self.insKuDosyasi2.yaz(wevew12,0)
                    else:
                        self.insKular.append(vewev21)
                        self.insKuDosyasi.yaz(wevew12,0)
            elif kom=="km":
                print("tcnizi boşluk şifrenizi girin")
                as23w=input("-")
                olki=as23w.split()
                if len(olki)!=2:
                    tera=0
                    break
                ok0=olki[0]
                ok1=olki[1]
                if ok0 in keylermi:
                    if ok1==keylermi[keylermi.index(ok0)+1]:
                        print("kayit sildirmek için ks")
                        print("bilgilerinizi gormek için gor giriniz")
                        se3456=input("-")
                        if se3456=="ks":
                            print("tc nizi giriniz")
                            wer456=input("-")
                            if wer456==ok0:
                                inidis43=-1
                                for lmw in range(len(self.insanlar)):
                                    if self.insanlar[lmw][0]==wer456:
                                        inidis43=lmw
                                        break
                                self.insanlar.remove(self.insanlar[inidis43])
                                self.auo.insanSil(wer456)
                                inidis45=keylermi.index(wer456)
                                for mukR in range(2):
                                    keylermi.remove(keylermi[inidis45])
                                self.insDosyasi.yaz(self.insanlar,1)
                                mi.yaz(keylermi,1)
                                odalisT=self.auo.getThesepeoplewithhome()
                                self.odaDosyasi.yaz(odalisT,1)
                                self.kuyruktanEkle()
                                tera=1
                                break
                            else:
                                tera=0
                                break
                        elif se3456=="gor":
                            inidis423=-1
                            for lmw2 in range(len(self.insanlar)):
                                if self.insanlar[lmw2][0]==ok0:
                                    inidis423=lmw2
                                    break
                            for nqw12 in self.insanlar[inidis423]:
                                print(nqw12,end=" ")
                        
                        
                    else:
                        tera=0
                        break
                else:
                    tera=0
                    break
            elif kom=="admin49":
                print("teloke=?")
                telA=int(input("-"))
                self.adGi49(telA)
    def kuyruktanEkle(self):
        chuck=0
        if len(self.insKu2ler[0])>1:
            ctc=insKu2ler[0][0]
            catr39=insKu2ler[0][1:]
            insKu2ler.remove(insKu2ler[0])
            chuck=1
        elif len(self.insKular[0])>1:
            ctc=insKular[0][0]
            catr39=insKular[0][1:]
            insKular.remove(insKular[0])
            chuck=1
        if chuck==1:
            mi2=pasifDosa("insan"+self.pequ+"k.txt",1)
            kriptocu2=kripto()
            insanQ=insan(ctc,catr39)
            insanQl=insanQ.getir()
            self.auo.insanEkle(ctc)
            self.insanlar.append(insanQl)
            insanlQ=[insanQl]
            self.insDosyasi.yaz(insanlQ)
            key0002=kriptocu2.sifreVer(ctc)
            mi2.yaz([ctc,key0002],0)
            odalisT12=self.auo.getThesepeoplewithhome()
            self.odaDosyasi.yaz(odalisT12,1)


# In[ ]:


class yksCreatinator():
    yksler=[]
    def __init__(self,yurtnum,odanums,odayataksayisi):
        self.yurt01=yurt(yurtnum)
        for x32 in range(len(odanums)):
            self.yurt01.odalar.append(oda(odayataksayisi[x32],odanums[x32]))
        self.yksler.append(yks(self.yurt01))
        print("kurulumun tamamlanması için 1 kayıt basvurusu tamamlayın")
        self.yksler[-1].sistembaslat()
    def yksyiBaslat(self,yksindex):
        self.yksler[yksindex].sistembaslat()


# In[ ]:


sistemTesti000=yksCreatinator("yurt000",["a2","a7"],[13,12])


# In[ ]:


#sistemTesti000.yksyiBaslat(0)


# In[ ]:





# -*- coding: cp1254 -*-
import random
class Card(object):
    """standart iskambil kartları sınıfı"""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ["Maça", "Karo", "Kupa", "Sinek"]
    rank_names = [None, "As" ,"2", "3", "4", "5", "6", "7", "8", "9", "10", "Vale", "Kız", "Papaz"]

    def __str__(self):
        return '%s %s' % (Card.suit_names[self.suit],
                          Card.rank_names[self.rank])
    
    def __cmp__(self, other):
        # check the suits
        if other.suit == 0 and other.rank == 2:
            return 1
        else:
            if self.rank > other.rank: return 1
            if self.rank < other.rank: return -1
            return 0

class Deck(object):
    #deste sınıfı
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def pop_card(self):
        return self.cards.pop() #en son kartı al

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def CardCount(self):
        s = 0
        for card in self.cards:
            s += 1
        return s

class Hand(Deck):
    """ Desteden kalıtan el """
    def __init__(self, label=""):
        self.cards = []
        self.label = label
        
class Game():    

    def __init__(self):
        print "Kart tahmin oyununa hos geldiniz."
        print "**********************************"
        print ""
        print "Simdi ortaya yeni bir deste acacagim."
        print "Once desteyi karistirecagim."
        print "Desteden bir kart acacagim."
        print "Siz de bir sonraki kartin buyuk mu yoksa kucuk mu oldunu tahmin edeceksiniz."
        print "Maca 2li en yuksek kart, diger kartlar sirali. Eger ayni rakamda farkli kart cekerseniz puan alamayacaksiniz."
        print "Her dogru tahmin icin bir puan alacaksiniz. 3 kez hata yaparsaniz yada destedeki kagitlar bittiginde oyun sona erecek."
        print ""
        print "Hazir misiniz?"
        print ""

        gameCount = 0
        gameScore = 0

        playAgain = True
        exitGame = ""

        while playAgain == True:
            gameScore =  self.Play()
            gameCount += 1
            print ""
            exitGame = raw_input("Tekrar denemek ister misiniz? [E | H]")
            if exitGame == 'E' or exitGame == 'e':
                playAgain = True
            else:
                playAgain = False

            print str(gameCount) + " kez oynadiniz."
            print "Toplam " + str(gameScore) + " kez dogru tahminde bulundunuz."
        
    def Play(self):
        
        yeniDeste = Deck()
        el = Hand("Oyuncu")

        dogruTahminSayisi = 0
        hataSayisi = 0

        yeniDeste.shuffle()

        birKart = yeniDeste.pop_card()
        el.add_card(birKart)
        print "Ilk kart: " + str(birKart)

        while hataSayisi < 3 and yeniDeste.CardCount() > 0:
            Tahmin = raw_input("Siradaki kart yuksek mi dusuk mu? [Y | D]")
            while Tahmin == 'Y' or Tahmin == 'D':
                if Tahmin != 'Y' and Tahmin != 'D':
                    print "Lutfen Y yada D giriniz."
                    Tahmin = raw_input()

            siradakiKart = yeniDeste.pop_card()
            el.add_card(siradakiKart)
            print "Cektiginiz kart " + str(siradakiKart)

            if siradakiKart == birKart:
                print "Kartlar esit cikti, puan yok ama oyun devam ediyor."
            elif siradakiKart > birKart:
                if Tahmin == 'Y' or Tahmin == 'y':
                    print "Tebrikler, dogru tahminde bulundunuz."
                    dogruTahminSayisi += 1
                else:
                    hataSayisi += 1
                    print "Bilemediniz. Bu sizin " + str(hataSayisi) + " hataniz. " + str(3-hataSayisi) + " hakkiniz kaldi"
            else:
                if Tahmin == 'D' or Tahmin == 'd':
                    print "Tebrikler, dogru tahminde bulundunuz."
                    dogruTahminSayisi += 1
                else:
                    hataSayisi += 1
                    print "Bilemediniz. Bu sizin " + str(hataSayisi) + " hataniz. " + str(3-hataSayisi) + " hakkiniz kaldi"

            if hataSayisi == 3: break
            birKart = siradakiKart
            print ""

        print ""
        print "Oyun sona erdi"
        print str(dogruTahminSayisi) + " dogru tahminde bulundunuz."
        
        return int(dogruTahminSayisi)



g = Game()

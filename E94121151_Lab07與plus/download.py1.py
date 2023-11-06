class Animal():                       #建立animal類別
    def __init__(self, weight, mood): #初始化，建立屬性
        self.weight = weight          #加入參數weight
        self.mood = mood              #加入參數mood

    def feed(self, n_feed):           #建立方法
        pass

    def walk(self, n_walk):
        pass

    def bath(self, n_bath):
        pass


class Dogs(Animal):
    def __init__(self, weight, mood): #初始化
        super().__init__(weight, mood)#繼承屬性

    def feed(self, n_feed):
        super().feed(n_feed)
        self.weight += 0.2 * n_feed   #設定子類別方法
        self.mood += n_feed

    def walk(self, n_walk):
        super().walk(n_walk)
        self.weight -= 0.2 * n_walk
        self.mood += 2 * n_walk

    def bath(self, n_bath):
        super().bath(n_bath)
        self.mood -= 2 * n_bath

    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed)
        self.walk(n_walk)
        self.bath(n_bath)
        print("狗狗現在的體重= {:.1f} kg, 心情 {}".format(self.weight, self.mood))


class Cats(Animal):
    def __init__(self, weight, mood):#初始化
        super().__init__(weight, mood)

    def feed(self, n_feed):
        super().feed(n_feed)
        self.weight += 0.1 * n_feed
        self.mood += n_feed

    def walk(self, n_walk):
        super().walk(n_walk)
        self.weight -= 0.1 * n_walk
        self.mood -= n_walk

    def bath(self, n_bath):
        super().bath(n_bath)
        self.mood -= 2 * n_bath

    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed)
        self.walk(n_walk)
        self.bath(n_bath)
        print("貓貓現在的體重= {:.1f} kg, 心情 {}".format(self.weight, self.mood))


dog = Dogs(4.8, 65)                  #建立物件
dog.printf(18, 10, 4)                #執行

cat = Cats(8.2, 60)
cat.printf(40, 7, 1)
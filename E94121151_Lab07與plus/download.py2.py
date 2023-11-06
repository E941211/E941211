class Animal():                             #建立animal類別
    def __init__(self, weight, mood):       #初始化，建立屬性
        self.weight = weight
        self.mood = mood

    def feed(self, n_feed):                 #建立方法
        pass

    def walk(self, n_walk):
        pass

    def bath(self, n_bath):
        pass

class Dogs(Animal):
    def __init__(self, weight, mood):
        super().__init__(weight, mood)      #繼承屬性

    def feed(self, n_feed):
        super().feed(n_feed)
        self.weight += 0.3 * n_feed         #建立子類別方法
        self.mood += 5*n_feed

    def walk(self, n_walk):
        super().walk(n_walk)
        self.weight += 0.2 * n_walk
        self.mood += 2 * n_walk

    def bath(self, n_bath):
        super().bath(n_bath)
        self.mood = self.mood - 2*n_bath

    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed)
        self.walk(n_walk)
        self.bath(n_bath)
        print("狗狗現在的體重= {:.1f} kg, 心情 {}".format(self.weight, self.mood))


class Shiba(Dogs):
    def __init__(self, weight, mood):
        super().__init__(weight, mood)

    def feed(self, n_feed):
        super().feed(n_feed)
        self.weight += 0.3 * n_feed
        self.mood += 5*n_feed

    def walk(self, n_walk):
        super().walk(n_walk)

    def bath(self, n_bath):
        super().bath(n_bath)

    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed)
        self.walk(n_walk)
        self.bath(n_bath)
        print("柴犬現在的體重= {:.1f} kg, 心情 {}".format(self.weight, self.mood))
    
    def mood_constraint(self, constraint):
        self.constraint = constraint
        print("mood最高只能為=",self.constraint)
        if self.constraint < self.mood:
            print("所以，柴犬現在的心情",self.constraint)

shiba1 = Shiba(4,80)
shiba1.printf(30,10,5)
shiba1.mood_constraint(90)
shiba2 = Shiba(3,60)
shiba2.printf(20,20,10)
shiba2.mood_constraint(300)
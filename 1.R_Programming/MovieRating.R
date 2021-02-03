
movies <- data.frame(read.csv("Movie-Ratings.csv"))


colnames(movies)<- c("Film","Genre","CriticRating","AudienceRating",
                     "BudgetMillion","Year")

head(movies)
tail(movies)
str(movies)
summary(movies)
movies$Year<-factor(movies$Year)


p <- ggplot(data=movies,aes(x=CriticRating,y=AudienceRating,
       color=Genre)) 



q <- ggplot(data=movies,aes(x=BudgetMillion,y=CriticRating,
                            color=Genre,size= AudienceRating,
                            alpha=0.1)) +geom_point()
p

ggplot(data=movies,aes(x=BudgetMillion,
                       fill=Genre)) +
  geom_histogram(binwidth=15,color="black")



ggplot() +geom_density(data=movies,
            aes(x=BudgetMillion,fill=Genre ),
                 binwidth=15,color="black", position="stack")


s <- ggplot(data=movies,aes(x=Genre,y=AudienceRating,color=Genre)) 
s+geom_point()+geom_smooth(fill=NA)
s+geom_boxplot()+geom_smooth(fill=NA)
s+geom_boxplot(size=1.2)+geom_jitter()

s+geom_jitter()+geom_boxplot(size=1.2, alpha=0.7)


v <- ggplot(data=movies,aes(x=BudgetMillion))
v+geom_histogram(  binwidth=10,aes(fill=Genre),color="Black" )


v+geom_histogram(  binwidth=10,aes(fill=Genre),color="Black" )+
  facet_grid(Genre~., scales="free")

p+geom_point(size=1)+facet_grid(.~Year)

p+geom_histogram(  binwidth=10,aes(fill=Genre),color="Black" )+
  facet_grid(Genre~Year, scales="free")

p+geom_point(size=1)+facet_grid(.~Year)

p+geom_point(aes(size=BudgetMillion))+geom_smooth()+
  facet_grid(Genre~Year)




z <- ggplot(data=movies,aes(x=BudgetMillion,
                       fill=Genre))
h<- z+ geom_histogram(binwidth=15,color="black")

h + xlab("Money Axis") + ylab("No of Movies")+
  theme(axis.title.x = element_text(color="DarkGreen",size=20),
        axis.title.y = element_text(color="Red",size=20),
        axis.text.x = element_text(color="Blue",size=20),
        axis.text.y = element_text(color="Blue",size=20),
        
        )


Ti <- ggplot(data=movies,aes(x=BudgetMillion,y=AudienceRating, 
                             color=Genre))
Ti+ geom_point(binwidth=15)

head(movies)









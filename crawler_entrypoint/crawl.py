import tweepy

from data_crawler_helper.tweepy_streamer import *
# Dictionary of the needed keywords to be crawled organized by their category (country name) mostly
dictionary = dict({
    "austri": ["Salzburg", "Rapid Wien", "Sturm Graz", "Austria Wien", "Admira Wacker Mödling", "Altach", "Mattersburg", "LASK Linz", "Ried", "Grödig", "FC Wacker Innsbruc", "Wolfsberger AC", "Kapfenberger SV", "SKN Sankt Pölten", "Austria Kärnten", "Austrian Football Bundesliga", "Helmut Köglberger", "Johann Pirkner", "Wiener Neustädter SC", "FC Vöcklabruck", "Bundesliga", "Erste Liga", "FC Salzburg", "Munas Dabbur", "Deni Alar", "Smail Prevljak", "Christoph Knasmüllner", "Bundesliga"],
    "belgium": ["RSC Anderlecht", "Standard Liège", "Edmilson Junior", "Abdoulay Diaby", "R. Emond", "Wesley", "Uruguay", "RSC Anderlecht", "KV Mechelen", "Club Brugge KV", "R Standard Liège", "RFC Liège", "Anderlecht", "Club Brugge"],
    "brazil": ["Sao Paulo", "Gremio", "Palmeiras", "Corinthians", "Campeonato Brasileiro", "Palmeiras", "Santos", "Flamengo", "Internacional", "Grêmio", "Palmeiras", "Flamengo", "Atlético Mineiro", "Portuguesa"],
    "denmark": ["Kasper Schmeichel", "Jonas Lössl", "Frederik Rönnow", "Simon Kjaer", "Zanka", "William Kvist", "København", "FC Midtjylland", "Brøndby", "Nordsjælland", "SønderjyskE", "Odense Boldklub", "Lyngby", "Superliga", "Denmark Series", "F.C. Copenhagen", "FC Midtjylland", "OB Odense", "FC Vestsjælland"],
    "egypt": ["mo salah", "mohamed salah", "Al-Ahly", "Al-Masry", "Mohamed Aboutrika", "Essam El-Hadary", "Mohamed Zidan", "Hazem Emam", "Ismaily SC", "Zamalek SC", "Tersana", "Ghazl El Mahalla", "mouha"],
    "england": ["The Premier League", "English Premier League", "serie A in Italy", "Spanish La Liga", "German Bundesliga", "Chelsea", "Manchester United", "Liverpool", "Arsenal", "Manchester City", "Tottenham Hotspur", "Everton F.C."],
    "france": ["Ligue 1", "PSG", "UEFA Champions League", "Paris Saint Germain", "Monaco", "Lyon", "Olympique Marseille" ],
    "germany": ["Bundesliga", "Bayern München", "Borussia Dortmund", "Bayer Leverkusen", "Schalke", "Werder Bremen", "Juventus", "AC Milan", "La Liga", "Real Madrid", "Barcelona", "messi", "Cristiano Ronaldo"],
    "italy": ["Keita Baldé Diao", "Serie A", "Atalanta", "Benevento", "Bologna", "SSC Napoli", "Inter Milan", "AC Milan", "Bologna"],
    "netherlands": ["ADO Den Haag", "Excelsior", "PSV Eindhoven", "FC Utrecht", "Roda JC Kerkrade", "Eredivisie", "Groningen"],
    "portugal": ["Liga NOS", "Cristiano Ronaldo", "Luís Figo", "Rui Costa", "Paulo Futre", "Ricardo Quaresma", "João Moutinho", "rouca", "Atlético", "FC Porto", "Benfica"],
    "russia": ["Lokomotiv Moscow", "CSKA Moscow", "Spartak Moscow", "Zenit St Petersburg", "VASILIY BEREZUTSKIY", "Zenit St. Petersburg", "Spartak Moskva", ],
    "spain": ["Spanish La Liga ", "Barcelona", "Atlético Madrid", "Valencia", "Sevilla", "Sporting Gijón"],
    "switzerland": ["Basel", "Young Boys", "Luzern", "Zürich", "Lugano", "Bellinzona", "FC Aarau", "SC Cham", "Swiss Super League", "Prima Lega"]})

hash_tag_list = list()
for value in dictionary.values():
    hash_tag_list += value

fetched_tweets_filename = base_dir + "/crawled_tweets/tweets.json"


#twAPI = tweepy.API(auth)
#list_of_tweets = twAPI.search("Arduino")

streamer = TwitterStreamer()
streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
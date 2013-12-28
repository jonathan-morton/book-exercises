class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_a_song(self):
        for line in self.lyrics:
            print line
            
happy_bday = Song(["Happy Birthday to you",
                  "I don't want to get sued",
                  "So Im done singing that song"])

kendrick_lyrics = ["I've done grew up around some people living their life in bottles",
                   "Grandaddy had the golden flask, backstroke every day in chicago"]
pools = Song(kendrick_lyrics)
happy_bday.sing_a_song()
pools.sing_a_song()
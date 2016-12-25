import fresh_tomatoes
import media

toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys come to life",
                        "http://vignette4.wikia.nocookie.net/disney/images/5/5b/Toy_Story_3_-_Poster.jpg/revision/20160408160703",
                        "https://www.youtube.com/watch?v=7FQ68Rw25gM")
#print(toy_story.storyline)


kabali = media.Movie("Kabali",
                     "Superstar's blockbuster",
                     "http://orig15.deviantart.net/628f/f/2016/195/5/c/kabali_poster_1_effectio_by_ashyy1999-da9xz2n.jpg",
                     "https://www.youtube.com/watch?v=9mdJV5-eias")

#print(kabali.storyline)
#kabali.show_trailer()

robot = media.Movie("Mr.Robot",
                     "Someone is watching you closely",
                     "http://static.tvtropes.org/pmwiki/pub/images/mr_robot_fs_poster.jpg",
                     "https://www.youtube.com/watch?v=xIBiJ_SzJTA")


chennai28 = media.Movie("chennai600028",
                     "the boyz are back",
                     "http://www.cineforest.com/Photos/Chennai%20600028%20Second%20Innings%20Movie%20First%20Look%20Poster/1.jpg",
                     "https://www.youtube.com/watch?v=R12iq2Qn4qQ")

movies = [toy_story,kabali,robot,chennai28]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)

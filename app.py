from movie import Movie_I_Like
from fresh_tomatoes import open_movies_page
titanic=Movie_I_Like("Titanic","http://img.moviepostershop.com/titanic-movie-poster-1997-1020339699.jpg",1997,7.7,"https://www.youtube.com/watch?v=2e-eXJ6HgkQ")
harry=Movie_I_Like("Harry Potter And The Deathly Hallows","http://static.boredpanda.com/blog/wp-content/uploads/2016/11/honest-movie-posters-067-583d73614a3b8__605.jpg",2011,8.1,"https://www.youtube.com/watch?v=_EC2tmFVNNE&t=2s")
deadpool=Movie_I_Like("Deadpool","http://www.youmovies.it/wp-content/uploads/2016/02/DEADPOOL_OOH_70X100_CmpH-03.jpg",2016,8.0,"https://www.youtube.com/watch?v=gtTfd6tISfw")
divergent=Movie_I_Like("Divergent","https://drnorth.files.wordpress.com/2015/02/divergent-2014-movie-posters-and-trailer.jpg",2014,6.7,"https://www.youtube.com/watch?v=sutgWjz10sM")
star_wars=Movie_I_Like("Star Wars: The Force Awakens","https://i.pinimg.com/736x/78/72/66/78726686611e3c9b6cbe3f1ede601fcf--star-wars-vii-star-trek.jpg",2015,8.1,"https://www.youtube.com/watch?v=sGbxmsDFVnE")
movie_list=[titanic,harry,star_wars,deadpool,divergent]
open_movies_page(movie_list)


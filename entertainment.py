import media
import fresh_tomatoes
# it is good practice to write the class def and contents separately.
toy_story = media.Movie("Toy Story", "Story of a boy and toys", "http://www.cultjer.com/img/ug_photo/2015_09/32772420150915154419.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar  = media.Movie("Avatar", "Story of another world with blue creatures", "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

mov = [toy_story, avatar]
fresh_tomatoes.open_movies_page(mov)
##library
# In the directory "movies", there is one class as Movie(). it is outside standard library. 
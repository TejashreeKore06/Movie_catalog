import movie, fresh_tomatoes

# instances of Movie class
jurassic_world = movie.Movie("Jurassic World",
        "Twenty-two years after the events of Jurassic Park, Isla Nublar now \
        features a fully functioning dinosaur theme park, Jurassic World, as \
        originally envisioned by John Hammond...",
        "Jun 12, 2015",
        "4",
        "images/jurassic_world.jpg",
        True,
        "images/jurassic_world_poster.jpg",
        "https://www.youtube.com/watch?v=xhQKwJFRL1g")

avengers = movie.Movie("Avengers: Age of Ultron",
        "When Tony Stark and Bruce Banner try to jump-start a dormant peacekeeping \
        program called Ultron, things go horribly wrong and it's up to Earth's \
        Mightiest Heroes to stop the villainous Ultron from enacting his terrible \
        plans.",
        "Apr 13, 2015",
        "4",
        "images/avengers.jpg",
        True,
        "images/avengers_poster.jpg",
        "https://www.youtube.com/watch?v=tmeOjFno6Do")

san_andreas = movie.Movie("San Andreas",
        "In the aftermath of a massive earthquake in California, a rescue-chopper \
        pilot makes a dangerous journey across the state in order to rescue his \
        daughter.",
        "May 29, 2015",
        "3",
        "images/san_andreas.jpg",
        False,
        "",
        "https://www.youtube.com/watch?v=yftHosO0eUo")

entourage = movie.Movie("Entourage",
        "Movie star Vincent Chase, together with his boys Eric, Turtle, and \
        Johnny, are back - and back in business with super agent-turned-studio \
        head Ari Gold on a risky project that will serve as Vince's directorial \
        debut.",
        "Jun 03, 2015",
        "4",
        "images/entourage.jpg",
        False,
        "",
        "https://www.youtube.com/watch?v=SGSE_XPF4_g")

mad_max = movie.Movie("Mad Max: Fury Road",
        "In a stark desert landscape where humanity is broken, two rebels \
        just might be able to restore order: Max, a man of action and of \
        few words, and Furiosa, a woman of action who is looking to make \
        it back to her childhood homeland.",
        "May 07, 2015",
        "5",
        "images/mad_max.jpg",
        False,
        "",
        "https://www.youtube.com/watch?v=hEJnMQG9ev8")

guardians = movie.Movie("Guardians of the Galaxy",
        "A group of intergalactic criminals are forced to work together to \
        stop a fanatical warrior from taking control of the universe.",
        "Jul 21, 2015",
        "5",
        "images/guardians_galaxy.jpg",
        True,
        "images/guardians_galaxy_poster.jpg",
        "https://www.youtube.com/watch?v=d96cjJhvlMA")

tomorrowland = movie.Movie("Tomorrowland",
        "Bound by a shared destiny, a teen bursting with scientific curiosity \
        and a former boy-genius inventor embark on a mission to unearth the \
        secrets of a place somewhere in time and space that exists in their \
        collective memory.",
        "May 09, 2015",
        "3",
        "images/tomorrowland.jpg",
        False,
        "",
        "https://www.youtube.com/watch?v=Vjx7wxjCv9A")

# save all movies into a list                  
movies = [jurassic_world, avengers, san_andreas, entourage, mad_max, guardians, tomorrowland]

# generate html page to show all movies
fresh_tomatoes.open_movies_page(movies)
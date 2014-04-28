import fresh_tomatoes
import media


love_comes_softly = media.Movie("1- Love comes softly",
                        "Durante la conquista del Oeste, cuando Marty había encontrado el lugar ideal para iniciar la vida de sus sueños junto a su marido, inesperadamente se queda viuda a causa de un trágico accidente. Sola, con el corazón desgarrado, sin recursos para sobrevivir, y debiendo afrontar un terrible invierno, al terminar el acto del entierro de su esposo recibe la sorprendente proposición de contraer un matrimonio de conveniencia.",
                        "http://upload.wikimedia.org/wikipedia/en/c/ce/Love_comes_softly.jpg",
                        "https://www.youtube.com/watch?v=nNz4QsJB93Q")
#print(love_comes_softly.storyline)

loves_enduring_promise = media.Movie("2- Love's enduring promise",
                     "Clark sufre un accidente que pone en riesgo la economía de la familia. Missie, que ahora es la maestra de escuela local, se ve obligada a hacerse cargo de las tareas más pesadas en la granja, hasta que aparece un jóven desconocido que se ofrece para ayudarles...",
                     "http://upload.wikimedia.org/wikipedia/en/5/57/Lovesenduringpromise.jpg",
                     "https://www.youtube.com/watch?v=oW-31tQsLNY")
#print(loves_enduring_promise.storyline)
#loves_enduring_promise.show_trailer()

loves_long_journey = media.Movie("3- Love's long journey",
                                 "Los recién casados La Haye emprenden una nueva vida como colonos en el Oeste americano. Adquieren un rancho y un buen número de cabezas de ganado. Una vez instalados, Missie confiesa a su marido que esperan un hijo. Su padre, desde la distancia, le recuerda que sus corazones están unidos por el amor y que pronto se reencontrarán. Mientras tanto, Missie trabaja como maestra granjeándose el afecto de la comunidad india.",
                                 "http://upload.wikimedia.org/wikipedia/en/9/96/Love%27s_Long_Journey.jpg",
                                 "https://www.youtube.com/watch?v=XypyZ65Gy4s")


loves_abiding_joy = media.Movie("4- Love's abiding joy",
                                "La alegría familiar de los LaHaye parece bien asentada cuando la tragedia golpea el hogar y pone a prueba sus cimientos.",
                                "http://upload.wikimedia.org/wikipedia/en/b/b6/Love%27s_Abiding_Joy.jpg",
                                "https://www.youtube.com/watch?v=BHvVx2SNTZU")


loves_unending_legacy = media.Movie("5- Love's unending legacy",
                                    "Ya han transcurrido tres años desde la muerte de su marido. Missie decide volver con su hijo a la casa de sus padres. Allí volverá a ejercer el trabajo de maestra para rehacer su vida, pero piensa que nunca más volverá a enamorarse. Siguiendo un imprevisto impulso decide adoptar a una niña huérfana que resulta ser muy rebelde y que además oculta un secreto...",
                                    "http://www.thesqueee.co.uk/wp-content/uploads/2013/09/lovesunendinglegacy.jpg",
                                    "https://www.youtube.com/watch?v=dfSXYepWxUs")

loves_unfolding_dream = media.Movie("6- Love's unfolding dream",
                                    "Belinda vive feliz con sus padres adoptivos Missie y Zach. Ha crecido y se ha convertido en una toda una mujer de caracter, aunque su vocación de convertirse en doctora estará sometida a dificultades. En este episodio también Belinda empieza a sentir un amor que le hace cuestionarse su fe.",
                                    "http://haal9000.com/dvd2008/images/loves%20unfolding%20dream.jpg",
                                    "https://www.youtube.com/watch?v=qXaK4FY_Y1s")

love_takes_wings = media.Movie("7- Love takes wing",
                               "Tras la muerte de su marido, la doctora Belinda Simpson llega a la ciudad de Sikeston. Pronto descubre que la población está enfermando y muriendo de cólera, epidemia que proviene de un orfanato cercano.",
                               "http://upload.wikimedia.org/wikipedia/en/4/48/Love_Takes_Wing.jpg",
                               "https://www.youtube.com/watch?v=6kPTPpHi7Xs")

love_finds_a_home = media.Movie("8- Love Finds a Home",
                                "La doctora Annie Watson va a casa de su mejor amiga, la también facultativa Belinda Owens. Allí, la chica tendrá que convivir con Mary, una mujer a la que le gustan los remedios naturales, y con un matrimonio en crisis, por la imposibilidad de Belinda por quedarse embarazada.",
                                "http://upload.wikimedia.org/wikipedia/en/3/33/Love_Finds_a_Home.jpg",
                                "https://www.youtube.com/watch?v=dguAb4Dpf-8")

love_begins = media.Movie("9- Love begins",
                          "En su camino a la fiebre del oro de California, dos vaqueros son arrestados por entrar en una pelea y dañando un restaurante de pueblo pequeño. Uno escapa, pero Davis Clark se queda a trabajar para pagar su deuda mediante la fijación de una granja que pertenece a dos mujeres jóvenes, Ellen y Cassie Cates. Con el tiempo, Clark y Ellen se enamoran, pero Clark se da a sus planes de hacerse ricos en el oeste de la comodidad de una familia y el hogar",
                          "http://img.movieberry.com/static/photos/125550/poster.jpg",
                          "https://www.youtube.com/watch?v=oNhAXXzvxCs")


loves_everlasting_courage = media.Movie("10- Love's everlasting courage",
                                        "Clark Davis struggles to maintain his land and support his family during a long drought. With a bank loan to repay, his wife, Ellen, takes a job in town as a seamstress, but soon becomes ill with scarlet fever. Eventually, she dies, telling Clark to leave his heart open for Missie's sake and to find love again. Devastated to lose his beloved wife, Clark and his young daughter Missie turn to his parents Irene and Lloyd for support",
                                        "http://www.christianfilmdatabase.com/wp-content/uploads/2011/09/Loves-Everlasting-Courage-Love-Comes-Softly-Vol.-10-Prequel-No.2-Christian-MovieFilm-DVD.jpg",
                                        "https://www.youtube.com/watch?v=uMzkUUEjK14")

movies = [love_comes_softly, loves_enduring_promise, loves_long_journey, loves_abiding_joy, loves_unending_legacy, loves_unfolding_dream, love_takes_wings, love_finds_a_home, love_begins, loves_everlasting_courage]
fresh_tomatoes.open_movies_page(movies)

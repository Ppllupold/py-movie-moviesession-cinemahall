import datetime

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: datetime.datetime,
                         movie_id: int, cinema_hall_id: int) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        date = datetime.datetime.strptime(session_date, "%Y-%m-%d").date()
        return MovieSession.objects.filter(show_time__date=date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_id)


def update_movie_session(session_id: int, show_time: datetime.datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    session.save()


def delete_movie_session_by_id(movie_id: int) -> None:
    MovieSession.objects.filter(id=movie_id).delete()

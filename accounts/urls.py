from django.urls import path, include
from .views import SignupView


urlpatterns = [
path('signup/', SignupView.as_view()),
# path('', include('accounts.urls'))
]


# from django.urls import path

# from api.views.publishers import PublishersView
# from .views.books import BooksView, BookView
# from .views.librarians import LibrariansView, LibrarianView
# from .views.publishers import PublishersView, PublishersView


# urlpatterns = [
#     path('books/', BooksView.as_view(), name='index'),
#     path('books/<int:pk>', BookView.as_view(), name="book"),
#     path('librarians/', LibrariansView.as_view(), name="librarians"),
#     path('librarians/<int:pk>', LibrarianView.as_view(), name="librarian"),
#     path('publishers/', PublishersView.as_view(), name="publishers"),
#     path('publishers/<int:pk>', PublishersView.as_view(), name="publisher")

    
# ]
from rest_framework import generics
from .serializers import PeopleSerializer
from .models import People

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Person."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
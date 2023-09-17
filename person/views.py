# from rest_framework import generics
# from rest_framework import status
# from rest_framework.response import Response
# from .models import Person
# from .serializers import PersonSerializer
# from django.db.models import Q
# from django.http import Http404

# class PersonCreateView(generics.CreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PersonSerializer
#     lookup_field = 'identifier'  # Define the lookup field to match the URL parameter

#     def get_object(self):
#         identifier = self.kwargs.get('identifier')

#         # Check if the identifier is a valid integer (user ID)
#         if identifier.isdigit():
#             return Person.objects.get(pk=identifier)
#         else:
#             # If it's not an integer, assume it's a name and try to retrieve by name
#             person = Person.objects.filter(Q(name__iexact=identifier) | Q(last_name__iexact=identifier)).first()
#             if not person:
#                 raise Http404('Person not found')
#             return person

#     def put(self, request, *args, **kwargs):
#         # Implement the put method to update the person's details
#         return self.partial_update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         # Implement the delete method to remove the person
#         return self.destroy(request, *args, **kwargs)


    # def get_queryset(self):
    #     # Get the 'name' parameter from the URL
    #     name = self.kwargs.get('name')

    #     # Use Q objects to allow filtering by first_name or last_name
    #     queryset = Person.objects.filter(Q(first_name__iexact=name) | Q(last_name__iexact=name))
    #     return queryset

    # def get_object(self):
    #     # Get the 'name' parameter from the URL
    #     name = self.kwargs.get(self.lookup_field)

    #     # Use Q objects to allow filtering by first_name or last_name
    #     queryset = self.filter_queryset(self.get_queryset())
    #     obj = generics.get_object_or_404(queryset, Q(first_name__iexact=name) | Q(last_name__iexact=name))
    #     self.check_object_permissions(self.request, obj)
    #     return obj

    # def get_queryset(self):
    #     return Person.objects.all()



from rest_framework import generics
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from django.db.models import Q
from django.http import Http404


class PersonCreateView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    lookup_field = 'identifier'  # Define the lookup field to match the URL parameter

    def get_object(self):
        identifier = self.kwargs.get('identifier')

        # Check if the identifier is a valid integer (user ID)
        if identifier.isdigit():
            return Person.objects.get(pk=identifier)
        else:
            # If it's not an integer, assume it's a name and try to retrieve by name
            # Correct query using the 'name' field
            person = Person.objects.filter(Q(first_name__iexact=identifier)).first()

            if not person:
                raise Http404('Person not found')
            return person

    def put(self, request, *args, **kwargs):
        # Implement the put method to update the person's details
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # Implement the delete method to remove the person
        return self.destroy(request, *args, **kwargs)

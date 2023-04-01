from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Experience, Perk
from .serializers import ExperienceListSerializer, PerkSerializer

class Experiences(APIView):
    def get(self, request):
        all_experiences = Experience.objects.all()
        serializer = ExperienceListSerializer(
            all_experiences,
            many=True,
            context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        pass

class ExperienceView(APIView):
    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass


class Perks(APIView):
    def get(self, request):
        all_perks = Perk.objects.all()
        serializer = PerkSerializer(all_perks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerkSerializer(data=request.data)
        if serializer.is_valid():
            perk = serializer.save()
            return Response(PerkSerializer(perk).data)
        else:
            return Response(serializer.errors)

class PerkView(APIView):
    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except:
            raise NotFound

    def get(self, request, pk):
        return Response(PerkSerializer(self.get_object(pk)).data)

    def put(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(perk, request.data, partial=True)
        if serializer.is_valid():
            updated_perk = serializer.save()
            return Response(PerkSerializer(updated_perk).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        perk = self.get_object(pk)
        perk.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Bookings(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass

class BookingView(APIView):
    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
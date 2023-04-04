from django.db import transaction
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Experience, Perk
from categories.models import Category
from bookings.models import Booking
from bookings.serializers import PublicBookingSerializer, CreateExperienceBookingSerializer
from .serializers import ExperienceListSerializer, ExperienceViewSerializer, PerkSerializer
from django.conf import settings
from django.utils import timezone

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
        serializer = ExperienceListSerializer(data=request.data)
        if serializer.is_valid():
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError("Category is required")
            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind == Category.CategoryKindChoices.ROOM:
                    raise ParseError("The category kind should be experiences")
            except Category.DoesNotExist:
                raise ParseError("Category not found")
            try:
                with transaction.atomic():
                    experience = serializer.save(host=request.user, category=category)
                    perks = request.data.get("perks")
                    for perk_pk in perks:
                        perk = Perk.objects.get(pk=perk_pk)
                        experience.perks.add(perk)
                    serializer = ExperienceViewSerializer(experience)
                    return Response(serializer.data)
            except Perk.DoesNotExist:
                raise ParseError("Perk not found")
        else:
            return Response(serializer.errors)


class ExperienceView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        experience = self.get_object(pk)
        serializer = ExperienceViewSerializer(
            experience,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        experience = self.get_object(pk)
        serializer = ExperienceViewSerializer(
            experience,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            # category
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError("Category is required")
            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind == Category.CategoryKindChoices.ROOM:
                    raise ParseError("The category kind should be experiences")
            except Category.DoesNotExist:
                raise ParseError("Category not found")
            
            # perks
            try:
                with transaction.atomic():
                    experience = serializer.save(category=category)
                    perks = request.data.get("perks")
                    experience.perks.set([])
                    for perk_pk in perks:
                        perk = Perk.objects.get(pk=perk_pk)
                        experience.perks.add(perk)
                    serializer = ExperienceViewSerializer(experience)
                    return Response(serializer.data)
                    
            except Perk.DoesNotExist:
                raise ParseError("Perk not found")

        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        experience = self.get_object(pk)
        experience.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class ExperiencePerks(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size
        experience = self.get_object(pk)
        serializer = PerkSerializer(
            experience.perks.all()[start:end],
            many=True,
        )
        return Response(serializer.data)


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
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        now = timezone.localtime(timezone.now()).date()
        bookings = Booking.objects.filter(
            experience__pk=pk,
            kind=Booking.BookingKindChoices.EXPERIENCE,
            experience_date__gte=now,
        )
        serializer = PublicBookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        experience = self.get_object(pk)
        serializer = CreateExperienceBookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save(
                experience=experience,
                user=request.user,
                kind=Booking.BookingKindChoices.EXPERIENCE,
            )
            serializer = PublicBookingSerializer(booking)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class BookingView(APIView):
    def get(self, request, pk, booking_pk):
        pass

    def put(self, request, pk, booking_pk):
        pass

    def delete(self, request, pk, booking_pk):
        pass
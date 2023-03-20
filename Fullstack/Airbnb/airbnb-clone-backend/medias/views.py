from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, PermissionDenied, NotAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Photo

class PhotoView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise NotFound

    def delete(self, request, pk):
        photo = self.get_object(pk=pk)
        if (photo.room and photo.room.owner != request.user) or (photo.experience and photo.experience.host != request.user):
            raise PermissionDenied

        photo.delete()
        return Response(status=HTTP_204_NO_CONTENT)
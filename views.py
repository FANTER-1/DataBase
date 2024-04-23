from rest_framework import generics, status
from rest_framework.response import Response
from .models import SubmitData
from .serializers import SubmitDataSerializer

class SubmitDataListCreateAPIView(generics.ListCreateAPIView):
    queryset = SubmitData.objects.all()
    serializer_class = SubmitDataSerializer

class SubmitDataRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubmitData.objects.all()
    serializer_class = SubmitDataSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == 'new':
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({'state': 1, 'message': 'Record updated successfully'})
        else:
            return Response({'state': 0, 'message': 'Record cannot be updated'})

class SubmitDataList(generics.ListAPIView):
    serializer_class = SubmitDataSerializer

    def get_queryset(self):
        user_email = self.request.query_params.get('user__email', None)
        if user_email is not None:
            return SubmitData.objects.filter(user__email=user_email)
        return SubmitData.objects.none()

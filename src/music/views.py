from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Subscriber
from .serializers import SubscriberSerializer


class SubscriberAdd(CreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = [IsAuthenticated]

class SubscriberDetails(RetrieveUpdateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    
class CurrentSubscriber(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        customer = Subscriber.objects.get(user_id=request.user.id)
        serializer = SubscriberSerializer(customer)

        return Response(serializer.data)
    
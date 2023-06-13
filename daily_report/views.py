from rest_framework import generics

from .models import Daily
from .serializers import DailyListSerializer, DailyDetailSerializer


class DailyList(generics.ListAPIView):
    """
    日報の一覧
    isOpen が True になっているものを日付の降順で返す
    """
    queryset = Daily.objects.filter(isOpen=True).order_by('-date')
    serializer_class = DailyListSerializer


class DailyDetail(generics.RetrieveAPIView):
    """
    日報の詳細情報
    """
    queryset = Daily.objects.all()
    serializer_class = DailyDetailSerializer

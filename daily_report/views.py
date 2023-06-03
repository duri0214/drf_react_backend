from rest_framework import generics

from .models import Daily
from .serializers import DailyListSerializer, DailyDetailSerializer, DailyCategorySerializer


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


class DailyCategory(generics.ListAPIView):
    """
    カテゴリ別の一覧
    例えば category に `univ` が入っていたら date, univ の field を返す
    """
    serializer_class = DailyCategorySerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Daily.objects.filter(isOpen=True).values('date', category).order_by('-date')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['category'] = self.kwargs['category']
        return context

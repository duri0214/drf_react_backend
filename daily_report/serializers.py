from rest_framework import serializers

from .models import Daily


class DailyListSerializer(serializers.ModelSerializer):
    """
    日報の一覧用シリアライザ
    """
    evaluation = serializers.CharField(source='evaluation.evaluation')

    class Meta:
        model = Daily
        fields = ('id', 'date', 'evaluation')


class DailyDetailSerializer(serializers.ModelSerializer):
    """
    日報の詳細用シリアライザ
    """
    class Meta:
        model = Daily
        fields = ('id', 'date', 'study', 'other', 'first_meet', 'wanna_do', 'summary')


class DailyCategorySerializer(serializers.ModelSerializer):
    """
    カテゴリ別の一覧用シリアライザ
    """
    content = serializers.SerializerMethodField()

    class Meta:
        model = Daily
        fields = ('date', 'content')

    def get_content(self, instance):
        category = self.context.get('category')
        return instance[category]

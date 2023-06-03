from django.db import models
from markdownx.models import MarkdownxField


class Daily(models.Model):
    """
    univ: 大学の課題とか
    study: 勉強したこと
    other: その他
    first_meet: 初めて知ったこと
    wanna_do: やりたいこと
    summary: 1日のまとめ
    evaluation: 1日の評価(外部キー)
    isOpen: 公開/非公開
    """
    date = models.DateField()
    univ = MarkdownxField()
    study = MarkdownxField()
    other = MarkdownxField()
    first_meet = MarkdownxField()
    wanna_do = MarkdownxField()
    summary = MarkdownxField()
    evaluation = models.ForeignKey('Evaluation', on_delete=models.PROTECT)
    isOpen = models.BooleanField(default=True)

    def __str__(self):
        date_str = self.date.__format__('%Y/%m/%d')
        return date_str


class Evaluation(models.Model):
    evaluation = models.CharField(max_length=255)

    def __str__(self):
        return self.evaluation

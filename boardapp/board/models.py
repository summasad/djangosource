from django.db import models
from django.contrib.auth.models import User

# 질문과 답변 게시판
# Question = pk(자동생성), 제목(subject), 내용(content), 작성일시(created_at), 수정일시(modified_at, null=True, blank=True)
# Answer - pk(자동생성), 질문(외래키), 내용, 작성일시, 수정일시


class Question(models.Model):
    subject = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    voter = models.ManyToManyField(
        User, related_name="voter_question", verbose_name="추천"
    )

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="질문"
    )

    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    voter = models.ManyToManyField(
        User, related_name="voter_answer", verbose_name="추천"
    )

    def __str__(self):
        return self.content


# 질문에 대한 댓글: author,content,created_at,modified_at,question
# 답변에 대한 댓글: author,content,created_at,modified_at,answer
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="질문", null=True, blank=True
    )
    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, verbose_name="답변", null=True, blank=True
    )

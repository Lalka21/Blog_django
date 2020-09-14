from django.db import models

class Article(models.Model):
	article_title = models.CharField('Название статьи', max_length = 50)
	article_text = models.TextField('Текст статьи')
	author = models.CharField('Автор статьи', max_length = 50)
	image = models.ImageField(upload_to = 'images/', null = True, blank = True, max_length = 200)
	pub_date = models.DateTimeField('Дата публикации')
	pub_create = models.DateTimeField('Дата создания')
	last_refresh = models.DateTimeField('Последнее обновление')

	def __str__(self):
		return self.article_title

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField('Автор коменнтария', max_length = 50)
	comment_text = models.CharField('Текст комментария', max_length = 200)

	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'


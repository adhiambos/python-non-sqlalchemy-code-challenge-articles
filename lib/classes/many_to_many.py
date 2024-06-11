class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = str(title)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
      if not isinstance(title, str):
        raise TypeError('title must be a string')
      if len(title) < 5 or len(title) > 50:
        raise Exception('title must be between 5 and 50 characters inclusive')
      if hasattr(self, '_title'):
        raise AttributeError('title cannot be changed')
      self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise TypeError('Author must be of type Author')

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise TypeError('Magazine must be of type Magazine')


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception('name must be a non-empty string')
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
     if not isinstance(new_name, str) or len(new_name) == 0:
        raise Exception('name must be a non-empty string')
     if hasattr(self, '_name'):
        raise AttributeError('name cannot be changed')
     self._name = new_name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        return list(set([article.magazine.category for article in self.articles()])) if self.articles() else None

    @staticmethod
    def list_authors():
        return [author.name for author in Author.all]


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise Exception('name must be between 2 and 16 characters inclusive')
        if not isinstance(category, str) or len(category) == 0:
            raise Exception('category must be a non-empty string')
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
     if not isinstance(new_name, str):
        raise TypeError("Name must be a string")
     if len(new_name) < 2 or len(new_name) > 16:
        raise Exception('name must be between 2 and 16 characters inclusive')
     self._name = new_name
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
     if not isinstance(new_category, str) or len(new_category) == 0:
        raise Exception('category must be a non-empty string')
     self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = {}
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        contributing_authors = [author for author, count in authors.items() if count >= 2]
        return contributing_authors if contributing_authors else None
class Article:
    all=[]
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = str(title)
        Article.all.Append(self)
        
        # title attribute getter method
        @property
        def title(self):
            return self._title
        
        # title attribute setter method
        @title.setter
        def title(self, title):
            if hasattr(self, 'title'):AttributeError('title cannot be changed')
            if len(title) < 5 or len(title) > 50:
                raise Exception('title must be between 5 and 50 characters inclusive')
            self._title = str(title)
            @property
            def author(self):
                return self._author
            
            @property
            def magazine(self):
                return self._magazine
            
            @author.setter
            def author(self, author):
             if isinstance(author,Author):
                self._author = author
             else:
                raise TypeError('Author must be type Author')
            @magazine.setter
            def magazine(self, magazine):
                if isinstance(magazine,Magazine):
                    self._magazine = magazine
                else:
                        raise TypeError('Magazine must be of type Magazine')
                




        
class Author:
    all = []
    def __init__(self, name):
        self._name = name
        Author.all.append(self)
        @property
        def name(self):
            return self._name
        @name.setter
        def name(self, new_names):
            self.new_name = new_names
            return self._name
        # getting articles written by the author
        def articles(self):
            return [articles for articles in Article.all if articles.author == self]
        # adding articles for the author
        def add_article(self, magazine, title):
            article = Article(self, magazine, title)
            return article
        # getting magazines the author has contributed to
        def magazines(self):
            return [magazine for magazine in Magazine.all if magazine in self.articles()]
        # getting topic areas for all articles by author
        def topic_areas(self):
            return [article.magazine.category for article in self.articles()]
            

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass
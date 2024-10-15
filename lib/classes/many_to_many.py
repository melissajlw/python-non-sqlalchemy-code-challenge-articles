class Article:
    # Class variable to store Article objects
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    # Article title must be a string between 5 and 50 characters inclusive and cannot be changed
    @title.setter
    def title(self, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50) or hasattr(self, 'title'):
            raise Exception
        self._title = title

    @property
    def author(self):
        return self._author
    
    # Article author must be of type Author
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception
        self._author = author

    @property
    def magazine(self):
        return self._magazine
    
    # Article magazine must be of type Magazine
    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise Exception
        self._magazine = magazine
        
class Author:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name

    # Author name must be a string longer than 0 characters and cannot be changed
    @name.setter
    def name(self, name):
        if not isinstance(name, str) or len(name) == 0 or hasattr(self, 'name'):
            raise Exception
        self._name = name

    # Author articles()
    # params: none
    # returns: a list of articles of type Article that the author has written
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # Author magazines()
    # params: none
    # returns: a list of unique magazines of type Magazine that the author has contributed to
    def magazines(self):
        magazines = list(set([article.magazine for article in self.articles()]))
        return magazines

    # Author add_article()
    # params: Magazine instance and title
    # returns: creates and returns a new Article instance and associates it with the author and magazine
    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine):
            article =  Article(self, magazine, title)
            return article

    # Author topic_areas()
    # params: none
    # returns: a unique list of strings with the categories of magazines the author has contributed to
    def topic_areas(self):
        if len(self.magazines()) == 0:
            return None
        return list(set([magazine.category for magazine in self.magazines()]))

class Magazine:
    # Class variable to store Magazine objects
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    # Magazine name must be a string between 2 and 16 characters inclusive
    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception
        self._name = name

    @property
    def category(self):
        return self._category
    
    # Magazine category must be a string longer than 0 characters
    @category.setter
    def category(self, category):
        if not isinstance(category, str) or len(category) == 0:
            raise Exception
        self._category = category

    # Magazine articles()
    # params: none
    # returns: a list of all the articles of type Article the magazine has published
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # Magazine contributors()
    # params: none
    # returns: a unique list of authors who have written for the magazine
    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine == self]))

    # Magazine article_titles()
    # params: none
    # returns: a list of title strings of all articles written for the magazine, otherwise None
    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        return [article.title for article in self.articles()]

    # Magazine contributing_authors
    # params: none
    # returns: a list of authors who have written more than 2 articles for the magazine, otherwise None
    def contributing_authors(self):
        authors = []
        article_authors = [article.author for article in self.articles()]
        
        for contributor in self.contributors():
            if article_authors.count(contributor) > 2:
                authors.append(contributor)
        
        if len(authors) == 0:
            return None
        return authors
    
    # Magazine top_publisher()
    # params: none
    # returns: Magazine instance with the most articles, None if there are no articles
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()))
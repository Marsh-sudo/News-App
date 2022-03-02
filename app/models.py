class Articles:
    '''
    Articles class to define articles objects
    '''

    def __init__(self,id,author,title,description,url,urlToImage):
        self.id = id
        self.title =title
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        
class Sources:
    '''
    source class to define source objects
    '''

    def __init__(self,id,name,description,url,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.language = language
        self.country =country
    
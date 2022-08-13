class Author:
    def __init__(self) -> None:
        """
        """
        self.id_ = 1
        self.name = "admin"

class Category:
    # {
    #     name: string
    #     created_at: datetime or time epoch
    #     doc_ids: list[string]
    # }
    def __init__(self, data = None) -> None:
        """
        """
        self.name = data["name"]
        self.created_at = data["created_at"]
        #self.doc_ids = data["doc_ids"]
        #self.image = data["image"]

    def update(self, data):
        self.name = data["name"]
        self.created_at = data["created_at"]
        # self.doc_ids = data["doc_ids"]
        #self.image = data["image"]
        return self
    
    def remove_doc(self, doc_id):
        self.doc_ids.remove(doc_id)
        return self

    def add_doc(self, doc_id):
        self.doc_ids.append(doc_id)
        return self
    

class Document:
    # {
    #     title: string
    #     author_id: string
    #     category_id: string
    #     created_at: datetime or time epoch
    #     meta: string 
    # }
    def __init__(self, data) -> None:
        """
        """
        self.title = data["title"]
        self.author_id =  data["author_id"]
        self.category_id = data["category_id"]
        self.created_at = data["created_at"]
        self.metadata = data["meta"]
    
    def switch_category(self, category_id):
        self.category_id = category_id
        return self
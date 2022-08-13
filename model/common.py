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
    #     docs: list[hash]
    # }
    def __init__(self, data=None) -> None:
        """
        """
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.docs = data["docs"]
        #self.image = data["image"]

    def update(self, data):
        self.name = data["name"]
        self.created_at = data["created_at"]
        # self.doc_ids = data["doc_ids"]
        #self.image = data["image"]
        return self

    def remove_doc(self, doc_id):
        for doc in self.docs:
            if doc['doc_id'] == doc_id:
                self.docs.remove(doc)
                return self
        return self

    def add_doc(self, doc_id, doc_name):
        self.docs.append({
            'doc_id': doc_id,
            'doc_name': doc_name
        })
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
        self.author_id = data["author_id"]
        self.category = data["category"]
        self.created_at = data["created_at"]
        self.metadata = data["meta"]

    def switch_category(self, category_id, category_name):
        self.category_id = {
            'category_id': category_id,
            'category_name': category_name
        }
        return self

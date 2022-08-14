class BasicControllerUI:
    # Doc

    def get_all_documents(self):
        pass

    def get_all_document_by_category(self, name):
        pass

    def get_document_by_id(self, doc_id):
        pass

    def get_document_by_name(self, doc_name):
        pass

    def delete_document_by_id(self, doc_id):
        pass

    def delete_document_by_name(self, doc_name):
        pass

    def update_document_by_id(self, doc_id):
        pass

    def update_document_by_name(self, doc_name):
        pass
    
    def create_document(self, data):
        pass

    # Category

    def get_all_categories(self):
        pass

    def get_category_by_id(self, cate_id):
        pass

    def get_category_by_name(self, cate_name):
        pass

    def delete_category_by_id(self, cate_id):
        pass

    def delete_category_by_name(self, cate_name):
        pass

    def update_category_by_id(self, cate_id):
        pass

    def update_category_by_name(self, cate_name):
        pass

    def create_category(self, data):
        pass
    

class FilterControllerUI:
    def get_documents_alike(self, part_string):
        pass

    def get_categories_alike(self, part_string):
        pass

    def get_documents_by_date(self, date):
        pass

    def get_categories_by_date(self, date):
        pass

class RepoInterface:

    def get_by_id(self, id_):
        pass

    def create(self):
        pass

    def update_by_id(self, id_, data):
        pass

    def delete_by_id(self, id_):
        pass


class CategoryRepoInteface(RepoInterface):

    def get_category_by_name(self, name):
        pass

    def get_category_by_name(self, name):
        pass

    def delete_category_by_name(self, name):
        pass


class DocRepoInteface(CategoryRepoInteface):
    def get_doc_by_title(self, title):
        pass

    def get_all_docs_by_cate_cate_id(self, cate_id):
        pass

    def get_all_docs_by_cate_name(self, cate_name):
        pass

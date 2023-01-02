# from oop.class_methods.exercise.project2.project.category import Category
# from oop.class_methods.exercise.project2.project.document import Document
# from oop.class_methods.exercise.project2.project.topic import Topic

from project.customer import Category
from project.equipment import Document
from project.gym import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.__get_object_by_id(self.categories, category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.__get_object_by_id(self.topics, topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = self.__get_object_by_id(self.documents, document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__get_object_by_id(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__get_object_by_id(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__get_object_by_id(self.documents, document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__get_object_by_id(self.documents, document_id)
        return document

    def __repr__(self):
        # result = ""
        # for document in self.documents:
        #     result += f"{document.__repr__()}" + "\n"
        # return result.strip()
        return '\n'.join([str(x) for x in self.documents])

    def __get_object_by_id(self, objects, id):
        for obj in objects:
            if obj.id == id:
                return obj


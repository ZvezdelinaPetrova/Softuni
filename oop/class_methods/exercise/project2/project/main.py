from project.customer import Category
from project.equipment import Document
from project.exercise_plan import Storage
from project.gym import Topic
# from oop.class_methods.exercise.project2.project.category import Category
# from oop.class_methods.exercise.project2.project.document import Document
# from oop.class_methods.exercise.project2.project.storage import Storage
# from oop.class_methods.exercise.project2.project.topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)




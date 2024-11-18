my_items_set = {
    "палатка",
    "еда",
    "вода",
    "нож",
    "спички",
}

brother_items_set = {
    "палатка",
    "еда",
    "вода",
    "термос",
    "карту",
}

common_set = my_items_set.union(brother_items_set)
print(common_set)
print(my_items_set)
print(brother_items_set)
shared_items_with_brother = my_items_set.intersection(brother_items_set)
print(shared_items_with_brother)

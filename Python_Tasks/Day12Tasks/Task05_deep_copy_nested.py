#5. Nested Data Independence (Deep Copy) A school stores classroom data:
#classes = [["Math", [30, 35]], ["Science", [25, 28]]]
#Scenario:
# ● Create a deep copy of this structure.
# ● Modify student count in original.
#Task:
# ● Prove that copied data remains unchanged.
# ● Explain why deep copy is required here.

import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]]

classes_copy = copy.deepcopy(classes)

classes[0][1][0] = 100

print("Original:", classes)
print("Deep Copy:", classes_copy)
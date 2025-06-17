
# set={1,2,3,4,4,4,4,5,5,5,5}
# print(set)
# set.add("vinod")
# print(set)
# set.add("jat")
# print(set)
# set.discard("vinod")
# print(set)
# set.update([1000,"vinpd",3000])
# print(set)



# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.intersection(b))  # {3}



# a = {1, 26,7,3,4,5, 3}
# b = {3, 4, 5}
# print(a.difference(b))  # {1, 2}



# ✅ What is a set in Python?
# A set is an unordered collection of unique items.

# python
# Copy
# Edit
# a = {1, 2, 3}
# b = {3, 4, 5}
# 🔗 1. union() → Combines all unique elements from both sets
# python
# Copy
# Edit
# a.union(b)
# # or a | b
# ✅ Example:

# python
# Copy
# Edit
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.union(b))     # {1, 2, 3, 4, 5}
# 🔗 2. intersection() → Common elements in both sets
# python
# Copy
# Edit
# a.intersection(b)
# # or a & b
# ✅ Example:

# python
# Copy
# Edit
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.intersection(b))  # {3}
# 🔗 3. difference() → Elements in A not in B
# python
# Copy
# Edit
# a.difference(b)
# # or a - b
# ✅ Example:

# python
# Copy
# Edit
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.difference(b))  # {1, 2}
# 🔗 4. symmetric_difference() → Elements in A or B but not both
# python
# Copy
# Edit
# a.symmetric_difference(b)
# # or a ^ b
# ✅ Example:

# python
# Copy
# Edit
# print(a.symmetric_difference(b))  # {1, 2, 4, 5}
# 🔍 5. issubset() → Is A a subset of B?
# python
# Copy
# Edit
# a.issubset(b)
# ✅ Example:

# python
# Copy
# Edit
# a = {1, 2}
# b = {1, 2, 3, 4}
# print(a.issubset(b))   # True
# 🔍 6. issuperset() → Is A a superset of B?
# python
# Copy
# Edit
# a.issuperset(b)
# ✅ Example:

# python
# Copy
# Edit
# a = {1, 2, 3, 4}
# b = {2, 3}
# print(a.issuperset(b))   # True
# 🔍 7. isdisjoint() → No common elements?
# python
# Copy
# Edit
# a.isdisjoint(b)
# ✅ Example:

# python
# Copy
# Edit
# a = {1, 2}
# b = {3, 4}
# print(a.isdisjoint(b))   # True






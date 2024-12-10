# cant contain duplicate values
# to use union intersection differences

bio_course={'tamil','english','maths','biology'}

art_courses={'tamil','english','ecom','history'}
print(bio_course)
print(art_courses)
print(bio_course.intersection(art_courses))
# {'english', 'tamil'}

print(bio_course.union(art_courses))
print(bio_course.difference(art_courses))
  
# empty strings
tuples=()
tuples1=tuple()
print(tuples)
print(tuples1)
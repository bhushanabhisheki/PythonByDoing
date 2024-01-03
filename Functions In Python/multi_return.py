def area_and_circumference(radius):
  area = radius * radius * 3.14
  circumference = 2 * 3.14 * radius
  return area,circumference

area, circumference = area_and_circumference(10)
print(area,circumference)

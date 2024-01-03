def area_of_circle(radius, pi=3.14):
  result =pi*radius*radius
  return result

def cost(circle_area, cost_per_sqm):
  total_cost = circle_area*cost_per_sqm
  return total_cost

area = area_of_circle(10)
tc= cost(area, 2)
print(tc)

print(cost(area_of_circle(10), 2)) #call function inside another

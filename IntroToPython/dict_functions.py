family = dict(
  bhushan=32,
  anuja=23,
  moksh=2
)
print(family)

print(family.get('moksh')) #2 get returns value based on key

#print(family['test']) #throws error KeyError: 'test' and further execution stops

print(family.get('test')) #returns None...no error thrown

prices={'iphone':300, 'ipad':100}
new_prices ={'iphone':600, 'imac':500}

prices.update(new_prices) #merge and update old with new
print(prices) #{'iphone': 600, 'ipad': 100, 'imac': 500}

prices.pop('ipad') #pops up ipad
print(prices) #{'iphone': 600, 'imac': 500}

#keys and items method
prices = {'iphone': 600, 'ipad': 100, 'imac': 500}
print(prices.values()) #dict_values([600, 100, 500])
print(prices.keys()) #dict_keys(['iphone', 'ipad', 'imac'])
print(prices.items())#dict_items([('iphone', 600), ('ipad', 100), ('imac', 500)])

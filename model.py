class City:
    def __init__(self, name):
        self.name = name
        self.distance_map = {}
 
    def to_string(self):
        return "City: " + self.name
        
    def add_distance(self, aCity, value):
        self.distance_map[aCity] = value
        
    def distance_to(self, aCity):
        return self.distance_map[aCity]

class Product:
    def __init__(self, name, price = 0):
        self.name = name
        self.price = price
 
    def to_string(self):
        return "Product: \n" + "\tname: " + self.name + "\n\tprice: " + str(self.price)

class Retailer:
    def __init__(self, city, name = ''):
        self.name = name
        self.city = city
        self.product_list = []
        
    def add_product(self, product):
        self.product_list.append(product)

    def to_string(self):
        info = "Retailer: \n" + "\tname: " + self.name + "\n\tcity: " + self.city.name
        for i in range(0, len(self.product_list)):
            info += "\n\t" + self.product_list[i].to_string()
        return info

class BusinessRecord:
    def __init__(self, period, product, retailer, value):
        self.period = period
        self.product = product
        self.retailer = retailer
        self.value = value
 
    def to_string(self):
        return "Product: " + self.product.name + " in " + self.retailer.city.name + " at period " + str(self.period) + " = " + str(self.value)

class BusinessData:
    def __init__(self):
        self.records = []
        
    def add_record(self, period, product, retailer, value):
        new_record = BusinessRecord(period, product, retailer, value)
        # print('Append new record: ' + new_record.to_string())
        self.records.append(new_record)
        
    def search_record(self, period, product_name, retailer):
        for i in range (0, len(self.records)):
            record = self.records[i]
            # print(record.to_string())
            # print('Expect:')
            # print(retailer.city.name)
            # print(product_name)
            # print(str(period))
            
            # print('Values:')
            # print(record.retailer.city.name)
            # print(record.product.name)
            # print(str(record.period))
            if record.retailer.city.name == retailer.city.name and record.product.name == product_name and record.period == period:
                return record
        return None

    # def search_record(self, period, retailer):
        # records = []
        # for i in range(0, len(self.records)):
            # if self.records[i].retailer.name == retailer.name and self.records[i].period == period:
                # records.append(self.records[i])
        # return records
        
    # def search_record(self, retailer):
        # records = []
        # for i in range(0, len(self.records)):
            # if self.records[i].retailer.name == retailer.name:
                # records.append(self.records[i])
        # return records
        
    def get_demand(self, period, product_name, retailer):
        return self.search_record(period, product_name, retailer).value
        
    # def get_demand(self, period, retailer):
        # demand = 0
        # records = self.search_record(period, retailer)
        # for i in range(0, len(records)):
            # demand += records[i].value
        # return demand

    # def get_demand(self, retailer):
        # demand = 0
        # records = self.search_record(retailer)
        # print('Number of records = ' + str(len(records)))
        # for i in range(0, len(records)):
            # val = records[i].value
            # print('Record info: ' + records[i].to_string())
            # demand += records[i].value
        # return demand
        
    def to_string(self):
        info = ""
        for i in range(0, len(self.records)):
            info += self.records[i].to_string() + "\n"
        return info
        
class Warehouse:
    def __init__(self, city):
        self.city = city
        self.capacity = {}
        self.demand = {}
        self.ordering_cost = {}
        self.holding_cost = {}
        self.shortage_cost = {}
        self.service_level = {}
        
    def add_capacity(self, product, value):
        self.capacity[product] = value
      
    def add_ordering_cost(self, product, value):
        self.ordering_cost[product] = value

    def add_demand(self, product, value):
        self.demand[product] = value
        
    def add_holding_cost(self, product, value):
        self.holding_cost[product] = value
    
    def add_shortage_cost(self, product, value):
        self.shortage_cost[product] = value

    def add_service_level(self, product, value):
        self.service_level[product] = value
        
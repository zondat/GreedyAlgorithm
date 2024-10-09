
# Online Python - IDE, Editor, Compiler, Interpreter

class Object:
    def __init__(self, volume, mass, price):
        self.volume             = volume
        self.mass               = mass
        self.price              = price
        self.dominating_objects = []
        self.dominated_objects  = []
        
    def dominate_mass(self, other):
        if self.mass <= other.mass and self.price >= other.price:
            return True
        return False
        
    def dominate_volume(self, other):
        if self.volume <= other.volume and self.price >= other.price:
            return True
        return False
        
    def dominate(self, other):
        if self.dominate_volume(other) and self.dominate_mass(other):
            return True
        else:
            return False
    
    def has_dominating(self):
        return len(self.dominating_objects)!=0
    
    def add_dominated(self, object):
        if not object in self.dominated_objects:
            self.dominated_objects.append(object)
            object.dominating_objects.append(self)
                        
class Heap:
    def __init__(self):
        self.objects     = []
        self.optimum_bag = None
        
    def create_object(self, volume, mass, price):
        object = Object(volume, mass, price)
        self.objects.append(object)
        return object
        
    def classify(self) :
        N = len(self.objects)
        for i in range(N-1):
            obj_i = self.objects[i]
            for j in range(i+1, N):
                obj_j = self.objects[j]
                if obj_i.dominate(obj_j):
                    obj_i.add_dominated(obj_j)
                
    def select_unassigned(self, assigned_objects):
        unassigned = []
        for obj in self.objects:
            if not obj in assigned_objects:
                unassigned.append(obj)
        return unassigned
                
    
    # Generate possible bag and compare total value
    def search_optimum(self, based_bag):
        available_objects   = self.select_unassigned(based_bag.objects)
        fittable_objects    = based_bag.select_fittable(available_objects)
        
        if len(fittable_objects) > 0:
            obj = fittable_objects[0]
            clone_bag = based_bag.clone()
            clone_bag.pack_object(obj)
            self.search_optimum(clone_bag)
            
        else:
            if based_bag.is_optimal_than(self.optimum_bag):
                self.optimum_bag = based_bag        
        
class Bag:
    def __init__(self, max_volume, max_mass):
        self.max_volume   = max_volume
        self.max_mass     = max_mass
        self.objects      = []
        self.total_mass   = 0
        self.total_volume = 0
        self.total_value  = 0
        
    def count_object(self):
        return len(self.objects)

    def pack_object(self, object):

        # Try to pack dominating object first
        if object.has_dominating():
            for dom_obj in object.dominating_objects:
                self.pack_object(dom_obj)
        
        # If object is still fit after adding dominating object
        if self.fit(object):
            self.objects.append(object)
            self.total_mass    += object.mass
            self.total_volume  += object.volume
            self.total_value   += object.price
                
    def reach_volume_limit(self):
        return self.total_volume == self.max_volume
        
    def reach_mass_limit(self):
        return self.total_mass == self.max_mass
    
    def fit(self, obj):
        attempt_mass = self.total_mass + obj.mass
        attempt_volume = self.total_volume + obj.volume
        return attempt_mass<= self.max_mass and attempt_volume <= self.max_volume
        
    def select_fittable(self, available_objects):
        fittable = []
        
        for obj in available_objects:
            if self.fit(obj):
                fittable.append(obj)
        return fittable
    
    def is_full(self, attempt_objects):
        if self.reach_mass_limit() or self.reach_volume_limit():
            return True
        for obj in attempt_objects:
            if not obj in self.objects and self.fit(obj):
                return False
        return True
    
    def is_optimal_than(self, other):
        return self.total_value > other.total_value
    
    def clone(self):
        cloned = Bag(self.max_volume, self.max_mass)
        cloned.objects      = self.objects
        cloned.total_mass   = self.total_mass
        cloned.total_volume = self.total_volume
        cloned.total_value  = self.total_value
        return cloned
        
##########################################
################# main() #################
##########################################

# Input data
heap = Heap()
heap.create_object(30, 10, 60)
heap.create_object(25, 15, 30)
heap.create_object(15, 10, 90)
heap.create_object(15, 9, 50)
heap.create_object(12, 20, 40)
heap.create_object(15, 45, 70)
heap.create_object(15, 40, 80)
heap.create_object(5, 5, 130)
heap.create_object(35, 10, 190)

# Classify objects
heap.classify()

# Find optimum bag
bag = Bag(90, 90)
heap.optimum_bag = bag
heap.search_optimum(bag)
for obj in heap.optimum_bag.objects:
    print(str(obj.mass) + ',' + str(obj.volume) + ',' + str(obj.price))
    
print(heap.optimum_bag.total_value)






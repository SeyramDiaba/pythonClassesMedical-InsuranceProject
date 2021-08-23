class Patient:
  def __init__(self, name, age,sex,bmi,num_of_children,smoker):
    self.name = name
    self.age = age
    # add more parameters here
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker

  def estimated_insurance_cost(self):
    try:
      estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
      print(self.name+ "'s estimated insureance cost is "+str(estimated_cost)+" dollars.")
    except:
      print("Update for age,sex,bmi,num_of_children and smoker should be of type integer or float")
    return estimated_cost
    
  def update_age(self,new_age):
    self.age = new_age
    print(self.name+ " is now " + str(self.age) + " years old.")

  def update_num_children(self,new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children in range(0,2):
     print(self.name+ " has " + str(self.num_of_children) + " child.")
    else:
       print(self.name+ " has " + str(self.num_of_children) + " of children.",)

  def update_bmi(self, new_bmi):
    self.bmi = new_bmi
    print(self.name+ " has a bmi of " + str(self.bmi) + ".")   
  
  def update_smoking_status(self,new_status):
    self.smoker = new_status
    if self.smoker == 0:
      print(self.name+ " is not a chain smoker")
    else:
      print(self.name+ " is a chain smoker")
    
  def patient_profile(self):
      patient_information = {}
      patient_information["Name"]= self.name
      patient_information["Age"]= self.age
      patient_information["Sex"]= self.sex
      patient_information["Bmi"]= self.bmi
      patient_information["Num_of_children"]= self.num_of_children
      patient_information["Smoker"]= self.smoker
      return patient_information

patient1 = Patient("John Doe", 25, 1 , 22.2, 0, 0)
print(patient1.name)
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_of_children)
print(patient1.smoker)

print(patient1.estimated_insurance_cost())
test1= patient1.update_age(26)
new_estimate = patient1.estimated_insurance_cost()
print(new_estimate)
patient1.update_num_children(1)
patient1.estimated_insurance_cost()

print(patient1.patient_profile())

patient1.update_bmi(22.3)
patient1.update_smoking_status(1)




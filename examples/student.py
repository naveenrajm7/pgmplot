from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianModel

# creating bayesian objects
difficulty_cpd = TabularCPD(variable='D',
                       variable_card=2,
                       values=[[.6, .4]])

intelligence_cpd = TabularCPD(variable='I',
                       variable_card=2,
                       values=[[.7, .3]])

sat_cpd = TabularCPD(variable='S',
                     variable_card=2,
                     values=[[.95, 0.2],
                             [.05, 0.8]],
                     evidence=['I'],
                     evidence_card=[2])

# grade
grade_cpd = TabularCPD(variable='G',
                         variable_card=3,
                         values=[[.3, .05, .9, .5 ],
                        [.4, .25, .08, .3],
                        [.3, .7, .02, .2]],
                         evidence=['I', 'D'],
                         evidence_card=[2, 2])

letter_cpd = TabularCPD(variable='L',
                     variable_card=2,
                     values=[[.1, 0.4, .99],
                             [.9, 0.6, .01]],
                     evidence=['G'],
                     evidence_card=[3])

# buildind model
student_model = BayesianModel([('D', 'G'),('I', 'G'), ('I', 'S'), ('G', 'L')])

# adding cpds
student_model.add_cpds(difficulty_cpd, intelligence_cpd, sat_cpd, grade_cpd, letter_cpd)


model_name = "student"
# json dump part
import json

data = {    "name"              : "student",
            "short_description" : "give short desc here",
            "long_description"  : "give long desc here",
            "nodes"           : {"L":"Letter", "D":"Difficulty", "G":"Grade", "I":"Intelligence", "S":"SAT Scores"}
        }

# with open('./data/model.json', 'r+') as f:
#     model_json = json.load(f)
#     model_list = model_json["list"]
#
#     if model_name not in model_list:
#         model_list.append[model_name]
#
#     model_json["list"] = model_list
#
#     f.seek(0)        # <--- should reset file position to the beginning.
#     json.dump(model_json, f, indent=4)
#     f.truncate()


with open('./data/student.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)



# pickle dump part
import pickle

pickle_out = open("./models/student.pickle","wb")
pickle.dump(student_model, pickle_out)
pickle_out.close()

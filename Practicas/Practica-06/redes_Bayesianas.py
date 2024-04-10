#!pip install pgmpy
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Se define la red bayesiana
# La satisfacción laboral está influenciada directamente por el balance
# trabajo-vida(B->S), el cual a su vez depende de las horas de trabajo(H->B)
modelo = BayesianNetwork([('B', 'S'), ('H', 'B')])

cpd_h = TabularCPD(variable='H',
                   variable_card=3, values=[[0.24], [0.72], [0.04]], #Probabilidades
                   state_names={'H': ['Largas', 'Moderadas', 'Cortas']})

cpd_b = TabularCPD(variable='B', variable_card=2,
                      values=[[0.13, 0.35, 0.72], #Probabilidades
                              [0.87, 0.65, 0.28]],
                      evidence=['H'],
                      evidence_card=[3],
                      state_names={'B': ['Equilibrado', 'No equilibrado'],
                                   'H': ['Largas', 'Moderadas', 'Cortas']})

cpd_s = TabularCPD(variable='S', variable_card=3,
                      values=[[0.37, 0.02], #Probabilidades
                              [0.49, 0.29],
                              [0.14, 0.69]],
                      evidence=['B'],
                      evidence_card=[2],
                      state_names={'S': ['Satisfecho', 'Neutral', 'Insatisfecho'],
                                   'B': ['Equilibrado', 'No equilibrado']})

print(cpd_h)
print(cpd_b)
print(cpd_s)
# Se agregan tablas de probabilidad condicional a la red bayesiana
modelo.add_cpds(cpd_h)
modelo.add_cpds(cpd_b)
modelo.add_cpds(cpd_s)
# Se checa que la suma de las tablas de 1
print(modelo.check_model())

from pgmpy.inference import VariableElimination

inferencia = VariableElimination(modelo)
# Se obtiene las probabilidades de la variable S cuando tiene horas de trabajo moderadas y un balance trabajo-vida equilibrado
probabilidades_s = inferencia.query(variables = ['S'], evidence = {'B': 'Equilibrado', 'H': 'Moderadas'})
# Se imprime la primera probabilidad de S, cuando está satisfecho
print(probabilidades_s.values[0])
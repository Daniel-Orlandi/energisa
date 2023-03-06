import pandas as pd
class DataHandler:       
    @staticmethod
    def agg_time_data(dataframe)->pd.DataFrame:
        tot_mens = 0
        result_list = []
        for idx, row in dataframe.iterrows():
          tot_mens = tot_mens + int(row[0])  
          result = pd.DataFrame({'Classe Consumo':[idx[0]],'UF':[idx[1]],'data':[idx[2]], 'count':[row[0]], 'tot_mens':[tot_mens]})        
          result_list.append(result)
        return pd.concat(result_list, ignore_index=True)
    
    @staticmethod
    def agg_agent_data(dataframe):
      tot_mens = 0
      result_list = []
      for idx, row in dataframe.iterrows():
        tot_mens = tot_mens + int(row[0])  
        result = pd.DataFrame({'Agente':[idx[0]],'Classe Consumo':[idx[2]],'UF':[idx[1]],'count':[row[0]], 'tot_emp':[tot_mens]})        
        result_list.append(result)
      return pd.concat(result_list, ignore_index=True)

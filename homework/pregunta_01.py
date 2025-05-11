"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel



def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    
    import pandas as pd
    df_dict = {
      "cluster": [],
      "cantidad_de_palabras_clave": [],
      "porcentaje_de_palabras_clave": [],
      "principales_palabras_clave": []
    }
    
    with open("./files/input/clusters_report.txt", "r") as f:
      lines = list(f.readlines())
      lines = [line.strip("\n").replace(" %", "").split() for line in lines]
      cluster = int()
      num_of_keywords = int()
      percentage = float()
      main_keywords = ""
      for line in lines[4:]:
          if len(line) == 0:
              df_dict["cluster"].append(cluster)
              df_dict["cantidad_de_palabras_clave"].append(num_of_keywords)
              df_dict["porcentaje_de_palabras_clave"].append(percentage)
              df_dict["principales_palabras_clave"].append(main_keywords[:-1])
              cluster = int()
              num_of_keywords = int()
              percentage = float()
              main_keywords = ""
              continue
          try:
              cluster = int(line[0])
              num_of_keywords = int(line[1])
              percentage = float(line[2].replace(",", "."))
              for word in line[3:]:
                  main_keywords += word.replace(".", "") + " "
          except:
              for word in line:
                  main_keywords += word.replace(".", "") + " "
      return pd.DataFrame().from_dict(df_dict)
      
    
    
  
  

if __name__ == "__main__":
    print(pregunta_01())
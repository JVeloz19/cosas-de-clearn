def tareas_sobre_k(t,k):
   if t != []:
      tareas = t[0][2]
      suma = 0
      for i in tareas:
         suma += i
      lista = tareas_sobre_k(t[1:],k)
      if suma/len(tareas) > k:
         lista.append(t[0][0])
      return lista
   return []
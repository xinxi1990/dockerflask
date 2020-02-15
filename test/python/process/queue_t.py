

import queue

# q = queue.Queue() # 先进先出
q = queue.LifoQueue() # 先进后出

q = queue.PriorityQueue() # 优先级队列,

# q.put(1)
# q.put(2)
# q.put(3)


q.put((1,'11')) # 优先级队列添加的参数是一个元组,元组元素为优先
q.put((2,'22'))
q.put((3,'33'))
q.put((4,'44'))
print(q.get())

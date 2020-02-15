
import pdb

def countnumber(number):
  for i in range(number):
    print(i)
    pdb.set_trace()

if __name__ == '__main__':
  countnumber(10)
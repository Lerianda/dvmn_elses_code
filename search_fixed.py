from random import sample


def s(list_, target):
  index = list_.index(target) if target in list_ else -1
  return index

def get_num_0_100():
    user_num = -1
    while user_num > 100 or user_num < 0:
        try:
            user_num = int(input('Pick a number between 0-100: '))
        except ValueError:
            print("That's not a number.")
    return user_num


if __name__ == "__main__":
  list_len = 10
  rand_list = sorted(sample(range(0, 101, 1), list_len))
  target = get_num_0_100()
  target_index = s(rand_list, target)
  
  print(f'\nList: {rand_list}')
  if target_index > -1:
      print(f'Found {target} in index {target_index}')
  else:
      print(f'Cannot find {target} in the list')

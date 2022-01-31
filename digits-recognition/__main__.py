from random import randint

bias = 7
target = 5
sensors = 15
training_iterations = 10000
weights = [0 for i in range(sensors)]

def increase(numbers):
  for i in range(sensors):
    if numbers[i] == '1':
      weights[i] += 1

def decrease(numbers):
  for i in range(sensors):
    if numbers[i] == '1':
      weights[i] -= 1

def proceed(numbers):<
  net = 0
  for i in range(sensors):
    net += int(numbers[i]) * weights[i]

  return net >= bias

def train(iterations, target, numbers):
  for i in range(iterations):
    random_number = randint(0, 9)

    if random_number != target:
      random_number_value = numbers[random_number]

      if proceed(random_number_value) == True:
        decrease(random_number_value)
    else:
      target_number = numbers[target]

      if proceed(target_number) == False:
        increase(target_number)

def run():
  zero = list('111101101101111')
  one = list('001001001001001')
  two = list('111001111100111')
  three = list('111001111001111')
  four = list('101101111001001')
  five = list('111100111001111')
  six = list('111100111101111')
  seven = list('111001001001001')
  eight = list('111101111101111')
  nine =  list('111101111001111')

  fake_five_first = list('111100111000111')
  fake_five_second = list('111100010001111')
  fake_five_third = list('111100011001111')
  fake_five_fourth = list('110100111001111')
  fake_five_fifth = list('110100111001011')
  fake_five_sixth = list('111100101001111')

  all_numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
  train(training_iterations, target, all_numbers)

  # All weights
  print(f'Weights: {weights}')

  # Run on training set
  print(f'0 is {target}?', proceed(zero))
  print(f'1 is {target}?', proceed(one))
  print(f'2 is {target}?', proceed(two))
  print(f'3 is {target}?', proceed(three))
  print(f'4 is {target}?', proceed(four))
  print(f'5 is {target}?', proceed(five))
  print(f'6 is {target}?', proceed(six))
  print(f'7 is {target}?', proceed(seven))
  print(f'8 is {target}?', proceed(eight))
  print(f'9 is {target}?', proceed(nine))

  # Run on test set
  print(f'{target} is 5.1? ', proceed(fake_five_first))
  print(f'{target} is 5.2? ', proceed(fake_five_second))
  print(f'{target} is 5.3? ', proceed(fake_five_third))
  print(f'{target} is 5.4? ', proceed(fake_five_fourth))
  print(f'{target} is 5.5? ', proceed(fake_five_fifth))
  print(f'{target} is 5.6? ', proceed(fake_five_sixth))

run()
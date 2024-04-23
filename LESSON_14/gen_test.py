# yield indicates that the function is a generator
# when we call a generator, a generator object is created, not a function is executed
# until we ask the generator will not work
# the generator is disposable and runs out
def square():
    print("Generator working ... ")
    for e in range(1, 11, 2):
        yield e ** 2  # stop, execution is paused


def pause():
    print('Generator working....')
    while True:
        print(a)
        yield a # stop, execution is paused before next()


if __name__ == '__main__':
    ##########
    gen = square()
    print(gen)  # <generator object square at 0x00000245517D6970>
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))  # StopIteration
    #####################
    gen_2 = pause()
    print(dir(gen_2))
    a = 10
    next(gen_2)
    next(gen_2)
    a = 20
    next(gen_2)

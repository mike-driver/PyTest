def test_string_printing():
    print("printing strings".upper())
    print("Hello world")
    text1 = "Home Log Cabin"
    print(text1[:])
    print(text1[0:3])
    print(text1[-1:])

def some_maths():
    print("some maths".upper())
    int1 = 3
    float1 = 1.414
    is_true = True
    print(int1)
    print(float1)
    print(is_true)
    print(type(is_true))

def loop_in_range():
    for x in range(0, 3):
        print("X is equal to %d" % (x))
        print(f"X is equal to {x}")
    print("\n")
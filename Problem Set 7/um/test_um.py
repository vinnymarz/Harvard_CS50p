from um import count

def test_count_with_um():
    assert count("um, that's um... umm, um.") == 3

def test_count_without_um():
    assert count("That's just a dummy text.") == 0

def test_count_with_mixed_case():
    assert count("Um, who said Um?") == 2



if __name__ == '__main__':
    main()

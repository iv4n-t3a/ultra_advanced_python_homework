from base_singleton import BaseSingleton
from singleton_decorator import singleton_decorator
from singleton_class_variable import SingletonClass


def test_singleton_class_variable():
    instance1 = SingletonClass()
    instance2 = SingletonClass()

    assert instance1 is not None
    assert instance1 is instance2
    assert id(instance1) == id(instance2)


def test_base_singleton():
    class InheritSingletonClass(BaseSingleton):
        pass

    instance1 = InheritSingletonClass()
    instance2 = InheritSingletonClass()

    assert instance1 is not None
    assert instance1 is instance2
    assert id(instance1) == id(instance2)


def test_base_singleton_different_classes():
    class InheritSingletonClass1(BaseSingleton):
        pass

    class InheritSingletonClass2(BaseSingleton):
        pass

    instance1 = InheritSingletonClass1()
    instance2 = InheritSingletonClass2()

    assert instance1 is not None
    assert instance2 is not None
    assert instance1 is not instance2
    assert id(instance1) != id(instance2)


def test_singleton_decorator():
    @singleton_decorator
    class SingletonDecorated:
        pass

    instance1 = SingletonDecorated()
    instance2 = SingletonDecorated()

    assert instance1 is not None
    assert instance1 is instance2
    assert id(instance1) == id(instance2)


def test_singleton_decorator_different_classes():
    @singleton_decorator
    class SingletonDecorated1:
        pass

    @singleton_decorator
    class SingletonDecorated2:
        pass

    instance1 = SingletonDecorated1()
    instance2 = SingletonDecorated2()

    assert instance1 is not None
    assert instance2 is not None
    assert instance1 is not instance2
    assert id(instance1) != id(instance2)

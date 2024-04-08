# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import b as module_0


def test_case_0():
    bool_0 = True
    queue_0 = module_0.Queue(bool_0)
    assert f"{type(queue_0).__module__}.{type(queue_0).__qualname__}" == "b.Queue"
    assert queue_0.max is True
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert (
        f"{type(queue_0.data).__module__}.{type(queue_0.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_0.data) == 1
    var_0 = queue_0.dequeue()


def test_case_1():
    bool_0 = False
    with pytest.raises(AssertionError):
        module_0.Queue(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 243
    queue_0 = module_0.Queue(int_0)
    assert f"{type(queue_0).__module__}.{type(queue_0).__qualname__}" == "b.Queue"
    assert queue_0.max == 243
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert (
        f"{type(queue_0.data).__module__}.{type(queue_0.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_0.data) == 243
    bool_0 = queue_0.enqueue(int_0)
    assert bool_0 is True
    assert queue_0.tail == 1
    assert queue_0.size == 1
    queue_1 = module_0.Queue(int_0)
    assert queue_1.head == 0
    assert queue_1.tail == 0
    assert queue_1.size == 0
    module_0.Queue(queue_1)


def test_case_3():
    bool_0 = True
    int_0 = 651
    queue_0 = module_0.Queue(int_0)
    assert f"{type(queue_0).__module__}.{type(queue_0).__qualname__}" == "b.Queue"
    assert queue_0.max == 651
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert (
        f"{type(queue_0.data).__module__}.{type(queue_0.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_0.data) == 651
    var_0 = queue_0.dequeue()
    var_1 = queue_0.dequeue()
    queue_1 = module_0.Queue(bool_0)
    assert f"{type(queue_1).__module__}.{type(queue_1).__qualname__}" == "b.Queue"
    assert queue_1.max is True
    assert queue_1.head == 0
    assert queue_1.tail == 0
    assert queue_1.size == 0
    assert (
        f"{type(queue_1.data).__module__}.{type(queue_1.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_1.data) == 1
    bool_1 = queue_1.empty()
    assert bool_1 is False
    queue_2 = module_0.Queue(bool_0)
    assert queue_2.head == 0
    assert queue_2.tail == 0
    assert queue_2.size == 0
    bool_2 = queue_1.empty()
    assert bool_2 is False
    bool_3 = queue_1.full()
    assert bool_3 is False
    var_2 = queue_2.dequeue()


def test_case_4():
    bool_0 = True
    queue_0 = module_0.Queue(bool_0)
    assert f"{type(queue_0).__module__}.{type(queue_0).__qualname__}" == "b.Queue"
    assert queue_0.max is True
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert (
        f"{type(queue_0.data).__module__}.{type(queue_0.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_0.data) == 1
    bool_1 = queue_0.enqueue(bool_0)
    assert bool_1 is True
    assert queue_0.size == 1
    queue_1 = module_0.Queue(bool_0)
    assert queue_1.head == 0
    assert queue_1.size == 0
    bool_2 = queue_1.empty()
    assert bool_2 is False
    var_0 = queue_0.dequeue()
    assert var_0 == 1
    assert queue_0.size == 0
    bool_3 = queue_1.empty()
    assert bool_3 is False
    bool_4 = queue_1.empty()
    assert bool_4 is False
    bool_5 = queue_0.enqueue(bool_4)
    assert bool_5 is True
    assert queue_0.size == 1
    queue_2 = module_0.Queue(bool_0)
    assert queue_2.size == 0
    bool_6 = queue_2.full()
    assert bool_6 is False
    bool_7 = queue_0.empty()
    assert bool_7 is True
    bool_8 = queue_0.full()
    assert bool_8 is True
    bool_9 = True
    queue_3 = module_0.Queue(bool_9)
    assert queue_3.size == 0
    var_1 = queue_2.dequeue()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    queue_0 = module_0.Queue(bool_0)
    assert f"{type(queue_0).__module__}.{type(queue_0).__qualname__}" == "b.Queue"
    assert queue_0.max is True
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert (
        f"{type(queue_0.data).__module__}.{type(queue_0.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_0.data) == 1
    bool_1 = queue_0.enqueue(bool_0)
    assert bool_1 is True
    assert queue_0.size == 1
    queue_1 = module_0.Queue(bool_0)
    assert queue_1.head == 0
    assert queue_1.size == 0
    bool_2 = queue_1.empty()
    assert bool_2 is False
    var_0 = queue_0.dequeue()
    assert var_0 == 1
    assert queue_0.size == 0
    bool_3 = queue_1.empty()
    assert bool_3 is False
    var_1 = queue_1.dequeue()
    bool_4 = queue_1.empty()
    assert bool_4 is False
    bool_5 = queue_0.enqueue(bool_4)
    assert bool_5 is True
    assert queue_0.size == 1
    bool_6 = queue_0.enqueue(bool_2)
    assert bool_6 is False
    module_0.Queue(var_1)


def test_case_6():
    bool_0 = True
    int_0 = 651
    queue_0 = module_0.Queue(int_0)
    assert f"{type(queue_0).__module__}.{type(queue_0).__qualname__}" == "b.Queue"
    assert queue_0.max == 651
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert (
        f"{type(queue_0.data).__module__}.{type(queue_0.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_0.data) == 651
    var_0 = queue_0.dequeue()
    var_1 = queue_0.dequeue()
    queue_1 = module_0.Queue(bool_0)
    assert f"{type(queue_1).__module__}.{type(queue_1).__qualname__}" == "b.Queue"
    assert queue_1.max is True
    assert queue_1.head == 0
    assert queue_1.tail == 0
    assert queue_1.size == 0
    assert (
        f"{type(queue_1.data).__module__}.{type(queue_1.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_1.data) == 1
    bool_1 = queue_1.empty()
    assert bool_1 is False
    queue_2 = module_0.Queue(bool_0)
    assert queue_2.head == 0
    assert queue_2.tail == 0
    assert queue_2.size == 0
    bool_2 = queue_1.empty()
    assert bool_2 is False
    bool_3 = queue_0.enqueue(bool_0)
    assert bool_3 is True
    assert queue_0.tail == 1
    assert queue_0.size == 1
    bool_4 = queue_1.full()
    assert bool_4 is False
    bool_5 = queue_2.full()
    assert bool_5 is False
    bool_6 = queue_1.full()
    assert bool_6 is False
    var_2 = queue_0.dequeue()
    assert var_2 == 1
    assert queue_0.head == 1
    assert queue_0.size == 0
    var_3 = queue_1.dequeue()

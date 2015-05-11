import asyncio

@asyncio.coroutine
def test1(future):
    yield from asyncio.sleep(5)
    future.set_result("test1 sleep 5s")

@asyncio.coroutine
def test2(future):
    yield from asyncio.sleep(8)
    future.set_result("test2 sleep 8s")

@asyncio.coroutine
def test3(future):
    yield from asyncio.sleep(2)
    future.set_result("test3 sleep 2s")
    print("call test4")
    asyncio.async(test4(loop))

def result(future):
    print(future.result())

@asyncio.coroutine
def test4(loop):
    yield from asyncio.sleep(10)
    print("test4 sleep 10s")
    loop.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    print(loop)

    print("call test1")
    future1 = asyncio.Future()
    asyncio.async(test1(future1))
    future1.add_done_callback(result)

    print("call test2")
    future2 = asyncio.Future()
    asyncio.async(test2(future2))
    future2.add_done_callback(result)

    print("call test3")
    future3 = asyncio.Future()
    asyncio.async(test3(future3))
    future3.add_done_callback(result)

#     print("call test4")
#     asyncio.async(test4(loop))

    print("call end")
    try:
        loop.run_forever()
    finally:
        loop.close()

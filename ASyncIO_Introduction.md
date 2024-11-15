# What is `asyncio`?
`asyncio` is a Python library used to write concurrent code using the `async`/`await` syntax. It provides a framework for asynchronous programming, allowing you to manage multiple tasks that run concurrently. This is particularly useful for I/O-bound and high-level structured network code, not particulairily parallel processing.

## Asynchronous Programming
In traditional synchronous programming, operations are executed one after another. If an operation involves waiting, like for a network request or file I/O, the entire program pauses until that operation completes. Asynchronous programming, on the other hand, enables your program to continue running other tasks while waiting for an I/O operation to finish.

## Key Concepts in `asyncio`

1. **Event Loop**: The core of `asyncio` is the event loop. It is responsible for managing and dispatching tasks, running `async` functions, and handling events. The event loop repeatedly checks for tasks that are ready to execute and manages scheduling.
   
2. **Coroutines**: Coroutines are functions defined with `async def`. They can be paused and resumed, making them ideal for asynchronous operations. When a coroutine calls `await`, it pauses, allowing the event loop to execute other tasks until the awaited operation is complete.
   
3. **Tasks**: A `Task` in `asyncio` is a coroutine that has been scheduled to run on the event loop. The event loop handles when and how the task is executed, ensuring efficient concurrent execution. Tasks are often created using `asyncio.create_task()`.

4. **Awaitable Objects**: These are objects that can be awaited, like coroutines or special objects provided by `asyncio`. When you use `await`, Python pauses the execution of the coroutine until the awaitable completes, then resumes execution with the result of the awaitable.

## How `asyncio` Works
Here's how `asyncio` manages asynchronous operations:

1. **Event Loop Management**: The event loop orchestrates running coroutines. When a coroutine calls `await`, the event loop can switch to another coroutine or task, ensuring that the program doesn't block while waiting for I/O operations.

2. **Non-Blocking I/O**: `asyncio` uses non-blocking I/O, which means that instead of waiting for an operation to complete (like a file read or network request), it continues to handle other tasks. This is efficient for I/O-bound applications, like web servers or chat applications.

3. **Concurrency, Not Parallelism**: `asyncio` provides concurrency but not true parallelism. It allows a single-threaded program to handle many tasks seemingly at once, but it does not run tasks on multiple cores simultaneously. For CPU-bound tasks that require parallel execution, you should use multi-threading or multiprocessing.

[PLEASE Review Example Code Using `asyncio`](asyncio_example.py)

## When to Use `asyncio`
* **I/O-bound Applications**: Great for programs that need to handle many I/O operations, such as web scraping, chat applications, or network servers.
* **Network Clients/Servers**: Efficiently manage multiple network connections, like handling thousands of clients in a server application.
* **Asynchronous Libraries**: Use `asyncio` when working with libraries that support asynchronous operations.

## Limitations
* **Not for CPU-bound Tasks**: `asyncio` is not ideal for tasks that require significant CPU resources, as it runs on a single thread. For CPU-heavy work, consider `concurrent.futures` with a `ThreadPoolExecutor` or `ProcessPoolExecutor`.
* **Learning Curve**: Understanding the `async`/`await` model can be challenging, especially when dealing with complex flows or debugging.
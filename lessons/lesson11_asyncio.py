''' async and await are Python keywords used to write concurrent, 
non-blocking code using the built-in asyncio library. 
They allow your program to pause an ongoing task 
(like waiting for a database response or a web download) 
and automatically switch to another task, preventing your application from sitting idle.
asyncio.gather() --> Run these asynchronous operations concurrently and wait until all are finished.'''

import asyncio

async def fetch_data():
    print(f"Start fetching data ...")
    # simulate non-blocking network request
    await asyncio.sleep(2)
    print("Data fetching completed successfully....")
    return {'data':123}
async def main():
    #pauses main() until fetch_data() complete 
    result=await fetch_data()
    print(f"Result received : {result}")

# Starts the event loop and executes the coroutine
asyncio.run(main())
    
#Advanced Example (Concurrent Execution)
''' To truly see the speed benefits of asynchronous code, you must run multiple tasks simultaneously 
using tools like asyncio.gather().Instead of waiting 2 + 3 = 5 seconds sequentially, 
the program finishes both operations concurrently in just 3 seconds'''

import time

async def download(fileid:str,duration:int)-> None:
    print(f"Started Downloading fileid {fileid}...")
    await asyncio.sleep(duration) # Yields control back to the event loop
    print(f"Finished the downloading fileid{fileid}")

async def main():
    start_time=time.time()  
    #run the both downloads cuncurrantly 
    await asyncio.gather(
        download("A1",2),
        download("A2",3)
    )
    end_time=time.time()
    print(f"Total files download time with cuncurrant:{end_time-start_time:.2f} seconds")

asyncio.run(main())    

## Example without Cuncurrant

async def downloadwo(fileid:str,duration:int)->None:
    print(f"start file download fileid {fileid}")
    await asyncio.sleep(duration)
    print("File download complete")

async def main():
    start_time=time.time()
    # downloadwo("Task1",2) ## Throws error -RuntimeWarning: coroutine 'downloadwo' was never awaited
    # downloadwo("Task2",3) ## without await it give error while calling function
    await downloadwo("Task1",2)
    await downloadwo("Task2",3)
    stop_time=time.time()

    print(f"Total files download time without cuncurrant:{stop_time-start_time:.2f} seconds")    

asyncio.run(main())    
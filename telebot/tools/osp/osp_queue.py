import asyncio


osp_queue = asyncio.Queue()

worker_started = False



async def add_osp_job(
    user_id,
    shd,
    callback
):

    job = {
        "user_id": user_id,
        "shd": shd,
        "callback": callback
    }


    await osp_queue.put(job)


    return osp_queue.qsize()



async def osp_worker():

    global worker_started


    if worker_started:
        return


    worker_started = True


    print(
        "🛠 OSP Queue Worker started"
    )


    while True:

        job = await osp_queue.get()


        try:

            await job["callback"](
                job["user_id"],
                job["shd"]
            )


        except Exception as e:

            print(
                "OSP JOB ERROR:",
                e
            )


        finally:

            osp_queue.task_done()

import asyncio
import cProfile
import pstats

from download import main  # 你的异步主函数

profiler = cProfile.Profile()
profiler.enable()
asyncio.run(main())
profiler.disable()

# 生成调用图
stats = pstats.Stats(profiler)
stats.dump_stats("profile.prof")

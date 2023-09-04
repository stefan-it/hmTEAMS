import nvidia_smi
import logging

from flair.trainers.plugins.base import TrainerPlugin

logger = logging.getLogger("flair")


class GpuStatsPlugin(TrainerPlugin):
    def __init__(self) -> None:
        super().__init__()
        nvidia_smi.nvmlInit()

        # Always use first GPU
        handle = nvidia_smi.nvmlDeviceGetHandleByIndex(0)
        self.memory = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)

    @TrainerPlugin.hook
    def after_training_epoch(self, epoch, **kw):
        gpu_memory_used_mb = self.memory.used // 1024**2
        gpu_total_memory_mb = self.memory.total // 1024**2
        logger.info("GPU Memory Stats: {}MB / {}MB used".format(gpu_memory_used_mb, gpu_total_memory_mb))

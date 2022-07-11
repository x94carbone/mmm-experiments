import logging
import signal

from mmm_experiments.agents.joint import MonarchPDFSubjectBMM

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    try:
        agent = MonarchPDFSubjectBMM(
            sample_origin=(69.2, 2.0),
            relative_bounds=(-30, 30),
            Cu_origin=(155.390, 83.96),
            Ti_origin=(155.381, 82.169),
            Cu_det_position=205,
            Ti_det_position=20,
            bmm_bounds=(-30, 23),
            bmm_time_window=30,
        )
        signal.signal(signal.SIGINT, agent.signal_handler)
        agent.start(ask_at_start=True)
    except Exception as e:
        agent.stop(exit_status="fail", reason=f"{e}")
        raise e

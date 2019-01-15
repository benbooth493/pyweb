from gaiasdk import sdk
import logging


def MyAwesomeJob(args):
    logging.info("MyAwesomeJob is running")


def main():
    logging.basicConfig(level=logging.INFO)
    myjob = sdk.Job("MyAwesomeJob", "Do something awesome", MyAwesomeJob)
    sdk.serve([myjob])

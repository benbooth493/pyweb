from gaiasdk import sdk
import logging


def build_container(args):
    logging.info("building container..")


def run_container(args):
    logging.info("run container..")


def main():
    logging.basicConfig(level=logging.INFO)
    build = sdk.Job(
        "Build Container", "building pyweb image", build_container)

    run = sdk.Job(
        "Run Container", "running pyweb image", run_container)

    sdk.serve([
        build,
        run,
    ])

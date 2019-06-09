from workaction import WorkAction
from assignaction import AssignAction
from constant import VERSION, LOGGER
import logging
import click
# import argparse

# parser = argparse.ArgumentParser(description="Default argument parser")
# parser.add_argument("workwork")
# parser.add_argument("--version", action="version", version="jirator %s" % (VERSION), help="show the current jirator version information")
# parser.add_argument("work", action=WorkAction, nargs='?', help="select issue from list and checkout to that branch")
# parser.add_argument("assign", action=AssignAction, nargs='?', help="manually provide issue number and assign it to you, and automatically move it to an in progress state")
# parser.add_argument("--verbose", "-v", action="store_true", default=False, help="enable debug logging")

def set_log_level(ctx,param,value):
    if value == True:
        logging.basicConfig(level="DEBUG",format="%(levelname)s: %(message)s")
    else:
        logging.basicConfig(level="INFO",format="%(message)s")
    logging.debug("enable debug logging")

@click.group()
@click.option("--verbose","-v",default=False, is_flag=True, help="enable debug logging",expose_value=True,is_eager=True, callback=set_log_level)
@click.version_option(None, "--version", message="jirator v%(version)s")
def main(verbose):
    logging.debug("in main")

@click.command()
@click.argument("issue")
def assign(issue):
    logging.info("assigning issue '%s'" % (issue))
    a = AssignAction()(issue)

@click.command()
def work():
    w = WorkAction()
    w()

main.add_command(assign)
main.add_command(work)

if __name__== '__main__':
    main()

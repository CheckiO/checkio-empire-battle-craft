import sys
from checkio_executor_python.client import ClientLoop
from checkio_executor_python.execs import Runner

Runner.ALLOWED_MODULES += ['battle', 'battle.commander']

ClientLoop(int(sys.argv[1]), sys.argv[2]).start()

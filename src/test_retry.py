from src.retry import retry
from src.flaky import flaky_operation

retry(flaky_operation)

from prometheus_client import (
    Counter,
    Histogram,
    CollectorRegistry
)

registry = CollectorRegistry()

# TOTAL REQUESTS
REQUEST_COUNT = Counter(
    "chaosforge_requests_total",
    "Total API Requests",
    ["method", "endpoint"],
    registry=registry
)

# TOTAL ERRORS
ERROR_COUNT = Counter(
    "chaosforge_errors_total",
    "Total Error Responses",
    registry=registry
)

# REQUEST LATENCY
REQUEST_LATENCY = Histogram(
    "chaosforge_request_latency_seconds",
    "API Request Latency",
    registry=registry
)

# CPU CHAOS
CPU_BURN_COUNT = Counter(
    "chaosforge_cpu_burn_total",
    "Total CPU Burn Simulations",
    registry=registry
)

# MEMORY CHAOS
MEMORY_LEAK_COUNT = Counter(
    "chaosforge_memory_leak_total",
    "Total Memory Leak Simulations",
    registry=registry
)
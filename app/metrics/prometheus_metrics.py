from prometheus_client import Counter, Gauge

# Total requests
REQUEST_COUNT = Counter(
    "chaosforge_requests_total",
    "Total API requests"
)

# Error mode state
ERROR_MODE = Gauge(
    "chaosforge_error_mode",
    "Whether application is in error mode"
)
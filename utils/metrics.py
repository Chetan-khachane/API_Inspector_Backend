
# utils/metrics.py

def avg_latency(latencies):
    return sum(latencies) / len(latencies)


def min_latency(latencies):
    return min(latencies)


def max_latency(latencies):
    return max(latencies)

def success_rate(success_count, total_requests):
    return (success_count / total_requests) * 100

def error_rate(error_count,total_requests):
    return (error_count / total_requests) *100

def calculate_performance(latencies,success_count,error_count,total_requests):
    
    return {
        "avg_latency" : avg_latency(latencies),
        "min_latency" : min_latency(latencies),
        "max_latency" : max_latency(latencies),
        "success_rate" : success_rate(success_count,total_requests),
        "total_requests" : total_requests,
        "error_rate" : error_rate(error_count,total_requests)
    }
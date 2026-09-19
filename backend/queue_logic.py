def calculate_waiting_time(queue_length, service_time_seconds):
    """
    Calculate approximate waiting time for people in the queue.
    """

    waiting_time_seconds = queue_length * service_time_seconds
    waiting_time_minutes = waiting_time_seconds / 60

    return waiting_time_minutes


def calculate_congestion(queue_length):
    """
    Determine congestion level based on the number of people waiting.
    """

    if queue_length < 10:
        return "Low"

    elif queue_length < 25:
        return "Moderate"

    elif queue_length < 50:
        return "High"

    else:
        return "Very High"


def calculate_trend(arrival_rate, service_rate):
    """
    Compare arrival rate and service rate to determine crowd trend.
    """

    if arrival_rate > service_rate:
        return "Increasing"

    elif arrival_rate < service_rate:
        return "Decreasing"

    else:
        return "Stable"


def recommend_visit(trend, congestion):
    """
    Give a simple recommendation based on crowd conditions.
    """

    if trend == "Increasing" and congestion in ["High", "Very High"]:
        return "Avoid now - visit later"

    elif trend == "Increasing":
        return "Consider visiting later"

    elif trend == "Decreasing":
        return "Good time to visit"

    else:
        return "Normal - monitor queue"


# -----------------------------------
# QueueLess Test
# -----------------------------------

if __name__ == "__main__":

    queue_length = 47
    service_time_seconds = 38

    arrival_rate = 8
    service_rate = 10

    waiting_time = calculate_waiting_time(
        queue_length,
        service_time_seconds
    )

    congestion = calculate_congestion(queue_length)

    trend = calculate_trend(
        arrival_rate,
        service_rate
    )

    recommendation = recommend_visit(
        trend,
        congestion
    )

    print("================================")
    print("        QUEUELESS SYSTEM")
    print("================================")

    print("People waiting       :", queue_length)
    print("Service time/person  :", service_time_seconds, "seconds")
    print("Estimated wait       :", round(waiting_time, 2), "minutes")

    print("Arrival rate         :", arrival_rate, "people/min")
    print("Service rate         :", service_rate, "people/min")

    print("Crowd trend          :", trend)
    print("Congestion level     :", congestion)
    print("Recommendation       :", recommendation)

    print("================================")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from queue_logic import (
    calculate_waiting_time,
    calculate_congestion,
    calculate_trend,
    recommend_visit
)


app = FastAPI(
    title="QueueLess API",
    description="Real-time queue monitoring and optimization backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "QueueLess API is running!"
    }


@app.get("/queue")
def get_queue():

    queue_length = 47
    service_time_seconds = 38

    arrival_rate = 8
    service_rate = 10

    waiting_time = calculate_waiting_time(
        queue_length,
        service_time_seconds
    )

    congestion = calculate_congestion(
        queue_length
    )

    trend = calculate_trend(
        arrival_rate,
        service_rate
    )

    recommendation = recommend_visit(
        trend,
        congestion
    )

    return {
        "people_waiting": queue_length,
        "service_time_seconds": service_time_seconds,
        "estimated_wait_minutes": round(waiting_time, 2),
        "arrival_rate": arrival_rate,
        "service_rate": service_rate,
        "crowd_trend": trend,
        "congestion_level": congestion,
        "recommendation": recommendation
    }

@app.get("/simulate")
def simulate_queue():

    import random

    queue_length = random.randint(5, 60)

    service_time_seconds = random.randint(25, 50)

    arrival_rate = random.randint(5, 15)

    service_rate = round(60 / service_time_seconds, 2)

    waiting_time = calculate_waiting_time(
        queue_length,
        service_time_seconds
    )

    congestion = calculate_congestion(
        queue_length
    )

    trend = calculate_trend(
        arrival_rate,
        service_rate
    )

    recommendation = recommend_visit(
        trend,
        congestion
    )

    return {
        "people_waiting": queue_length,
        "service_time_seconds": service_time_seconds,
        "estimated_wait_minutes": round(waiting_time, 2),
        "arrival_rate": arrival_rate,
        "service_rate": service_rate,
        "crowd_trend": trend,
        "congestion_level": congestion,
        "recommendation": recommendation
    }
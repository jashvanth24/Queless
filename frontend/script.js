async function loadQueueData() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/simulate"
        );

        if (!response.ok) {
            throw new Error("Unable to get queue data");
        }

        const data = await response.json();


        // People waiting
        document.getElementById("people-waiting").textContent =
            data.people_waiting;


        // Waiting time
        document.getElementById("waiting-time").textContent =
            data.estimated_wait_minutes + " min";


        // Congestion
        document.getElementById("congestion").textContent =
            data.congestion_level;


        // Crowd trend
        document.getElementById("trend").textContent =
            data.crowd_trend;


        // Recommendation
        document.getElementById("recommendation").textContent =
            data.recommendation;

    }

    catch (error) {

        console.error("QueueLess Error:", error);

        document.getElementById("recommendation").textContent =
            "Unable to connect to QueueLess server.";
    }
}


// Load data immediately
loadQueueData();


// Refresh queue data every 5 seconds
setInterval(loadQueueData, 5000);
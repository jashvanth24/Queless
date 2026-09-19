async function loadQueueData() {

    try {

        const response = await fetch("http://127.0.0.1:8000/queue");

        if (!response.ok) {
            throw new Error("Unable to get queue data");
        }

        const data = await response.json();


        // Update People Waiting
        document.getElementById("people-waiting").textContent =
            data.people_waiting;


        // Update Waiting Time
        document.getElementById("waiting-time").textContent =
            data.estimated_wait_minutes + " min";


        // Update Congestion
        document.getElementById("congestion").textContent =
            data.congestion_level;


        // Update Crowd Trend
        document.getElementById("trend").textContent =
            data.crowd_trend;


        // Update Recommendation
        document.getElementById("recommendation").textContent =
            data.recommendation;

    }

    catch (error) {

        console.error("Error:", error);

        document.getElementById("recommendation").textContent =
            "Unable to connect to QueueLess server.";

    }
}


// Load queue data when the page opens
loadQueueData();
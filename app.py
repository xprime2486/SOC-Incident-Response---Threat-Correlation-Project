from flask import Flask, render_template
from correlate import correlate_logs
from severity import assign_severity

app = Flask(__name__)

@app.route("/")
def dashboard():
    data = correlate_logs()
    incidents = []

    for ip, info in data.items():
        incidents.append({
            "ip": ip,
            "events": info["count"],
            "event_types": ", ".join(set(info["events"])),
            "severity": assign_severity(info["count"])
        })

    return render_template("dashboard.html", incidents=incidents)


if __name__ == "__main__":
    app.run(debug=True)

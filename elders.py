from flask import Flask, render_template, request, jsonify
import ml_model  # Import your machine learning model module

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("elders.html")

@app.route("/register", methods=["POST"])
def register():
    # Get form data
    name = request.form.get("name")
    password = request.form.get("password")
    entered_age = int(request.form.get("age"))
    aadhar_image = request.files.get("aadharImage")

    # Calculate age from Aadhar image using machine learning model
    try:
        predicted_age = ml_model.predict_age(aadhar_image)
        predicted_age = int(predicted_age)  # Convert to integer
    except Exception as e:
        print("Error predicting age:", e)
        return jsonify({"success": False, "message": "Error predicting age"})

    # Verify age
    if predicted_age > 50 and predicted_age == entered_age:
        # Age verification successful
        return jsonify({"success": True, "message": "Signed up successfully!"})
    else:
        # Age verification failed
        return jsonify({"success": False, "message": "Age verification failed"})

if __name__ == "__main__":
    app.run(debug=True)

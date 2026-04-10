from flask import jsonify , request
from . import api_bp
from app.service.mqtt_service import all_data, MQTT_BROKER, MQTT_TOPIC
from app.models import Test
from app import db





@api_bp.route("/")
def index():
    return "Hello World"

@api_bp.route("/data")
def show_data():
    return jsonify(all_data)

@api_bp.route("/debug")
def debug():
    return jsonify({
        "broker": MQTT_BROKER,
        "topic": MQTT_TOPIC,
        "devices_count": len(all_data)
    })




@api_bp.route("/add_test" , methods=["POST"])
def test():

    data = request.get_json()

    if not data or 'name' not in data:
        return jsonify({"error": "Missing 'name' in request body"}), 400


    try: 
        new_test = Test(name=data['name'])
        db.session.add(new_test)
        db.session.commit()

        return jsonify({
            "message": "Entry created successfully!",
            "id": new_test.id,
            "name": new_test.name
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500



@api_bp.route("/get_test")
def get_users():

    try:
        users = Test.query.all()
        return jsonify({
            "users": [{"id": user.id, "name": user.name} for user in users]
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
    
    

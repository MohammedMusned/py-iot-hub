import os




class Config:
    MQTT_BROKER = os.environ.get("MQTT_BROKER", "127.0.0.1")
    MQTT_TOPIC = os.environ.get("MQTT_TOPIC", "v1/data/#")
    SQLALCHEMY_DATABASE_URI = "sqlite:///iot.db"

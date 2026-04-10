import asyncio
import json
import threading
from collections import defaultdict
import aiomqtt
import os
from config import Config

# In-memory store: all messages per device
all_data = defaultdict(list)



#Read broker host from environment variable MQTT_BROKER.
#If not set, use "127.0.0.1".
MQTT_BROKER = Config.MQTT_BROKER 



#Read topic filter from env var MQTT_TOPIC.
#Default is v1/data/# (# means all subtopics under v1/data/).
MQTT_TOPIC = Config.MQTT_TOPIC







async def mqtt_listener():
    while True:
        try:

            #Connect to MQTT broker
            async with aiomqtt.Client(MQTT_BROKER) as client:



                #Subscribe to topic
                await client.subscribe(MQTT_TOPIC)
                print(f"✅ Subscribed to {MQTT_TOPIC}")

                #Listen for messages
                async for message in client.messages:

                    #Convert message to topic and String
                    topic = str(message.topic)  # e.g. v1/data/device1
                    payload_raw = message.payload.decode("utf-8") # actual message content sent on that topic.

                    try:
                        payload = json.loads(payload_raw)
                    except json.JSONDecodeError:
                        payload = {"raw": payload_raw}

                    parts = topic.split("/")
                    device_id = parts[-1] if parts else "unknown"

                    all_data[device_id].append({
                        "topic": topic,
                        "payload": payload
                    })

                    print(f"📥 Received from {device_id}: {payload}")

        except aiomqtt.MqttError as e:
            print(f"⚠️ MQTT error: {e}. Reconnecting in 5s...")
            await asyncio.sleep(5)

def start_mqtt_background_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(mqtt_listener())

def start_mqtt():
    # Start MQTT listener once when called
    threading.Thread(target=start_mqtt_background_loop, daemon=True).start()

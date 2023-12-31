import * as mqtt from "mqtt";
import { useEffect, useRef } from 'react';

const useMQTT = () => {

  const clientRef = useRef<mqtt.MqttClient>()

  useEffect(() => {
    // Connect to the MQTT broker
    var options: mqtt.IClientOptions = {
      port: 8884,
      protocol: 'wss',
      username: 'crustypi-ui',
      password: 'Crustyburger@123'
    }

    let client = mqtt.connect("wss://a91938236da5469ca7780ce25a489b8f.s2.eu.hivemq.cloud:8884", {
      ...options
    })

    client.on("connect", (packet) => {
      console.log("Connected")
    })

    client.on("disconnect", (packet) => {
      console.log("Disconnected")
    })

    client.on("error", (err) => {
      console.error(err)
    })

    client.subscribe('sensordata');

    client.on('message', (topic: any, message: any) => {
      console.log(`Received message on topic '${topic}': ${message.toString()}`);
    })

    // Clean up the MQTT client on component unmount
    return () => {
      client.end();
    }
  }, [])

  return {
    client: clientRef.current
  }
};

export default useMQTT;
import mqtt from 'mqtt';
import { useEffect, useRef } from 'react';

const useMQTT = () => {

  const clientRef = useRef<mqtt.MqttClient>()

  useEffect(() => {
    // Connect to the MQTT broker
    var options: mqtt.IClientOptions = {
      host: 'a91938236da5469ca7780ce25a489b8f.s2.eu.hivemq.cloud',
      port: 8883,
      protocol: 'mqtts',
      username: 'crustypi-ui',
      password: 'Crustyburger@123'
    }

    clientRef.current = mqtt.connect(options)

    clientRef.current.subscribe('sensordata');

    clientRef.current.on('message', (topic, message) => {
      console.log(`Received message on topic '${topic}': ${message.toString()}`);
    })

    // Clean up the MQTT client on component unmount
    return () => {
      clientRef.current?.end();
    }
  }, [])

  return {
    client: clientRef.current
  }
};

export default useMQTT;
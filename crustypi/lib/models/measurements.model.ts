import {Schema, model} from 'mongoose';

const measurementSchema = new Schema({
  temperature: {
    type: Number
  },
  humidity: {
    type: Number
  },
  pressure: {
    type: Number
  },
  timestamp: {
    type: Date
  },
  detectedMotion: {
    type: Boolean
  },
  gas: {
    type: Number
  }
});

measurementSchema.index({ timestamp: -1 });

const Measurement = model('Measurement', measurementSchema);
export default Measurement;
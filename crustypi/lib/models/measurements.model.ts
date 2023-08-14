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

measurementSchema.index({ timestamp: -1, temperature: 1 })

measurementSchema.index({ timestamp: -1, humidity: 1 })

measurementSchema.index({ timestamp: -1, pressure: 1 })

measurementSchema.index({ timestamp: -1, detectedMotion: 1 })

measurementSchema.index({ timestamp: -1, gas: 1 }, { partialFilterExpression: {'email': { $exists: true } } })

const Measurement = model('Measurement', measurementSchema);
export default Measurement;
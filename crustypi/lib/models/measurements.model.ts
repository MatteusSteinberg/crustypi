import mongoose from 'mongoose';

const measurementSchema = new mongoose.Schema({
  temperature: {
    type: Number,
    required: true
  },
  humidity: {
    type: Number,
    required: true
  },
  pressure: {
    type: Number,
    required: true
  },
  timestamp: {
    type: Date,
    required: true
  }
});
const Measurement = mongoose.models.Measurement || mongoose.model('Measurement', measurementSchema);
export default Measurement;
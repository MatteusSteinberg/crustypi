import mongoose, { ConnectOptions } from "mongoose";

mongoose.set('debug', process.env.NODE_ENV !== 'production')

mongoose.set('autoIndex', true);

mongoose.set('maxTimeMS', 10000)

let connection: typeof import("mongoose") | undefined;

async function disconnect() {
  console.log("Close mongodb connection")

  await connection?.disconnect()

  connection = undefined
}

async function connect(cb?: () => Promise<void>) {

  if (connection == null) {
    const options: ConnectOptions = {
      serverSelectionTimeoutMS: 2000
    }

    let uri = process.env.DB_URI as string

    if (!uri) {
      throw ("DB_URI is not configured")
    }

    process.env.LOG && console.log("connection to", uri)

    connection = await mongoose.connect(uri, options)

    console.log("Connected to MongoDB!");

    if (cb) await cb()
  }

  return connection;
}

export { connect, disconnect };
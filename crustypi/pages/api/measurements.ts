import { connect } from '../../config/db'
import runMiddleware from '../../lib/middleware'

import measurementsModel from '../../lib/models/measurements.model'

import { NextApiRequest, NextApiResponse } from 'next'
import Cors from 'cors'


const cors = Cors({
  methods: ['POST', 'GET', 'HEAD'],
})

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  await runMiddleware(req, res, cors)
  await connect()
  if (req.method === 'POST') {
    
    // Process a POST request
    const newMeseurement = await measurementsModel.insertMany(req.body)
    res.status(201).json(newMeseurement)
  }
  if (req.method === 'GET') {
    // Process a GET request
    res.status(200).json({ name: 'John Doe' })
  }
}
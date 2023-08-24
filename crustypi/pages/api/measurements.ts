import { connect } from '../../config/db'
import runMiddleware from '../../lib/middleware'

import measurementsModel from '../../lib/models/measurements.model'

import Cors from 'cors'
import { PipelineStage } from 'mongoose'
import { NextApiRequest, NextApiResponse } from 'next'


const cors = Cors({
  methods: ['POST', 'GET', 'HEAD'],
})

export const config = {
  api: {
    responseLimit: false,
  },
}

export default async function handler(req: NextApiRequest, res: NextApiResponse) {

  await runMiddleware(req, res, cors)
  await connect()
  if (req.method === 'POST') {
    if (req.headers.authorization !== 'Bearer ' + process.env.ALLOW_KEY) {
      res.status(401).json({ error: 'Unauthorized' })
      return
    }
    const newMeseurement = await measurementsModel.insertMany(req.body)

    res.status(201).json(newMeseurement)
  }
  if (req.method === 'GET') {

    const timestampFrom = req.query.timestampFrom ? Array.isArray(req.query.timestampFrom) ? req.query.timestampFrom[0] : req.query.timestampFrom : null
    const timestampTo = req.query.timestampTo ? Array.isArray(req.query.timestampTo) ? req.query.timestampTo[0] : req.query.timestampTo : null
    const groupBy = req.query.groupBy ? req.query.groupBy : null

    const aggreate: PipelineStage[] = [
      ...(!!timestampTo || !!timestampFrom ? [{
        $match: {
          timestamp: {
            ...(!!timestampFrom ? { $gte: new Date(timestampFrom) } : {}),
            ...(!!timestampTo ? { $lte: new Date(timestampTo) } : {})
          }
        }
      }] : []),
      {
        $group: {
          _id: {
            $dateTrunc: {
              date: "$timestamp",
              unit: groupBy || 'day'
            }
          },
          temperature: {
            $avg: "$temperature"
          },
          humidity: {
            $avg: "$humidity"
          },
          pressure: {
            $avg: "$pressure"
          },
          gas: {
            $avg: "$gas"
          },
        }
      },
      {
        $sort: {
          _id: 1
        }
      }
    ]
    res.status(200).json(await measurementsModel.aggregate(aggreate, { allowDiskUse: true, maxTimeMS: 120000 }))
  }
}
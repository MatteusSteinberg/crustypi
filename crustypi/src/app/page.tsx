"use client"

import {
  BarElement,
  CategoryScale,
  Chart as ChartJS,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  Title,
  Tooltip,
} from 'chart.js';
import moment from 'moment';
import { useCallback, useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import useMQTT from '../../lib/hooks/useMQTT';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const options = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top' as const,
    }
  },
};

export default function Home() {
  const [data, setData] = useState([])
  const [groupBy, setGroupBy] = useState("hour")

  const { } = useMQTT()

  const timeFormat = () => {
    switch (groupBy) {
      case "month":
        return 'ddd, hA'
      case "week":
        return 'ddd, hA'
      case "day":
        return 'ddd'
      case "hour":
        return 'ddd, hA'
      case "minute":
        return 'ddd, h:mmA'
      case "second":
        return 'ddd, h:mm:ssA'
    }
  }

  const getData = useCallback(async () => {
    await fetch(`/api/measurements?groupBy=${groupBy}`)
      .then(res => res.json())
      .then(data => setData(data))
      .catch(err => console.log(err))
  }, [groupBy])

  const labels = data.map((item: any) => moment(item._id).format(timeFormat()));

  const color: { [key: string]: { borderColor: string, backgroundColor: string } } = {
    temperature: {
      borderColor: 'rgb(255, 99, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
    },
    humidity: {
      borderColor: 'rgb(54, 162, 235)',
      backgroundColor: 'rgba(54, 162, 235, 0.5)',
    },
    pressure: {
      borderColor: 'rgb(75, 192, 192)',
      backgroundColor: 'rgba(75, 192, 192, 0.5)',
    },
    gas: {
      borderColor: 'rgb(255, 205, 86)',
      backgroundColor: 'rgba(255, 205, 86, 0.5)',
    },
  }

  const createChart = () => {
    const chartElements = [];
    const charts = data[0] ? Object.keys(data[0]).filter((item: string) => item !== "_id") : [];
    for (const chart of charts) {
      const generatedChart = {
        labels,
        datasets: [
          {
            label: chart.charAt(0).toUpperCase() + chart.slice(1),
            data: data.map((item: any) => item[chart]),
            borderColor: color[chart].borderColor,
            backgroundColor: color[chart].backgroundColor,
          },
        ],
      }
      chartElements.push(<Line key={chart} data={generatedChart} options={options} />)
    }
    return chartElements;
  }

  useEffect(() => {
    const interval = setInterval(() => {
      getData()
    }, 10000);
    return () => clearInterval(interval);
  }, [getData])

  return (
    <main>
      <div className="container">
        <div className='header'>
          <h1>Crusty Pi</h1>
        </div>
        <div>
          <select defaultValue={groupBy} onChange={(ev) => setGroupBy(ev.target.value)}>
            <option value={"month"}>Month</option>
            <option value={"week"}>Week</option>
            <option value={"day"}>Day</option>
            <option value={"hour"}>Hour</option>
            <option value={"minute"}>Minute</option>
          </select>
        </div>
        <div className='content'>
          <div className='charts'>
            {createChart()}
          </div>
        </div>
      </div>
    </main>
  )
}

"use client"

import React, { useEffect, useState } from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar, Line } from 'react-chartjs-2';
import moment from 'moment';

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

  useEffect(() => {
    const interval = setInterval(() => {
      getData()
    }, 10000);
    return () => clearInterval(interval);
  }, [])
  
  const getData = async () => {
    await fetch('/api/measurements?groupBy=hour')
      .then(res => res.json())
      .then(data => setData(data))
      .catch(err => console.log(err))
  }

  const labels = data.map((item: any) => moment(item._id).format('ddd, hA'));

  console.log(data)

  const temperature = {
    labels,
    datasets: [
      {
        label: 'Temperature',
        data: data.map((item: any) => item.temperature),
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
      }
    ],
  };

  const humidity = {
    labels,
    datasets: [
      {
        label: 'Humidity',
        data: data.map((item: any) => item.humidity),
        borderColor: 'rgb(53, 162, 235)',
        backgroundColor: 'rgba(53, 162, 235, 0.5)',
      },
    ],
  }

  const pressure = {
    labels,
    datasets: [
      {
        label: 'Pressure',
        data: data.map((item: any) => item.pressure),
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: 'rgba(75, 192, 192, 0.5)',
      },
    ],
  }

  const gas = {
    labels,
    datasets: [
      {
        label: 'Gas',
        data: data.map((item: any) => item.gas),
        borderColor: 'rgb(255, 205, 86)',
        backgroundColor: 'rgba(255, 205, 86, 0.5)',
      },
    ],
  }

  return (
    <main>
      <div className="container">
        <div className='header'>
          <h1>Crusty Pi</h1>
        </div>
        <div className='content'>
          <div className='charts'>
            <Line options={options} data={temperature} />
            <Line options={options} data={humidity} />
            <Line options={options} data={pressure} />
            <Line options={options} data={gas} />
          </div>
        </div>
      </div>
    </main>
  )
}

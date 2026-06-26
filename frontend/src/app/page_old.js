"use client";

import { useEffect, useState } from "react";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

export default function Home() {
  const [uploads, setUploads] = useState([]);
  const [monthlySales, setMonthlySales] = useState([]);
  const [file, setFile] = useState(null);

  const totalSales = uploads.reduce(
    (sum, item) => sum + item.total_sales,
    0
  );

  const totalOrders = uploads.reduce(
    (sum, item) => sum + item.total_orders,
    0
  );

  const chartData = uploads.map((item) => ({
    name: item.filename,
    sales: item.total_sales,
  }));
  const monthlyChartData = monthlySales;
  const loadData = () => {
    fetch("http://localhost:8000/api/upload")
      .then((res) => res.json())
      .then((data) => setUploads(data))
    fetch("http://localhost:8000/api/analytics/monthly-sales")
      .then((res) => res.json())
      .then((data) => {
        const chart = Object.entries(data).map(([month, sales]) => ({
          month,
          sales,
      }));

      setMonthlySales(chart);
    });  
    .catch((err) => console.error(err));
  };

  useEffect(() => {
    loadData();
  }, []);

  const handleUpload = async () => {
    if (!file) {
      alert("یک فایل انتخاب کنید");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch(
      "http://localhost:8000/api/upload",
      {
        method: "POST",
        body: formData,
      }
    );

    if (res.ok) {
      alert("آپلود موفق");
      setFile(null);
      loadData();
    } else {
      alert("خطا در آپلود");
    }
  };

  return (
    <main className="p-10">
      <h1 className="text-3xl font-bold mb-6">
        BotNara Dashboard
      </h1>

      <div className="grid grid-cols-4 gap-4 mb-8">
        <div className="border rounded-lg p-4 shadow">
          <h3 className="font-bold">📁 فایل‌ها</h3>
          <p className="text-2xl">{uploads.length}</p>
        </div>

        <div className="border rounded-lg p-4 shadow">
          <h3 className="font-bold">💰 فروش کل</h3>
          <p className="text-2xl">
            {totalSales.toLocaleString()}
          </p>
        </div>

        <div className="border rounded-lg p-4 shadow">
          <h3 className="font-bold">🛒 سفارش‌ها</h3>
          <p className="text-2xl">{totalOrders}</p>
        </div>

        <div className="border rounded-lg p-4 shadow">
          <h3 className="font-bold">👤 آخرین مشتری برتر</h3>
          <p className="text-xl">
            {uploads[0]?.top_customer || "-"}
          </p>
        </div>
      </div>

      <div className="border rounded p-4 mb-8">
        <input
          type="file"
          accept=".xlsx,.xls"
          onChange={(e) =>
            setFile(e.target.files[0])
          }
        />

        <button
          onClick={handleUpload}
          className="ml-4 px-4 py-2 border rounded"
        >
          Upload Excel
        </button>
      </div>

      <div className="border rounded-lg p-4 mb-8 shadow">
        <h2 className="text-xl font-bold mb-4">
          📊 نمودار فروش فایل‌ها
        </h2>

        <div style={{ width: "100%", height: 300 }}>
          <ResponsiveContainer>
            <BarChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="sales" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {uploads.map((item) => (
        <div
          key={item.id}
          className="border rounded p-4 mb-4"
        >
          <p>📄 {item.filename}</p>
          <p>💰 فروش: {item.total_sales}</p>
          <p>🛒 سفارش: {item.total_orders}</p>
          <p>👤 مشتری برتر: {item.top_customer}</p>
          <p>📦 محصول برتر: {item.top_product}</p>
        </div>
      ))}
    </main>
  );
}
<div className="border rounded-lg p-4 mb-8 shadow">
  <h2 className="text-xl font-bold mb-4">
    📈 فروش ماهانه
  </h2>

  <div style={{ width: "100%", height: 300 }}>
    <ResponsiveContainer>
      <BarChart data={monthlyChartData}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="month" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="sales" />
      </BarChart>
    </ResponsiveContainer>
  </div>
</div>

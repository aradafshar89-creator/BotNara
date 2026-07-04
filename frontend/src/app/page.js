"use client";

import ForecastCard from "../components/ForecastCard";
import AdvisorCard from "../components/AdvisorCard";
import ProfitCards from "../components/ProfitCards";
import DashboardCards from "../components/DashboardCards";
import { useEffect, useState } from "react";

import {
  ResponsiveContainer,
  BarChart,
  Bar,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
} from "recharts";

export default function Home() {

  const [uploads, setUploads] = useState([]);
  const [monthlySales, setMonthlySales] = useState([]);
  const [topCustomers, setTopCustomers] = useState([]);
  const [topProducts, setTopProducts] = useState([]);
  const [profit, setProfit] = useState(null);
  const [advice, setAdvice] = useState([]);
  const [forecast, setForecast] = useState("");

  const [file, setFile] = useState(null);

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const loadData = async () => {

    try {

      const uploadsRes = await fetch(
        "http://localhost:8000/api/upload"
      );

      const uploadsData = await uploadsRes.json();

      setUploads(uploadsData);

      const monthlyRes = await fetch(
        "http://localhost:8000/api/analytics/monthly-sales"
      );

      const monthlyData = await monthlyRes.json();

      setMonthlySales(
        Object.entries(monthlyData).map(([month, sales]) => ({
          month,
          sales,
        }))
      );

      const customersRes = await fetch(
        "http://localhost:8000/api/analytics/top-customers"
      );

      setTopCustomers(await customersRes.json());

      const productsRes = await fetch(
        "http://localhost:8000/api/analytics/top-products"
      );

      setTopProducts(await productsRes.json());

      const profitRes = await fetch(
        "http://localhost:8000/api/analytics/profit"
      );

      setProfit(await profitRes.json());

    } catch (err) {

      console.error(err);

    }

  };
const loadAdvisor = async () => {

  try {

    const res = await fetch(
      "http://localhost:8000/api/advisor"
    );

    const data = await res.json();

    setAdvice(data.advice);

  } catch (err) {

    console.error(err);

  }

};
const askBot = async () => {

    if (!question.trim()) return;

    setLoading(true);

    try {

      const res = await fetch(
        "http://localhost:8000/api/chat",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            message: question,
          }),
        }
      );

      const data = await res.json();

      setAnswer(data.reply);

    } catch (err) {

      console.error(err);

      setAnswer("خطا در ارتباط با BotNara");

    }

    setLoading(false);

  };

  useEffect(() => {

    loadData();
    loadAdvisor();

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

  return (

    <main className="p-10 bg-gray-50 min-h-screen">
<h1 className="text-4xl font-bold mb-8">
        🚀 BotNara Dashboard
      </h1>

<DashboardCards
  uploads={uploads}
  totalSales={totalSales}
  totalOrders={totalOrders}
/>

<ProfitCards profit={profit} />

<AdvisorCard advice={advice} />

<ForecastCard forecast={forecast} />

      <div className="bg-white rounded-xl shadow p-5 mb-8">

        <input
          type="file"
          accept=".xlsx,.xls"
          onChange={(e) =>
            setFile(e.target.files[0])
          }
        />

        <button
          onClick={handleUpload}
          className="ml-4 px-5 py-2 rounded bg-blue-600 text-white"
        >
          Upload Excel
        </button>

      </div>
<div className="grid grid-cols-2 gap-8 mb-8">

        <div className="bg-white rounded-xl shadow p-5">

          <h2 className="font-bold mb-4">
            📊 فروش فایل‌ها
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

        <div className="bg-white rounded-xl shadow p-5">

          <h2 className="font-bold mb-4">
            📈 فروش ماهانه
          </h2>

          <div style={{ width: "100%", height: 300 }}>
            <ResponsiveContainer>
              <BarChart data={monthlySales}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="month" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="sales" />
              </BarChart>
            </ResponsiveContainer>
          </div>

        </div>

      </div>

      <div className="grid grid-cols-2 gap-8 mb-8">

        <div className="bg-white rounded-xl shadow p-5">

          <h2 className="text-xl font-bold mb-4">
            🏆 مشتریان برتر
          </h2>

          {topCustomers.map((item, index) => (

            <div
              key={index}
              className="flex justify-between border-b py-2"
            >
              <span>{item.customer}</span>
              <span>{Number(item.sales).toLocaleString()}</span>
            </div>

          ))}

        </div>

        <div className="bg-white rounded-xl shadow p-5">

          <h2 className="text-xl font-bold mb-4">
            📦 محصولات برتر
          </h2>

          {topProducts.map((item, index) => (

            <div
              key={index}
              className="flex justify-between border-b py-2"
            >
              <span>{item.product}</span>
              <span>{Number(item.sales).toLocaleString()}</span>
            </div>

          ))}

        </div>

      </div>

      <div className="bg-white rounded-xl shadow p-5 mb-8">

        <h2 className="text-xl font-bold mb-4">
          🤖 BotNara AI
        </h2>

        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="مثلاً: پرفروش‌ترین محصول چیست؟"
          className="border rounded w-full p-3 mb-4"
        />

        <button
          onClick={askBot}
          className="px-5 py-2 rounded bg-blue-600 text-white"
        >
          {loading ? "درحال پردازش..." : "ارسال"}
        </button>

        {answer && (

          <div className="mt-6 rounded border bg-gray-100 p-4">

            <strong>BotNara:</strong>

            <p className="mt-2">
              {answer}
            </p>

          </div>

        )}

      </div>

    </main>

  );

}

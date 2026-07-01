"use client";

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

  const [file, setFile] = useState(null);

  const [question, setQuestion] = useState("");

  const [answer, setAnswer] = useState("");

  const [loading, setLoading] = useState(false);

  const loadData = async () => {

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

      const uploadsData = await uploadsRes.json();

      setUploads(uploadsData);

      const monthlyRes = await fetch(
        "http://localhost:8000/api/analytics/monthly-sales"
      );

      const monthlyData = await monthlyRes.json();

      setMonthlySales(
        Object.entries(monthlyData).map(
          ([month, sales]) => ({
            month,
            sales,
          })
        )
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

  const totalSales =
    uploads.reduce(
      (sum, item) => sum + item.total_sales,
      0
    );

  const totalOrders =
    uploads.reduce(
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

      <div className="grid grid-cols-4 gap-4 mb-10">

        <div className="bg-white rounded-xl shadow p-5">

          <h3 className="font-bold mb-2">📁 فایل‌ها</h3>

          <p className="text-3xl">{uploads.length}</p>

        </div>

        <div className="bg-white rounded-xl shadow p-5">

          <h3 className="font-bold mb-2">💰 فروش کل</h3>

          <p className="text-3xl">

            {totalSales.toLocaleString()}

          </p>

        </div>

        <div className="bg-white rounded-xl shadow p-5">

          <h3 className="font-bold mb-2">🛒 سفارش‌ها</h3>

          <p className="text-3xl">

            {totalOrders}

          </p>

        </div>

        <div className="bg-white rounded-xl shadow p-5">

          <h3 className="font-bold mb-2">

            👤 مشتری برتر

          </h3>

          <p className="text-xl">

            {uploads[0]?.top_customer || "-"}

          </p>

        </div>

      </div>

      {profit && (

        <div className="grid grid-cols-4 gap-4 mb-10">

          <div className="bg-green-100 rounded-xl p-5 shadow">

            <h3>💵 سود کل</h3>

            <p className="text-2xl">

              {profit.total_profit.toLocaleString()}

            </p>

          </div>

          <div className="bg-blue-100 rounded-xl p-5 shadow">

            <h3>💰 هزینه خرید</h3>

            <p className="text-2xl">

              {profit.total_purchase.toLocaleString()}

            </p>

          </div>

          <div className="bg-yellow-100 rounded-xl p-5 shadow">

            <h3>📈 حاشیه سود</h3>

            <p className="text-2xl">

              {profit.margin_percent}%

            </p>

          </div>

          <div className="bg-purple-100 rounded-xl p-5 shadow">

            <h3>📊 فروش کل دیتابیس</h3>

            <p className="text-2xl">

              {profit.total_sales.toLocaleString()}

            </p>

          </div>

        </div>

      )}

      <div className="bg-white rounded-xl shadow p-5 mb-10">

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

      <div className="grid grid-cols-2 gap-8 mb-10">

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
<div className="grid grid-cols-2 gap-8 mb-10">

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

              <span>
                {Number(item.sales).toLocaleString()}
              </span>

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

              <span>
                {Number(item.sales).toLocaleString()}
              </span>

            </div>

          ))}

        </div>

      </div>

      <div className="bg-white rounded-xl shadow p-5">

        <h2 className="text-xl font-bold mb-5">

          📄 فایل‌های آپلود شده

        </h2>

        {uploads.map((item) => (

          <div
            key={item.id}
            className="border rounded-lg p-4 mb-4"
          >

            <p>📄 {item.filename}</p>

            <p>
              💰 فروش:
              {" "}
              {Number(item.total_sales).toLocaleString()}
            </p>

            <p>
              🛒 سفارش:
              {" "}
              {item.total_orders}
            </p>

            <p>
              👤 مشتری برتر:
              {" "}
              {item.top_customer}
            </p>

            <p>
              📦 محصول برتر:
              {" "}
              {item.top_product}
            </p>

          </div>

        ))}

      </div>

<div className="border rounded-lg p-6 shadow mt-8">

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
    className="px-4 py-2 bg-blue-600 text-white rounded"
  >
    {loading ? "درحال پردازش..." : "ارسال"}
  </button>

  {answer && (

    <div className="mt-6 border rounded p-4 bg-gray-100">

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

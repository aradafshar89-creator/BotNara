export default function DashboardCards({
  uploads,
  totalSales,
  totalOrders,
}) {
  return (
    <div className="grid grid-cols-4 gap-4 mb-8">

      <div className="bg-white rounded-xl shadow p-5">
        <h3 className="font-bold">📁 فایل‌ها</h3>
        <p className="text-3xl">{uploads.length}</p>
      </div>

      <div className="bg-white rounded-xl shadow p-5">
        <h3 className="font-bold">💰 فروش کل</h3>
        <p className="text-3xl">
          {Number(totalSales).toLocaleString()}
        </p>
      </div>

      <div className="bg-white rounded-xl shadow p-5">
        <h3 className="font-bold">🛒 سفارش‌ها</h3>
        <p className="text-3xl">
          {totalOrders}
        </p>
      </div>

      <div className="bg-white rounded-xl shadow p-5">
        <h3 className="font-bold">
          👤 مشتری برتر
        </h3>

        <p className="text-xl">
          {uploads[0]?.top_customer || "-"}
        </p>

      </div>

    </div>
  );
}

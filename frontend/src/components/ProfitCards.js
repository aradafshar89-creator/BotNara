export default function ProfitCards({ profit }) {

  if (!profit) return null;

  return (

    <div className="grid grid-cols-4 gap-4 mb-8">

      <div className="bg-green-100 rounded-xl p-5">
        <h3>💵 سود کل</h3>
        <p>{Number(profit.total_profit).toLocaleString()}</p>
      </div>

      <div className="bg-blue-100 rounded-xl p-5">
        <h3>💰 هزینه خرید</h3>
        <p>{Number(profit.total_purchase).toLocaleString()}</p>
      </div>

      <div className="bg-yellow-100 rounded-xl p-5">
        <h3>📈 حاشیه سود</h3>
        <p>{profit.margin_percent}%</p>
      </div>

      <div className="bg-purple-100 rounded-xl p-5">
        <h3>📊 فروش دیتابیس</h3>
        <p>{Number(profit.total_sales).toLocaleString()}</p>
      </div>

    </div>

  );

}

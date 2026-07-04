export default function ForecastCard({ forecast }) {

  return (

    <div className="bg-white rounded-xl shadow p-5 mb-8">

      <h2 className="text-xl font-bold mb-4">

        📈 پیش‌بینی فروش

      </h2>

      <pre className="whitespace-pre-wrap text-gray-700">

        {forecast}

      </pre>

    </div>

  );

}

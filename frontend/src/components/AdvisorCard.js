export default function AdvisorCard({ advice }) {

  return (

    <div className="bg-white rounded-xl shadow p-5 mb-8">

      <h2 className="text-xl font-bold mb-4">

        🧠 پیشنهادهای امروز BotNara

      </h2>

      {advice.length === 0 ? (

        <p className="text-gray-500">

          در حال دریافت تحلیل...

        </p>

      ) : (

        advice.map((item, index) => (

          <div
            key={index}
            className="border-b py-2"
          >

            {item}

          </div>

        ))

      )}

    </div>

  );

}

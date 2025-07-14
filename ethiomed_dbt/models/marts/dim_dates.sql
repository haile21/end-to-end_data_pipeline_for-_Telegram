with dates as (
  select generate_series(
    (select min(message_date) from {{ ref('stg_telegram_messages') }}),
    (select max(message_date) from {{ ref('stg_telegram_messages') }}),
    interval '1 day'
  )::date as date
)

select
  date,
  extract(dow from date) as day_of_week,
  extract(week from date) as week_of_year,
  extract(month from date) as month,
  extract(year from date) as year
from dates

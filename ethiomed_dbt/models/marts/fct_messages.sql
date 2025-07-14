select
  message_id,
  message_date::date as date,
  channel as channel_name,
  length(text) as message_length,
  has_media
from {{ ref('stg_telegram_messages') }}

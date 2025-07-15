select
  i.message_id,
  i.class_name as detected_object_class,
  i.confidence,
  m.message_date,
  m.channel as channel_name
from raw.image_detections i
join {{ ref('stg_telegram_messages') }} m
  on i.message_id = m.message_id

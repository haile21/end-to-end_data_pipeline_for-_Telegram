with raw as (
  select
    (message->>'id')::bigint as message_id,
    (message->>'message') as text,
    (message->>'date')::timestamp as message_date,
    (message->>'from_id') as sender_id,
    (message->'media') is not null as has_media,
    channel,
    scraped_at
  from raw.telegram_messages
)

select * from raw;

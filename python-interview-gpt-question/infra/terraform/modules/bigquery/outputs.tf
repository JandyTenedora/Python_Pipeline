output "dataset_id" {
  description = "The ID of the BigQuery dataset."
  value       = google_bigquery_dataset.dataset.dataset_id
}

output "dataset_self_link" {
  description = "The self-link of the BigQuery dataset."
  value       = google_bigquery_dataset.dataset.self_link
}

output "table_ids" {
  description = "The IDs of the tables created in the dataset."
  value       = { for table, details in google_bigquery_table.table : table => details.table_id }
}

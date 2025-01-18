resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.dataset_id
  project = var.project_id
  location = var.location
  description = var.description

  labels = var.labels
}


resource "google_bigquery_table" "table" {
  for_each = var.tables
  deletion_protection = false
  table_id = each.key
  dataset_id = google_bigquery_dataset.dataset.dataset_id
  project = var.project_id
  schema = each.value.schema
  description = each.value.description
}
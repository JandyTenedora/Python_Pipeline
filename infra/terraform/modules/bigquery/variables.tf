variable "project_id" {
  description = "The GCP project ID where the BigQuery dataset will be created."
  type        = string
}

variable "dataset_id" {
  description = "The ID of the BigQuery dataset to create."
  type        = string
}

variable "location" {
  description = "The location for the dataset (e.g., US or EU)."
  type        = string
  default     = "EU"
}

variable "description" {
  description = "A description for the BigQuery dataset."
  type        = string
  default     = "Dataset created via Terraform."
}

variable "labels" {
  description = "Labels to apply to the BigQuery dataset."
  type        = map(string)
  default     = {}
}

variable "tables" {
  description = "A map of table definitions to create in the dataset."
  type = map(object({
    schema      = string
    description = string
  }))
  default = {}
}

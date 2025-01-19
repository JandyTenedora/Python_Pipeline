variable "project_id" {
  description = "The GCP project ID where the Firestore database will be created."
  type        = string
}

variable "database_name" {
  description = "The name of the Firestore database."
  type        = string
}

variable "location_id" {
  description = "The location ID for the Firestore database."
  type        = string
}
